print([x for x in range(100, 401) if all([int(y) % 2 == 0 for y in str(x)])])
