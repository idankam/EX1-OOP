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
        self.allocate()

    def allocate(self):
        self.foreign_allocate()
        self.parrallel_allocate_range()
        self.calls["Index"] = self.elevators_allocated
        self.get_output_file()

    def parrallel_allocate_range(self):
        counter = 0
        for index, call in self.not_allocated_calls.iterrows():  # for each call check if can assign to some elev as foreign call
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
        allocated = []
        for index, call in self.calls.iterrows():  # for each call check if can assign to some elev as foreign call
            times = {}
            tmp_calls = {}
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
                self.elevators_allocated.append(-1)
        self.not_allocated_calls.drop(allocated, inplace=True)

    def is_foreign(self, index, call_time):
        elevator = self.building.elevators[index]
        if elevator.allocatedCalls[-1].finish_time <= call_time:
            return True
        return False

    def get_output_file(self):
        self.calls.to_csv(self.output_file, header=False, index=False)
