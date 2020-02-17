'''
Title:           State Space Generation
Files:           p1_statespace.py
Course:          CS540, Spring 2020

Author:          Yeochan Youn
Email:           yyoun5@wisc.edu
'''
max = [5,7] # max capacity of each jug
s0 = [0,0] # initial state of jugs which are empty

'''
fill max capacity of jug
input:
    - state: current state
    - max: maximum capcacity of target jug
    - which: jug to fill
return: state after fill
'''
def fill(state, max, which):
    ls = state[:]
    ls[which] = max[which]
    return ls
'''
empty the target jug
input:
    - state: current state
    - max: maximum capacity of jug
    - which: jug to empty
return: state after empty
'''
def empty(state, max, which):
    ls = state[:]
    ls[which] = 0
    return ls

'''
transfer water from source jug to dest jug until source is empty or dest is full
input:
    - state: current state
    - max: max capacity of jug
    - source: jug to empty
    - dest: jug to fill
return: state after move water
'''
def xfer(state, max, source, dest):
    ls = state[:]
    capDest = max[dest] - state[dest] # space left in dest jug
    if capDest >= ls[source]: # if capdest is equal or greater than water in source jug 
        ls[dest] = ls[dest] + ls[source] # pour whole water into dest jug
        ls[source] = 0 # empty source jug
    else: # if dest jug doesnt have enough space
        ls[source] = ls[source] - capDest # pour as much as dest jug can handle
        ls[dest] = max[dest] # dest jug is full
    return ls # return state

'''
display successor states of the current state
input:
    - state: current state
    - max: max capacity of jug
'''
def succ(state, max):
    ls = []
    succ = xfer(state, max, 0, 1)
    if succ not in ls: # filter for duplicate state
        ls.append(succ)
    succ = xfer(state, max, 1, 1)
    if succ not in ls:
        ls.append(succ)
    succ = fill(state, max, 0)
    if succ not in ls:
        ls.append(succ)
    succ = fill(state, max, 1)
    if succ not in ls:
        ls.append(succ)
    for i in ls:
        print(i) # print all the states
    
