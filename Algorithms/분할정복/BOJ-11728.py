a, b = map(int, input().split())
c, d = [list(map(int, input().split())) for _ in range(2)]

befres = sorted(c + d)
befres = [str(befre) for befre in befres]
# for i in range(1, len(befres)):
#     if befres[i - 1] == befres[i]:
#         del befres[i - 1]
print(' '.join(befres))