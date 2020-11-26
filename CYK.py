Rules = dict()
Rules["S"] = ["AT", "AU", "0"]
Rules["T"] = ["UB", "b"]
Rules["U"] = ["AT", "UT"]
Rules["A"] = ["a"]
Rules["B"] = ["b"]

word = "aaabbb" #I want the letters indexed from 1

######### program #########

n = len(word)
word = " " + word

T = [[set() for j in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    for lhs in Rules:
        if word[i] in Rules[lhs]:
            T[i-1][i].add(lhs)

for l in range(2, n+1):
    for i in range(0, n-l+1):
        j = i+l
        for lhs in Rules:
            for rhs in Rules[lhs]:
                if len(rhs) == 2: # rule A->BC
                    A, B, C = lhs, rhs[0], rhs[1]
                    for k in range(i+1, j):
                        if (B in T[i][k]) and (C in T[k][j]):
                            T[i][j].add(A)

for row in T:
    for s in row:
        print("ø" if len(s)==0 else s, end=' ')
    print()
