number = int(input())
cont = 0
pum1 = 1
pum2 = 3
pum = []
while cont < number:
    for i in range(pum1, pum2+1):
        pum.append(i)
    print(f'{" ".join(map(str, pum))} PUM') #use " ".join(map(str, pum)) para retirar os [] e as virgulas do codigo
    
    #" ".join(map(str, pum)) o map(str, pum) converte os vvalores dentro da lista para string enquanto o join substitui os [] e os separa com espaco 
    pum.clear()
    cont += 1
    pum1 += 4
    pum2 += 4