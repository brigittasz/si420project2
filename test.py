from world import *

if __name__ == "__main__":
    worldName = input('World file name: ')
    i = int(input('Number of iterations: '))
    w = World(worldName)
    w.valueIteration(i)
    printWorldValues(w)
    printWorldPolicy(w)
