import numpy as np


class AllocatedCall:
    def __init__(self, ID, src, dst, start_pos, start_time, elevator):
        self.id = ID
        self.src = src
        self.dst = dst
        self.start_pos = start_pos
        self.start_time = np.ceil(start_time)
        time = (elevator.sumStartTime + elevator.sumStopTime) + np.round((1 / elevator.speed) * (np.abs(start_pos - src))) + np.round((1 / elevator.speed) * np.abs(src - dst))
        # print((elevator.sumStartTime + elevator.sumStopTime))
        # print(np.ceil(1 / elevator.speed * (np.abs(start_pos - src))))
        # print(np.ceil(1 / elevator.speed * np.abs(src - dst)))
        if src != start_pos:
            time += (elevator.sumStartTime + elevator.sumStopTime)
        self.finish_time = self.start_time + time

    @classmethod
    def first_call(cls, elevator):
        first = AllocatedCall(-1, 0, 0, 0, 0.0, elevator)
        first.finish_time = 0.0
        return first
