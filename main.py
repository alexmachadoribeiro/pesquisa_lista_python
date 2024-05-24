# lista de 15 nomes
nomes = ['Alex', 'Eduardo', 'Maria', 'Mariana', 'João', 'José', 'Joana', 'Fernanda', 'Fulano', 'Cicrano', 'Beltrano', 'Connor','Corona' ,'Cecília' ,'Alexandre']

# usuário informa o nome que deseja pesquisar
nome = input('Digite o nome a ser pesquisado: ').capitalize()

# verifica se o nome está na lista ou não
try:
    # retorna o índice do nome pesquisado
    indice = nomes.index(nome)
    print(f'Nome encontrado: {nome} no índice {indice}.')
except:
    print(f'{nome} não encontrado na lista.')