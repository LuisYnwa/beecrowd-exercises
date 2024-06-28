number = int(input())
mourinho = [] 

for i in range(1000):
    count = 0

    while count < number:
        mourinho.append(count)
        count = count + 1
        
    print(f'N[{i}] = {mourinho[i]}')



#INCOMPLETO -- INDICE REPETINDO x number VEZES
#mourinho = []
#number = int(input())
#p = 0
#for i in range(10):
    
    #for p in range(number):
        #mourinho.append(p)
    #print(f'N[{i}] = {p}')

    #if max(mourinho) >= number:
        #mourinho.clear()
