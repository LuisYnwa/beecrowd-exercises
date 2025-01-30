#LIFE IS NOT A PROBLEM TO BE SOLVED BUT A REALITY TO BE EXPERIENCED
user_letters = int(input())
phrase = 'LIFE IS NOT A PROBLEM TO BE SOLVED BUT A REALITY TO BE EXPERIENCED'
final_phrase = []
#phrase.split()
for c in range(user_letters):
    final_phrase.append(phrase[c])

print(''.join(final_phrase)) #join usado para tirar as ' ' da lista final
