frog_height, pipes = map(int, input().split())
#se a diferenca de altura entre os canos for MAIOR que a altura de pulo so sapo ele perde
pipes_height = list(map(int, input().split()))
previous_pipe = pipes_height[0]
for i in range(1, len(pipes_height)): #importante adicionar o len para ler todos os valores da lista
#o 1 eh usado para comecar o loop a partir do segundo numero e assim poder fazer a diferenca com o primeiro settado no previous_pipe ([0])
    pipe_difference = abs(pipes_height[i] - previous_pipe) #abs aqui eh usado para manter a diferenca entre os canos sempre positiva
    if pipe_difference > frog_height:
        print('GAME OVER')
        break
    previous_pipe = pipes_height[i]
else:
    print('YOU WIN')






    