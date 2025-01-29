elves_hired = int(input())
#dolls = 8 hours (30 horas disponiveis = 3 presentes)
#architects = 4 hours (15 horas disponiveis = 3 presentes)
#musicians = 6 hours (20 horas disponiveis = 3 presente)
#drawners = 12 hours (15 horas disponiveis = 1 presente)
#limitador para 24 horas trabalhadas
dolls = 0
architects = 0
musicians = 0
drawners = 0

for i in range(elves_hired):
    nome, funcao, horas = input().split()
    horas = int(horas)
    if funcao == 'bonecos':
        dolls += horas
    elif funcao == 'arquitetos':
        architects += horas
    elif funcao == 'musicos':
        musicians += horas
    elif funcao == 'desenhistas':
        drawners += horas

# Calcular a quantidade de presentes produzidos por grupo
dolls_estimate = dolls // 8
architects_estimate = architects // 4
musicians_estimate = musicians // 6
drawners_estimate = drawners // 12

# Soma total de presentes
print(dolls_estimate + architects_estimate + musicians_estimate + drawners_estimate)

