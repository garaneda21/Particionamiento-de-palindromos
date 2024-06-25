def palPart(string):
    # largo del string
    n = len(string)

    # C: Matriz con cortes nesesarios para el string[i,j]
    # P : si el string[i,j] es palindromo True
    C = [[0 for i in range(n)] for i in range(n)]
    P = [[False for i in range(n)] for i in range(n)]

    # como el algoritmo usa el método bottom up,
    # inicializa las matrices donde i=j (donde los strings son solo un caracter)
    # como palíndromos
    for i in range(n):
        C[i][i] = 0
        P[i][i] = True

    # L: largo del substring
    # se irán recorriendo todos los substrings 
    # desde los de largo 2 hasta n
    for L in range(1, n):
        for i in range(0, n - L):
            j = i + L

            # Sí el string es un palíndromo
            #   (o estamos en L == 1, substring de largo 2)
            #   no nesesita cortes, marcar el substring como palíndromo
            # Sino, nesesita un corte y compara entre
            #   el mínimo número de cortes del cada substring anterior
            #   de la misma forma que el algoritmo de multiplicación de matrices
            if string[i] == string[j] and (P[i+1][j-1] or L == 1):
                C[i][j] = 0
                P[i][j] = True
            else:
                C[i][j] = float("inf")
                for k in range(i, j):
                    C[i][j] = min(C[i][j], 1 + C[i][k] + C[k+1][j])

    return C[0][n-1]

print(palPart('geek'))