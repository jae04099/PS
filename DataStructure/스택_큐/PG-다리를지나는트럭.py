bridge_length = 2
weight= 10
truck_weights = [7, 4, 5, 6]
bridge_on = [0] * (len(truck_weights) + 1)
curr_weight = 0
answer = 0


##다리 길이, 트럭은 1초에 1만큼 움직임, 무게 weight까지 견딤, 트럭이 다리에 완전히 오르지 않은 경우, 트럭의 무게는 고려하지 않음
import collections

while truck_weights:
    answer += 1
    bridge_out = bridge_on.pop(0)
    curr_weight -= bridge_out
    


