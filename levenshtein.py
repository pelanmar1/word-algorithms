# Pedro Lanzagorta

def printMatrix(mat):
    for i in range(len(mat)):
        ln = ""
        for j in range(len(mat[0])):
            ln += str(mat[i][j]) +' '
        print ln + '\n'

def levenshteinDistance(wrd1,wrd2):
    # Setup matrix
    n = len(wrd1)
    m = len(wrd2)
    mat = [[]]
    mat = [[i for i in xrange(m+1)] for i in xrange(n+1)]
    for i in xrange(n+1):
        for j in xrange(m+1):
            if i == 0:
                mat[i][j] = j
            elif j == 0:
                mat[i][j] = i
            else:
                mat[i][j] = 0
    
    
    
    # Calculate costs

    for i in range(1,n+1):
        for j in range(1,m+1):
            c = 1
            if wrd1[i-1] == wrd2[j-1]:
                c = 0
            m1 = mat[i-1][j]+1
            m2 = mat[i][j-1]+1
            m3 = mat[i-1][j-1]+c
            mat[i][j] = min(m1,m2,m3)
    
    return mat[n][m]
    

def levenshteinDistanceOptimized(wrd1,wrd2):
    # Setup matrix
    n = len(wrd1)
    m = len(wrd2)
    mat = [[]]
    mat = [[i for i in xrange(n+1)] ,[1]+[ 0 for i in xrange(n)]]

    for i in range(1,m+1):
        for j in range(1,n+1):
            c = 1
            if wrd1[j-1] == wrd2[i-1]:
                c = 0
            m1 = mat[1][j-1]+1
            m2 = mat[0][j]+1
            m3 = mat[0][j-1]+c
            mat[1][j] = min(m1,m2,m3)
            if (j > 1 and i < m):
                mat[0][(j-1)] = mat[1][(j-1)]
            if (j == n and i < m):
                mat[0][n] = mat[1][n]
        mat[0][0] += 1
        mat[1][0] += 1
    return mat[1][n]

    

print levenshteinDistanceOptimized('GAMBOL','GUMBO')
    

