<div align="justify">

  
# Algorithm Evaluation
A distribution and logistics company has a fleet made up of N trucks. Weekly,
this company organizes its deliveries into M routes, which must be distributed among trucks
available. The company wants to distribute in such a way that each truck fulfills the same
mileage, thus avoiding that at the end of the period there are idle trucks while others
are still running multiple routes. If it is not possible to complete the same mileage as the
difference between the trucks' mileage is as small as possible, reducing the problem.

For example, suppose there are 3 trucks and 10 routes with the following mileages: 35, 34,
33, 23, 21, 32, 35, 19, 26, 42. Among the distributions D1 and D2 below, D1 would be considered better.


### D1

Truck 1: routes 21, 32, 42 – total 95km

Truck 2: routes 35, 34, 26 – total 95km

Truck 3: routes 23, 19, 35, 33 – total 110km


### D2

Truck 1: routes 35, 33, 32, 42 – total 142km

Truck 2: routes 35, 19, 26 – total 80km

Truck 3: routes 23, 34, 21 – total 78kms

Along with this statement, a ‘problem generator’ is being provided, which returns a set of routes generated from a fixed random seed. Taking that into account, the tasks are:

### a) Design and implement a solution to the problem presented using backtracking. A solution must include a pruning strategy for unpromising solutions.

a1) Using the ‘problem generator’ code provided, measure the execution time of sets of increasing size, until reaching a size T that cannot be resolved within 30 seconds per algorithm. This test must be performed for 3 trucks and starting with 6 routes. In pursuit of the 30 second time limit, test with 10 sets of each size, counting the average of executions.

### b) Design and implement solutions to the problem presented using a greedy algorithm. Must be used at least two different greedy strategies in implementation.

b1) For this test, use the same sets of size T used in backtracking. In then increase the set sizes from T to T until reaching size 10T, always running 10 tests of each size to use the average.

### c) Design and implement a solution to the problem presented using divide and conquer. 

c1) In this case, use the same sets of size T used in backtracking.

</div>

### d) Design and implement a solution to the problem presented using programming dynamics. 

d1) Here, use the same test sets as the greedy algorithm.
