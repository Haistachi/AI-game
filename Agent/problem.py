import copy
from Battlefield import Battlefield


class Problem(Battlefield):

    def __init__(self, battlefield):
        self.battlefield = battlefield
        nods = 0

    def getStartState(self):
        return self.battlefield

    def isGoalState(self, given_battlefield):
        if given_battlefield.endgame() == 1:
            return True
        else:
            return False

    def expand(self, given_battlefield):
        children = []
        for action in self.getActions(given_battlefield):
            nextState = self.getNextState(given_battlefield, action)
            cost = self.getActionCost(given_battlefield, action, nextState)
            children.append((nextState, action, cost))
        return children

    def getActions(self, given_battlefield):
        possible_action = [(-1, 0), (0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
        valid_actions = []
        for action in possible_action:
            x, y = action
            if not self.is_invalid(x, y, given_battlefield):
                valid_actions.append(action)
        return valid_actions

    def is_invalid(self, pos1, pos2, battlefield):
        if battlefield.turn > 10:
            return True
        if battlefield.endgame() > 0:
            return True
        if battlefield.prev_ac == (pos1, pos2) and ((pos1, pos2) != (4, 5) or battlefield.team1_unit_lost):
            return True
        if pos1 == -1:
            return False
        if pos1 > 9 or pos2 > 9 or pos1 == pos2:
            return True
        elif (battlefield.battlefield[pos1] is None) or (battlefield.battlefield[pos2] is None):
            return True
        elif battlefield.battlefield[pos1].action_points == 0 or battlefield.battlefield[pos2].action_points == 0:
            return True
        elif pos1 > 4:
            return True
        else:
            return False

    def getNextState(self, state, action):
        assert action in self.getActions(state), (
            "Invalid action passed to getActionCost().")
        x, y = action
        nextState = copy.deepcopy(state)
        nextState.action(x, y)
        return nextState

    def getActionCost(self, state, action, next_state):
        assert next_state == self.getNextState(state, action), (
            "Invalid next state passed to getActionCost().")
        score = 6
        if action == (4, 5):
            if state.team2_unit_lost:
                score = -40
            else:
                score = 1
        if action == (-1, 0):
            score = 30
        return score

    def getCostOfActionSequence(self, actions):
        total_cost = 0
        # state = self.start_state
        state = self.battlefield
        for a in actions:
            # children = self.children[state]
            children = self.expand(state)
            match = False
            for (next_state, action, cost) in children:
                if a == action:
                    state = next_state
                    total_cost += cost
                    match = True
            if not match:
                raise Exception("Invalid action sequence")
        return total_cost
