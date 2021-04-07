import json


class World:
    # init method for constructor
    def __init__(self, filename):
        self.file = filename
        with open(filename, 'r') as filehandle:
            inputDict = json.load(filehandle)

        # initialize values and policy grid
        self.values = [[0] * inputDict["shape"][1]] * inputDict["shape"][0]
        self.policy = [['N'] * inputDict["shape"][1]] * inputDict["shape"][0]
        self.blocked_array = [['N'] * inputDict["shape"][1]] * inputDict["shape"][0]
        self.terminating_array = [['N'] * inputDict["shape"][1]] * inputDict["shape"][0]

        # initialize rewards grid
        rewards = inputDict["rl"]
        # make copy of values array
        # fill in rewards values
        self.rewards_array = self.values.copy()
        self.setRewards(rewards)

        # initialize blocked and terminating arrays
        self.blocked = inputDict["bl"]
        self.terminating = inputDict["tl"]

        # fill blocked and terminating tiles
        self.setBlocked(self.blocked)
        self.setTerminating(self.terminating)
        print(self.policy)
        print(self.terminating_array)
        print(self.blocked_array)

        # store gamma
        self.gamma = inputDict["gamma"]

        print(self.returnQ(0.8, 0, self.gamma, 0.8))
        print(self.getReward(1, 3))

        print(self.getValue(5, 3, "south"))

    def setRewards(self, rewards):
        for reward in rewards:
            row = reward[0][0]
            col = reward[0][1]
            self.rewards_array[row][col] = reward[1]

    def setBlocked(self, blockeds):
        if not blockeds:
            return
        for blocked in blockeds:
            row = blocked[0]
            col = blocked[1]
            self.policy[row][col] = '.'
            self.blocked_array[row][col] = '.'

    def setTerminating(self, blockeds):
        if not blockeds:
            return
        for blocked in blockeds:
            row = blocked[0]
            col = blocked[1]
            self.terminating_array[row][col] = '.'

    def returnQ(self, probability, reward, gamma, value):
        return probability * (reward + gamma * value)

    def getReward(self, row, col):
        return self.rewards_array[row][col]

    def getValue(self, row, col, direction):
        if direction == "north":
            if row - 1 < 0 or self.policy[row - 1][col] == '.':
                print("bounced off top wall")
                return self.values[row][col]
            else:
                return self.values[row - 1][col]
        if direction == "east":
            if col + 1 > len(self.values[0]) or self.policy[row][col + 1] == '.':
                print("bounced off right wall")

                return self.values[row][col]
            else:
                return self.values[row][col + 1]
        if direction == "south":
            if row + 1 > len(self.values):
                print("bounced off bottom wall")
                return self.values[row][col]
            if self.policy[row + 1][col] == '.':
                print("bounced off bottom wall")
                return self.values[row][col]
            else:
                return self.values[row + 1][col]
        if direction == "west":
            if col - 1 < 0 or self.policy[row][col - 1] == '.':
                print("bounced off left wall")

                return self.values[row][col]
            else:
                return self.values[row][col - 1]
