# Problem: Design and analyze a greedy solution to give a schedule of n print jobs of lengths l1,…,ln that minimizes the total waiting time, when two identical printers are available (each can print one job at a time). Prove that your algorithm is optimal.
# Source: SCU COEN279 DAA HW5 Q1
# Author: Shreyas Padhye
# Algorithm: Greedy Strategy

class solution:
    def greedy_schedule_2(self, A):
        A.sort()
        # pre: A[start:stop:step] - used for list slicing. Start at 'start', go till 'stop' with step size = 'step'
        # keep all elements at even positions of the list in `schedule_1`
        schedule_1 = A[0::2]

        # keep all elements at odd positions of the list in `schedule_2`
        schedule_2 = A[1::2]

        # compute wait lists for both schedules
        wait_list_1 = []
        wait_list_2 = []
        wait = 0
        for i in range(1, len(schedule_1)):
            wait += schedule_1[i-1]
            wait_list_1.append(wait)

        wait = 0
        for i in range(1, len(schedule_2)):
            wait += schedule_2[i-1]
            wait_list_2.append(wait)

        # TODO: figure out if the sum can be done in the loop itself
        # TODO: see if you can improvr the code by adding map or other list methods / manipulations
        return sum(wait_list_1) + sum(wait_list_2)

sol = solution()
sol.greedy_schedule_2([6, 8, 10, 14, 1, 7, 11, 12])


