price1, price2 = map(float, input().split())
final_percentage = ((price1 - price2) / price1) * 100
print(f'{abs(final_percentage):.2f}%')