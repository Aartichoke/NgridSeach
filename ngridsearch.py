import numpy
import sklearn
import csv
import random
import math
def main():
    # instantiate the 8 grid obj, 9 total slots
    initial = grid(9)
    print("goal")
    print(goal(9))

def goal(size):
    goal = []
    for i in range(1, size):
        goal.append(i)
    goal.append('b')
    return goal

# create a board
class grid:
    def __init__(self,size):
        new = []
        new.append("b")
        for i in range(1,size):
            new.append(i)
        #randomize the list
        random.shuffle(new)
        # check if input is perfect square
        if math.sqrt(size) % 1:
            print("ERROR: size %d is not a whole number"%size)
            exit(0)

        self.current = []
        # TBD: need to mod by sqrt(size)
        for x in range(int(math.sqrt(size))): # 1..3, 1..4, etc.
            self.current.append([])
            print("QQQ x %d"%x)
            print(new)
            for y in range(int(math.sqrt(size))):  # 1..3, 1..4, etc.
                self.current[x].append(new.pop())
        print(self.current)

'''
def best_first(grid): # returns a solution, or failure
    limit = 500
    return RBFS(problem,MAKE-NODE(problem.INITIAL-STATE),limit)

#recursize best first search
def RBFS(problem, node, f limit ) returns a solution, or failure and a new f-cost limit
if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
successors ←[ ]
for each action in problem.ACTIONS(node.STATE) do
add CHILD-NODE(problem, node, action) intosuccessors
if successors is empty then return failure,∞
for each s in successors do /* update f with value from previous search, if any */
s.f ←max(s.g + s.h, node.f ))
loop do
best ←the lowest f-value node in successors
if best .f > f limit then return failure, best .f
alternative ←the second-lowest f-value among successors
result , best .f ←RBFS(problem, best , min( f limit, alternative))
if result = failure then return result
'''

if __name__ == "__main__":
    main()