def create_patterns():
    R = [[" " for _ in range(5)] for _ in range(6)]
    D = [[" " for _ in range(5)] for _ in range(6)]
    X = [[" " for _ in range(5)] for _ in range(5)]
    
    # Create pattern for R
    for i in range(6):
        for j in range(5):
            if j == 0 or (j == 4 and (i == 1 or i == 2)) or (i == 0 or i == 3):
                R[i][j] = '*'
            elif i == 4 and j == 3:
                R[i][j] = '*'
            elif i == 5 and j == 4:
                R[i][j] = '*'

    # Create pattern for D
    for i in range(6):
        for j in range(5):
            if j == 0 or (j == 4 and (i != 0 and i != 5)) or (i == 0 or i == 5):
                D[i][j] = '*'

    # Create pattern for X
    for i in range(5):
        for j in range(5):
            if i == j or i + j == 4:
                X[i][j] = '*'

    return R, D, X

def combine_patterns(patterns):
    max_height = max(len(p) for p in patterns)
    combined = [""] * max_height

    for i in range(max_height):
        for pattern in patterns:
            if i < len(pattern):
                combined[i] += "".join(pattern[i]) + "  "
            else:
                combined[i] += " " * len(pattern[0]) + "  "

    return combined

def print_pattern():
    R, D, X = create_patterns()

    combined = combine_patterns([R, D, X])

    for line in combined:
        print(line)

print_pattern()
