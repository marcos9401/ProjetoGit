pessoa = list()
dadosp = dict()
mulheres = list()
aux = 0

while True:
  dadosp['nome'] = input('digite um nome: ')
  dadosp['idade'] = int(input('digite uma idade: '))
  while True:
    dadosp['sexo'] = input('digite "m" para masculino e "f" para feminino: ')
    if dadosp['sexo'].lower() == 'm' or dadosp['sexo'].lower() == 'f':
      break
    else:
      print('entrada invalida, digite "m" para masculino e "f" para feminio: ')
      continue
  pessoa.append(dadosp.copy())
  aux += dadosp['idade']
  if dadosp['sexo'].lower() == 'f':
    mulheres.append(dadosp['nome'])
  while True:
    opc = input('quer continuar(s/n): ')
    if opc.lower() == 's' or opc.lower() == 'n':
      break
    else:
      print('opçao invalida')
  if opc == 'n':
    break
media = aux/len(pessoa)

print(f'Total de pessoas cadastrada: {len(pessoa)}')
print(f'Media das idades: {media}')
print(f'Mulheres cadastradas: {mulheres}')
print('pessoas com idade acima da media: ')
for pmedia in pessoa:
  if pmedia['idade'] >= media:
    print(pmedia['nome'], pmedia['idade'],'anos') 