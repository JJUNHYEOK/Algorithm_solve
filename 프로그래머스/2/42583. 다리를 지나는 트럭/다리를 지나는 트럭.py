from collections import deque

def solution(bridge_length, weight, truck_weights):

    time = 0
    bridge = deque()
    trucks = deque(truck_weights)
    cur_weight = 0

    while bridge or trucks:
        time += 1

        if bridge and bridge[0][1] == time:
            truck_w, x = bridge.popleft()
            cur_weight -= truck_w

        if trucks and cur_weight + trucks[0] <= weight:
            truck_w = trucks.popleft()
            bridge.append((truck_w, time + bridge_length))
            cur_weight += truck_w

    return time