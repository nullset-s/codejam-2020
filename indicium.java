def compute(matrix):
    hashmap = dict()
    for i in range(len(matrix)):
        g = matrix[i]
        if (g[0], g[1]) not in hashmap:
            hashmap[(g[0], g[1])] = []
        hashmap[(g[0], g[1])].append(i)
        if len(hashmap[(g[0], g[1])]) > 2:
            return "IMPOSSIBLE"

    sch = sorted(matrix)
    j = c = -99999
    final_op = [None] * len(sch)

    for i in range(len(sch)):
        activity = sch[i]
        if j <= activity[0]:
            if not final_op[hashmap[(activity[0], activity[1])][0]]:
                final_op[hashmap[(activity[0], activity[1])][0]] = "C"
            else:
                final_op[hashmap[(activity[0], activity[1])][1]] = "C"
            j = activity[1]

        elif c <= activity[0]:
            if not final_op[hashmap[(activity[0], activity[1])][0]]:
                final_op[hashmap[(activity[0], activity[1])][0]] = "J"
            else:
                final_op[hashmap[(activity[0], activity[1])][1]] = "J"
            c = activity[1]

        elif j > activity[0] and c > activity[0]:  #
            return "IMPOSSIBLE"

    return ''.join(final_op)


T = int(input())
for i in range(1, T + 1):
    N = int(input())
    mat = []
    for j in range(N):
        mat.append(input().split(" "))

    for row in range(len(mat)):
        for col in range(len(mat[0])):
            mat[row][col] = int(mat[row][col])


    print("Case #{}: {}".format(i, compute(mat)))