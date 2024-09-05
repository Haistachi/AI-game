import random
import Agent.util


class Nod:
    def __init__(self, nume, cost):
        self.nume = nume
        self.cost = cost

    def getNume(self):
        return self.nume

    def getCost(self):
        return self.cost


def depthFirstSearch(problem):
    nodCrt = (problem.getStartState(), [])
    problem.nodes = 1
    frontiera = Agent.util.Stack()
    frontiera.push(nodCrt)
    teritoriu = []
    while not frontiera.isEmpty():
        nodCrt = frontiera.pop()
        teritoriu.append(nodCrt[0])
        if problem.isGoalState(nodCrt[0]):
            return nodCrt[1]
        succesori = problem.expand(nodCrt[0])

        for succesor in succesori:
            problem.nodes += 1
            (stare, actiune, _) = succesor
            #stare.print(), print(stare.nrAction, " ", stare.turn, " ", actiune)
            if stare not in teritoriu and stare not in functie(frontiera.list):
                cale = nodCrt[1] + [actiune]
                frontiera.push((stare, cale))
    return []


def breadthFirstSearch(problem):
    nod_crt = (problem.getStartState(), [])
    problem.nodes = 1
    frontiera = Agent.util.Queue()
    frontiera.push(nod_crt)
    teritoriu = []
    while not frontiera.isEmpty():
        nod_crt = frontiera.pop()
        teritoriu.append(nod_crt[0])
        if problem.isGoalState(nod_crt[0]):
            return nod_crt[1]
        succesori = problem.expand(nod_crt[0])

        for succesor in succesori:
            problem.nodes += 1
            (stare, actiune, _) = succesor
            # stare.print(), print(stare.nrAction, " ", stare.turn, " ", actiune)
            if stare not in teritoriu and stare not in functie(frontiera.list):
                cale = nod_crt[1] + [actiune]
                frontiera.push((stare, cale))
    return []
    util.raiseNotDefined()


def rndSearch(problem):
    crt = problem.getStartState()
    solutie = []
    while not (problem.isGoalState(crt)):
        succesori = problem.expand(crt)
        nrSucc = len(succesori)
        i = int(random.random() * nrSucc)
        if nrSucc > 0:
            succesor = succesori[i]
        crt = succesor[0]
        solutie.append(succesor[1])
    #print("solutie: ", solutie)
    return solutie


def uniformCostSearch(problem):
    frontiera = Agent.util.PriorityQueue()
    teritoriu = []
    nod_crt = (problem.getStartState(), [])
    problem.nodes = 1
    frontiera.push(nod_crt, 0)
    while not frontiera.isEmpty():
        nod_crt = frontiera.pop()
        if problem.isGoalState(nod_crt[0]):
            return nod_crt[1]
        teritoriu.append(nod_crt[0])
        succesori = problem.expand(nod_crt[0])
        # print(succesori)
        # print(teritoriu)
        for succesor in succesori:
            problem.nodes += 1
            (stare, mutare, cost) = succesor
            if stare not in teritoriu:
                cale = nod_crt[1] + [mutare]
                # stare.print(), print(stare.nrAction, " ", stare.turn, " ", mutare)
                g = problem.getCostOfActionSequence(cale)
                # print(g)
                frontiera.update((stare, cale), g)
    return []


def nullHeuristic(state, problem=None):
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    frontiera = Agent.util.PriorityQueue()
    teritoriu = []
    nod_crt = (problem.getStartState(), [])
    problem.nodes = 1
    g = 0
    h = heuristic(problem.getStartState(), problem)
    f = g + h
    frontiera.push(nod_crt, f)
    while not frontiera.isEmpty():
        nod_crt = frontiera.pop()
        if problem.isGoalState(nod_crt[0]):
            return nod_crt[1]
        teritoriu.append(nod_crt[0])
        succesori = problem.expand(nod_crt[0])
        for (stare, mutare, cost) in succesori:
            problem.nodes += 1
            if stare not in teritoriu:
                cale = nod_crt[1] + [mutare]
                g = problem.getCostOfActionSequence(cale)
                h = heuristic(stare, problem)
                f = g + h
                frontiera.update((stare, cale), f)
    return []


def functie(lista):
    a = []
    for x in lista:
        a.append(x[0])
    return a


def AproxAttackHeuristic(state, problem):  # O heuristica care imi ofera o aproximare bazata pe numarul de unitati
    dmg = 0
    for i in range(5, 10, 1):
        if state.battlefield[i] is not None:
            dmg += 1
    return dmg * 3 + dmg * 30  # avreage attack + turn


def AproxTypeHeuristic(state, problem):  # O heuristica care imi ofera o aproximare bazata pe tipul de unitati
    u = []
    score = 0
    for i in range(0, 5, 1):
        if state.battlefield[i] is not None:
            if state.battlefield[i].name == "Cav":
                u.append("Cav")
            elif state.battlefield[i].name == "Halb":
                u.append("Halb")
            elif state.battlefield[i].name == "Musket":
                u.append("Musket")
    for i in range(5, 10, 1):
        if state.battlefield[i] is not None:
            if state.battlefield[i].name in u:
                score += 2
            else:
                score += 3 + 30
    return score
