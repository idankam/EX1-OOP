# EX1-OOP

This project implements an offline elevator placement algorithm.

### Review of the Literature:
1.	https://www.geeksforgeeks.org/look-disk-scheduling-algorithm/
2.	https://en.wikipedia.org/wiki/Elevator_algorithm
3.	https://en.wikipedia.org/wiki/LOOK_algorithm
4.	https://thinksoftware.medium.com/elevator-system-design-a-tricky-technical-interview-question-116f396f2b1c

After perusing these sources, we saw a number of methods for the algorithm that assigns an elevator to a specific reading. The general idea we chose from these methods - LOOK AHEAD algorithm. In this approach, each elevator moves in a defined direction (ascending or descending) which changes only when it is at rest, i.e., there are no more readings that are embedded in this elevator. When there is one elevator, the system scans the collection of given readings and selects the appropriate readings for the direction of movement of the elevator and its current location. This creates a defined sequence of floors where the elevator has to stop. When the elevator stops (finished the readings) it will select a new direction (up / down) according to the first reading that is in the system and then the system will again cross out readings that correspond to the movement of the elevator and the floor where it is currently. When there is more than one elevator, the system must in addition to the scan described above also decide which elevator will be selected to perform the reading.

### Offline Algorithm Idea:
Since in the literature review most of the ideas are for an online algorithm, we have thought of a different way of realization.
First, we will assign all the readings which are foreign to each other in terms of start and end times. That is, each elevator is assigned only readings that do not overlap in terms of working hours. Also, the allocation of foreign calls is optimally done - the elevator that will finish the call the fastest will be assigned to that call.
The algorithm then goes over the readings that were not initially assigned (i.e., they overlap with other readings) and tries to embed them optimally. If there is an elevator that responds to a call in the same direction and can receive that call on the way, it will be embedded in that elevator. Calls that cannot be embedded in any elevator in this way - will be embedded in a distributed and uniform manner for all elevators.

### results:

Building_file,B1.json, calls_a:
Total waiting time: 11292.0,  average waiting time per call: 112.92,  unCompleted calls,0,  certificate, -273590444

Building_file,B1.json, calls_b:
Total waiting time: 1784243.6402240375,  average waiting time per call: 1784.2436402240376,  unCompleted calls,963,  certificate, -4323896053

Building_file,B1.json, calls_c:
Total waiting time: 1839360.3121899734,  average waiting time per call: 1839.3603121899735,  unCompleted calls,958,  certificate, -4661569723

Building_file,B1.json, calls_d:
Total waiting time: 1841698.4976999543,  average waiting time per call: 1841.6984976999543,  unCompleted calls,950,  certificate, -4710424603

Building_file,B2.json, calls_a:
Total waiting time: 5057.0,  average waiting time per call: 50.57,  unCompleted calls,0,  certificate, -218740302

Building_file,B2.json, calls_b:
Total waiting time: 1783489.6402240375,  average waiting time per call: 1783.4896402240374,  unCompleted calls,963,  certificate, -4320973898

Building_file,B2.json, calls_c:
Total waiting time: 1837991.3121899734,  average waiting time per call: 1837.9913121899733,  unCompleted calls,958,  certificate, -4651502993

Building_file,B2.json, calls_d:
Total waiting time: 1840628.4976999543,  average waiting time per call: 1840.6284976999543,  unCompleted calls,950,  certificate, -4706939562

Building_file,B3.json, calls_a:
Total waiting time: 3173.0,  average waiting time per call: 31.73,  unCompleted calls,0,  certificate, -19044407

Building_file,B3.json, calls_b:
Total waiting time: 552136.0496319974,  average waiting time per call: 552.1360496319974,  unCompleted calls,159,  certificate, -1991782147

Building_file,B3.json, calls_c:
Total waiting time: 587571.8401950039,  average waiting time per call: 587.5718401950039,  unCompleted calls,99,  certificate, -2139571706

Building_file,B3.json, calls_d:
Total waiting time: 596859.5519140022,  average waiting time per call: 596.8595519140022,  unCompleted calls,79,  certificate, -2112214927

Building_file,B4.json, calls_a:
Total waiting time: 1763.0,  average waiting time per call: 17.63,  unCompleted calls,0,  certificate, -71094841

Building_file,B4.json, calls_b:
Total waiting time: 257758.01654399934,  average waiting time per call: 257.75801654399936,  unCompleted calls,53,  certificate, -866532504

Building_file,B4.json, calls_c:
Total waiting time: 268066.61219999986,  average waiting time per call: 268.06661219999984,  unCompleted calls,40,  certificate, -812356760

Building_file,B4.json, calls_d:
Total waiting time: 241012.87044399994,  average waiting time per call: 241.01287044399993,  unCompleted calls,34,  certificate, -920185323

Building_file,B5.json, calls_a:
Total waiting time: 1116.0,  average waiting time per call: 11.16,  unCompleted calls,0,  certificate, -83933611

Building_file,B5.json, calls_b:
Total waiting time: 40604.0,  average waiting time per call: 40.604,  unCompleted calls,0,  certificate, -259565060

Building_file,B5.json, calls_c:
Total waiting time: 41647.0,  average waiting time per call: 41.647,  unCompleted calls,0,  certificate, -255027313

Building_file,B5.json, calls_d:
Total waiting time: 41425.0,  average waiting time per call: 41.425,  unCompleted calls,0,  certificate, -255027313
