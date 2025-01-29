def count_walks(n):
    dp = [[[0] * (n + 1) for _ in range(25)] for _ in range(25)]
    dp[12][12][0] = 1 #[x] [y] sao usadas para armazenar o numero de caminho ate o destino e o terceiro [] eh a quantidade de passos
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)] #as seis coordenadas possiveis de um favo de mel
    
    for steps in range(1, n + 1):
        for x in range(25):
            for y in range(25):
                dp[x][y][steps] = 0
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 25 and 0 <= ny < 25: #verificacao se ambos estao nos limites 25x25 da matriz
                        dp[x][y][steps] += dp[nx][ny][steps - 1]
    
    return dp[12][12][n]

t = int(input())
for _ in range(t):
    n = int(input())
    print(count_walks(n))
