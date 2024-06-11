categoria1 = input().lower() 
categoria2 = input().lower() 
categoria3 = input().lower()
if categoria1 == 'vertebrado' and categoria2 == 'ave':
    if categoria3 == 'carnivoro':
        print('aguia')
    elif categoria3 == 'onivoro':
        print('pomba')

elif categoria1 == 'vertebrado' and categoria2 == 'mamifero':
    if categoria3 == 'onivoro':
        print('homem')
    elif categoria3 == 'herbivoro':
        print('vaca')

elif categoria1 == 'invertebrado' and categoria2 == 'inseto':
    if categoria3 == 'hematofago':
        print('pulga')
    elif categoria3 == 'herbivoro':
        print('lagarta')

elif categoria1 == 'invertebrado' and categoria2 == 'anelideo':
    if categoria3 == 'hematofago':
        print('sanguessuga')
    elif categoria3 == 'onivoro':
        print('minhoca')