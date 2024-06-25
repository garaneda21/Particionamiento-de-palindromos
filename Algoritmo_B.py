def generarPalindromo(string):
    n = len(string)

    P = [[False for i in range(n)] for i in range(n)]

    # Inicializar la matriz de palíndromos para un caracter
    for i in range(n):
        P[i][i] = True

    for L in range(2, n+1):

        for i in range(n-L+1):
            j = i + L - 1

            if string[i] == string[j] and (P[i+1][j-1] or L == 2):
                P[i][j] = True

    return P

def minCutDP(string):
    n = len(string)

    P = generarPalindromo(string)
    minCortesDP = [float('inf')] * n

    minCortesDP[0] = 0

    for i in range(1, n):
        if P[0][i]:
            minCortesDP[i] = 0
        else:
            for j in range(i, 0, -1):
                if P[j][i]:
                    if minCortesDP[j-1] + 1 < minCortesDP[i]:
                        minCortesDP[i] = minCortesDP[j-1] + 1

    return minCortesDP[n-1]

print(minCutDP('geek'))