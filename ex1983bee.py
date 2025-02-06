test_cases = int(input())
registry_numbers = []
notes = []

for i in range(test_cases):
    registry, note = input().split()
    registry = int(registry) # mudança pra float com o objetivo de contornar o erro invalid literal for int()
    note = float(note)  
    registry_numbers.append(registry)
    notes.append(note)

average = sum(notes) / test_cases
if max(notes) < 8:  # Verificação da maior nota
    print('Minimum note not reached')
else:
    max_index = notes.index(max(notes))
    print(registry_numbers[max_index]) #pega o numero da mesma posicao no registry_numbers
