t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))

    # find matched number
    cost_map = {}
    for i, cost in enumerate(a):
        sunny = cost
        johnny = m - cost
        if johnny in cost_map.keys():
            print(cost_map[johnny] + 1, i + 1)
        else:
            cost_map[cost] = i