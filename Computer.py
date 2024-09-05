from Battlefield import Battlefield
from Agent.problem import Problem
import Agent.Algoritmi
import time


class Computer:

    def start(self, test):

        init_state_easy = ['_', '_', '_', 'H', 'M', 'C', 'H', '_', '_', '_']
        init_state_mediu = ['_', '_', 'C', 'H', 'M', 'C', 'H', '_', '_', '_']
        init_state_hard = ['C', 'H', 'M', 'H', 'M', 'C', 'H', 'M', 'M', 'M']
        #print(init_state_hard)
        Computer = Battlefield(init_state_easy)
        #Computer = Battlefield()
        Computer.regroup()
        #Computer.print()
        problem = Problem(Computer)
        alg = test

        if alg == "DFS":
            path = Agent.Algoritmi.depthFirstSearch(problem)
            print('DFS found a path of %d moves: %s' % (len(path), str(path)))
            print(problem.nodes)
            return path
        elif alg == "BFS":
            path = Agent.Algoritmi.breadthFirstSearch(problem)
            print('BFS found a path of %d moves: %s' % (len(path), str(path)))
            print(problem.nodes)
        elif alg == "RNDS":
            path = Agent.Algoritmi.rndSearch(problem)
            #print('RNDS found a path of %d moves: %s' % (len(path), str(path)))
        elif alg == "UCS":
            path = Agent.Algoritmi.uniformCostSearch(problem)
            print('UCS found a path of %d moves: %s' % (len(path), str(path)))
            print(problem.nodes)
        elif alg == "A*A":
            path = Agent.Algoritmi.aStarSearch(problem, Agent.Algoritmi.AproxAttackHeuristic)
            print('A* found a path of %d moves: %s' % (len(path), str(path)))
            print(problem.nodes)
        elif alg == "A*T":
            path = Agent.Algoritmi.aStarSearch(problem, Agent.Algoritmi.AproxTypeHeuristic)
            print('A* found a path of %d moves: %s' % (len(path), str(path)))
            print(problem.nodes)
        """curr = Computer
        i = 1
        for a in path:
            curr = curr.result(a)
            print('After %d move%s: %s' % (i, ("", "s")[i > 1], a))
            curr.print(), print(curr.nrAction, " ", curr.turn, " ", a)
            input("Press return for the next state...")  # wait for key stroke
            i += 1
        end_game = curr.endgame()
        print(curr.nrAction , " " , curr.turn)
        if end_game == 1:
            print("WIN!")
        else:
            print("LOSE!")"""


def main(test):
    Computer().start(test)

    return 0


if __name__ == "__main__":
    """start_time = time.clock()
    main("DFS")
    main("DFS")
    main("DFS")
    main("DFS")
    main("DFS")
    print((time.clock() - start_time)/5, "seconds")
    start_time = time.clock()
    main("BFS")
    main("BFS")
    main("BFS")
    main("BFS")
    main("BFS")
    print((time.clock() - start_time) / 5, "seconds")
    start_time = time.clock()
    main("UCS")
    main("UCS")
    main("UCS")
    main("UCS")
    main("UCS")
    print((time.clock() - start_time) / 5, "seconds")"""
    start_time = time.clock()
    main("A*A")
    main("A*A")
    main("A*A")
    main("A*A")
    main("A*A")
    print((time.clock() - start_time) / 5, "seconds")
    start_time = time.clock()
    main("A*T")
    main("A*T")
    main("A*T")
    main("A*T")
    main("A*T")
    print((time.clock() - start_time) / 5, "seconds")
