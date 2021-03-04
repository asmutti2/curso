pessoa = {'nome': 'Ângelo', 'Idade': 38, 'cursos': ['Inglês', 'Python']}
pessoa["idade"] = 44
pessoa['cursos'].append(' Algebra')
print(pessoa['idade'])
print(pessoa['cursos'])
pessoa.pop('idade') #removerá o item do dicionário
print(pessoa)
pessoa.update({'Idade' : 40, 'Sexo' :  'M'})
print(pessoa)
del pessoa['cursos'] #remoção do item
print(pessoa)
