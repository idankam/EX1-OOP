from ReadJson import ReadJson
from Offline import Offline
import sys


def main(argv):
    json_file = argv[0]
    calls_input = argv[1]
    calls_output = argv[2]
    json_object = ReadJson(json_file)
    building = json_object.building
    algo = Offline(building, calls_input, calls_output)


if __name__ == '__main__':
    #main(sys.argv[1:])
    main(["B5.json", "Calls_d.csv", "out.csv"])
