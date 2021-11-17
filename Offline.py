import pandas as pd
import numpy as np
import os

from AllocatedCall import AllocatedCall
from Building import Building
from Elevator import Elevator


class Offline:
    def __init__(self, building, calls_file, output_file):
        self.building = building
        self.calls = pd.read_csv(calls_file, names=["Elevator calls:", "Time", "SRC", "DST", "Status", "Index"])
        self.not_allocated_calls = self.calls.copy(deep=True)
        self.output_file = output_file
        self.elevators_allocated = []
        # for i in range(len(self.building.elevators)):
        #     self.elevators_calls.add([])
        self.allocate()

    def allocate(self):
        #self.just_foreign_allocate()
        self.foreign_allocate()
        self.parrallel_allocate_range()
        #self.parrallel_allocate_min_calls()
        #self.parrallel_allocate()
        # self.last_allocate()
        self.calls["Index"] = self.elevators_allocated
        self.get_output_file()

    # def allocate_random(self):
    #     elev_id = range(0, len(self.building.elevators))
    #     indexes = np.random.choice(elev_id, size=self.calls.index.size)
    #     self.calls["Index"] = indexes
    #     self.get_output_file()

    def parrallel_allocate(self):
        for index, call in self.not_allocated_calls.iterrows():  # for each call check if can assign to some elev as foreign call
            times = {}
            max_key = -1
            for i in range(len(self.building.elevators)):
                calls_list = self.building.elevators[i].allocatedCalls
                k = 0
                while k < len(calls_list) - 1 and index > calls_list[k].id: k += 1
                if k == len(calls_list) - 1:
                    max_key = i
                else:
                    last_finish_time = calls_list[k - 1].finish_time
                    next_start_time = calls_list[k].start_time
                    diff_time = next_start_time - last_finish_time
                    times[i] = diff_time
            times_list = list(times.values())
            keys_list = list(times.keys())
            if len(times_list)>0:
                max_key = keys_list[times_list.index(max(times_list))]
                self.elevators_allocated[index] = max_key
            else:
                elev_id = range(0, len(self.building.elevators))
                key_rand = np.random.choice(elev_id, size=1)[0]
                self.elevators_allocated[index] = key_rand
            # if max_key != -1 and max(times_list) < 10:
            #     self.elevators_allocated[index] = max_key

    # def parrallel_allocate_min_calls(self):
    #     for index, call in self.not_allocated_calls.iterrows():  # for each call check if can assign to some elev as foreign call
    #         more_calls_dict = {}
    #         for i in range(len(self.building.elevators)):
    #             calls_list = self.building.elevators[i].allocatedCalls
    #             k = 0
    #             while k < len(calls_list) - 1 and index > calls_list[k].id: k += 1
    #             more_calls = len(calls_list) - k
    #             more_calls_dict[i] = more_calls
    #         amount_more_calls_list = list(more_calls_dict.values())
    #         keys_list = list(more_calls_dict.keys())
    #         min_key = keys_list[amount_more_calls_list.index(min(amount_more_calls_list))]
    #         self.elevators_allocated[index] = min_key

    def parrallel_allocate(self):
        for index, call in self.not_allocated_calls.iterrows():  # for each call check if can assign to some elev as foreign call
            times = {}
            max_key = -1
            for i in range(len(self.building.elevators)):
                calls_list = self.building.elevators[i].allocatedCalls
                k = 0
                while k < len(calls_list) - 1 and index > calls_list[k].id: k += 1
                if k == len(calls_list) - 1:
                    max_key = i
                else:
                    last_finish_time = calls_list[k - 1].finish_time
                    next_start_time = calls_list[k].start_time
                    diff_time = next_start_time - last_finish_time
                    times[i] = diff_time
            times_list = list(times.values())
            keys_list = list(times.keys())
            if len(times_list)>0:
                max_key = keys_list[times_list.index(max(times_list))]
                self.elevators_allocated[index] = max_key
            else:
                elev_id = range(0, len(self.building.elevators))
                key_rand = np.random.choice(elev_id, size=1)[0]
                self.elevators_allocated[index] = key_rand
            # if max_key != -1 and max(times_list) < 10:
            #     self.elevators_allocated[index] = max_key

    def parrallel_allocate_range(self):
        counter = 0
        for index, call in self.not_allocated_calls.iterrows():  # for each call check if can assign to some elev as foreign call
            # more_calls_dict = {}
            for i in range(len(self.building.elevators)):
                calls_list = self.building.elevators[i].allocatedCalls
                k = 0
                while k < len(calls_list) - 1 and index > calls_list[k].id: k += 1
                if calls_list[k].src < calls_list[k].dst and calls_list[k].src <= call['SRC'] <= call['DST']: # both up
                    self.elevators_allocated[index] = i
                    break
                elif calls_list[k].src > calls_list[k].dst and calls_list[k].src >= call['SRC'] >= call['DST']:# both down
                    self.elevators_allocated[index] = i
                    break
            if self.elevators_allocated[index] == -1:
                self.elevators_allocated[index] = counter % len(self.building.elevators)
                counter += 1

    def foreign_allocate(self):
        counter = 0
        allocated = []
        random_allocated = []
        for index, call in self.calls.iterrows():  # for each call check if can assign to some elev as foreign call
            times = {}
            tmp_calls = {}
            print(call)
            print("index=" + str(index))
            for i in range(len(self.building.elevators)):
                if self.is_foreign(i, call['Time']):
                    elevator = self.building.elevators[i]
                    tmp_call = AllocatedCall(ID=index, src=call['SRC'], dst=call['DST'],
                                             start_pos=elevator.allocatedCalls[-1].dst,
                                             start_time=call['Time'], elevator=elevator)
                    times[i] = tmp_call.finish_time - tmp_call.start_time
                    tmp_calls[i] = tmp_call
            if len(times) > 0:
                times_list = list(times.values())
                keys_list = list(times.keys())
                min_key = keys_list[times_list.index(min(times_list))]
                best_elevator = self.building.elevators[min_key]
                best_elevator.allocatedCalls.append(tmp_calls.get(min_key))
                allocated.append(index)
                self.elevators_allocated.append(min_key)
            else:
                self.elevators_allocated.append(-1)  # not allocated yet
            #     # elev_id = range(0, len(self.building.elevators))
            #     # key_rand = np.random.choice(elev_id, size=1)[0]
            #     key_rand = counter % len(self.building.elevators)
            #     counter+=1
            #     random_allocated.append(key_rand)
            #     self.elevators_allocated.append(key_rand)
        print(allocated)
        print(len(allocated))
        # print(random_allocated)
        # print(len(random_allocated))
        self.not_allocated_calls.drop(allocated, inplace=True)
        print(self.not_allocated_calls)

    def just_foreign_allocate(self):
        counter = 0
        allocated = []
        random_allocated = []
        for index, call in self.calls.iterrows():  # for each call check if can assign to some elev as foreign call
            times = {}
            tmp_calls = {}
            print(call)
            print("index=" + str(index))
            for i in range(len(self.building.elevators)):
                if self.is_foreign(i, call['Time']):
                    elevator = self.building.elevators[i]
                    tmp_call = AllocatedCall(ID=index, src=call['SRC'], dst=call['DST'],
                                             start_pos=elevator.allocatedCalls[-1].dst,
                                             start_time=call['Time'], elevator=elevator)
                    times[i] = tmp_call.finish_time - tmp_call.start_time
                    tmp_calls[i] = tmp_call
            if len(times) > 0:
                times_list = list(times.values())
                keys_list = list(times.keys())
                min_key = keys_list[times_list.index(min(times_list))]
                best_elevator = self.building.elevators[min_key]
                best_elevator.allocatedCalls.append(tmp_calls.get(min_key))
                allocated.append(index)
                self.elevators_allocated.append(min_key)
                print("foreign " + str(index) + " finish time:")
                print(tmp_calls.get(min_key).finish_time)
                print()
            else:
                #self.elevators_allocated.append(-1)  # not allocated yet
                key_rand = counter % len(self.building.elevators)
                counter+=1
                random_allocated.append(key_rand)
                self.elevators_allocated.append(key_rand)
        print(allocated)
        print(len(allocated))
        print(random_allocated)
        print(len(random_allocated))
        self.not_allocated_calls.drop(allocated, inplace=True)
        print(self.not_allocated_calls)

    def last_allocate(self):
        pass

    def is_foreign(self, index, call_time):
        elevator = self.building.elevators[index]
        if elevator.allocatedCalls[-1].finish_time <= call_time:
            return True
        return False

    def get_output_file(self):
        self.calls.to_csv(self.output_file, header=False, index=False)
