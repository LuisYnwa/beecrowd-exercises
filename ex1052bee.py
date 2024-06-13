usuario = int(input())
datas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August' , 'September', 'October', 'November', 'December']
qual_mes = dict(zip(datas, meses))
mes_resposta = qual_mes[usuario]
print(mes_resposta)