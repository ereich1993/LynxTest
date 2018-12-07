import numpy as np
import pandas as pd



#data could be named numbers, and key could be named number
def _find(data, key):
    #no need for the counter"""
  counter = 0
  #i could be named number
  for i in data:
    if i == key:
        #this line should return i-1 instead
      return counter
    #this part to be deleted
    else:
      counter = counter+1
    #minus one is a good return value if the functuion cant find the value
  return -1



#the threshold was outside the function
#len(data)/2 is float have to change it to an int
#recursion has to have a base case allways
def find(data, key):
  threshold = 10
  half = int(len(data) / 2)
  #Make sure you correct the v name
  data_first = data[0:half]
  data_second = data[half:]
  #this line should return that data is to big and throw an exception
  #switch
  if len(data) <= threshold:
    return 1#find(data, key)
  elif key < data[half]:
    return find(data_first, key)
  else:
    return find(data_second, key)

def find_example(data,key):
    threshold = 10
    half = int(len(data) / 2)
    data_first = data[0:half]
    data_second = data[half:]

def depthfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for i in graph[vertex]:
                if i not in visited:
                    stack.append(i)
    return visited




def main():
    table = [[1, 5, 7, 10], [3, 13, 14, 15], [6, 16, 19, 25]]
    print(depthfs(table,table[0][0]))




if __name__ == "__main__":
    main()