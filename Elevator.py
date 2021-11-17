import numpy as np

from AllocatedCall import AllocatedCall


class Elevator:
    UP = 1
    DOWN = -1
    LEVEL = 0

    def __init__(self, ID, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime):
        self.id = ID
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.allocatedCalls = []
        # check if needed:
        # self.position = 0
        # self.goto = np.nan
        self.sumStartTime = np.round(closeTime+startTime)
        self.sumStopTime = np.round(openTime+stopTime)
        #self.sumStartTime = closeTime + startTime
        #self.sumStopTime = openTime + stopTime
        # self.startCounter = self.sumStartTime
        # self.stopCounter = self.sumStopTime
        # self.direction = Elevator.LEVEL
        self.allocatedCalls.append(AllocatedCall.first_call(self))

    # def set_position(self):
    #     if self.goto != np.nan:
    #         if self.startCounter > 0:
    #             self.startCounter -= 1
    #         elif self.position != self.goto:
    #             if self.direction == Elevator.UP:
    #                 if (self.position + self.speed) >= self.goto:
    #                     self.position = self.goto
    #                 else:
    #                     self.position += self.speed
    #             else:  # DOWN
    #                 if (self.position - self.speed) <= self.goto:
    #                     self.position = self.goto
    #                 else:
    #                     self.position -= self.speed
    #         elif self.stopCounter > 0:
    #             self.stopCounter -= 1
    #             if self.stopCounter == 0:
    #                 self.startCounter = self.sumStartTime
    #                 self.stopCounter = self.sumStopTime
    #                 self.direction = Elevator.LEVEL
    #                 self.goto = np.nan
