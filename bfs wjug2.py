import math
from collections import deque
'''input capacities and initial/final states for jugs'''
a = int(input("enter jug A capacity: "))
b = int(input("enter jug B capacity: "))
ai = int(input("initially water in jug A: "))
bi = int(input("initially water in jug B: "))
af = int(input("final state of jug A: "))
bf = int(input("final state of jug B: "))
if a<=0 or b <= 0:
    print("jug capacities must be positive.")
    exit(1)
if ai < 0 or bi < 0 or af < 0 or bf < 0:
    print("negative values are not allowed.")
    exit(1)
if ai==af and bi==bf:
    print(f"initial state is already the final state: juga{ai} and jugb={bi}")
    exit()
def bfs_wjug(a,b,ai,bi,af,bf):
    visited = set()
    queue =deque([(ai,bi,[])])
    while queue:
        curr_ai,curr_bi,operations = queue.popleft()
        if(curr_ai,curr_bi) in visited:
            continue
        visited.add((curr_ai,curr_bi))
        if curr_ai == af and curr_bi == bf:
            for i,op in enumerate(operations):
                print(f"step{i+1}:{op}")
            print(f"final state reached: jug A = {curr_ai},jug B = {curr_bi}")
            return
        possible_operations = [
            (a,curr_bi,"fill jug A"),
            (curr_ai, b,"fill jug B"),
            (0, curr_bi,"empty jug A"),
            (curr_ai, 0,"empty jug B"),
            (curr_ai - min(curr_ai,b - curr_bi),curr_bi + min(curr_ai, b- curr_bi),"pour from A to B"),
            (curr_ai + min(curr_bi, a - curr_ai),curr_bi - min(curr_bi, a - curr_ai),"pour from B to A"),
        ]
        for next_ai,next_bi,op in possible_operations:
            if (next_ai,next_bi) not in visited:
                queue.append((next_ai, next_bi, operations + [op]))
    print("no solution found.")
    return
gcd = math.gcd(a,b)
if (af <= a and bf <= b) and (af % gcd == bf % gcd == 0):
    bfs_wjug(a,b,ai,bi,af,bf)
else:
    print("the final state is not achievable with the given capacities.")
    exit()
    




                
