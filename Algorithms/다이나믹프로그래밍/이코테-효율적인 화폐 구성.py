## n가지 종류의 화폐. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 m원이 되게 하려고 함. 
## m원을 만들기 위한 최소한의 화폐 개수를 출력

n, m = map(int, input().split())
d = [0] * 10001
money = list()

for i in range(n):
    money.append(int(input()))

for i in range(2, m - 1):
    