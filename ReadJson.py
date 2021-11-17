import json

from Building import Building
from Elevator import Elevator


class ReadJson:

    def __init__(self, file_name):
        # Opening JSON file
        f = open(file_name, )

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        self.fileName = file_name
        self.building = self.get_building(data)

        f.close()

    @classmethod
    def get_elevators(cls, data):
        elevators = []
        for elevator_data in data['_elevators']:
            elevator = cls.get_elevator(elevator_data)
            elevators.append(elevator)
        return elevators

    @classmethod
    def get_elevator(cls, data):
        elevator = Elevator(data['_id'], data['_speed'], data['_minFloor'], data['_maxFloor'], data['_closeTime'],
                            data['_openTime'], data['_startTime'], data['_stopTime'])
        return elevator

    @classmethod
    def get_building(cls, data):
        min_floor = data['_minFloor']
        max_floor = data['_maxFloor']
        elevators = cls.get_elevators(data)
        building = Building(min_floor, max_floor, elevators)
        return building
