lista_matr = []
lista_media_notas = []
dicionario = {}
media_geral = 0

for i in range(50):
	matricula = input('digite sua matricula: ')
	if matricula == '':
		break
	notas = list(map(int,input('digite suas 3 notas: ').split()))
	if notas == []:
		break
	lista_matr.append(matricula)
	lista_media_notas.append(int(sum(notas)/3))

dicionario = dict(zip(lista_matr,lista_media_notas))
print('\nMedia dos alunos {}'.format(dicionario))

resultado_final = list(filter(lambda media: media[1] > (sum(lista_media_notas)/len(lista_matr)), dicionario.items()))
print('\nResultado final dos alunos {}'.format(resultado_final))