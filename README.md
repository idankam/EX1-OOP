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