############################################################
# EXEMPLO DE REDE NEURAL GESTAO DE APROVADOS - SCIKIT LEARN
############################################################

# Importa Biblioteca necessárias 

from sklearn.neural_network import MLPClassifier

# Dados de Treinamento

# Variavel X: Cada linha representa um aluno
# Primeira coluna: 
# Nota Alta? 
#   0 = Não
#   1 = Sim

# Segunda Coluna:
# Frequência alta?
#   0 = Não
#   1 = Sim

x = [
    # Aluno 1
    # Nota baixa e frequência baixa
    [0,0], 

    # Aluno 2
    # Nota baixa e frequência alta
    [0,1],

    # Aluno 3
    # Nota alta e frequência baixa
    [1,0],

    # Aluno 4
    # Nota alta e frequência baixa
    [1,1],

]

# Resultados Esperados
# y Representa a resposta esperada (correta de cada aluno)
# 0 = Reprovado
# 1 = Aprovado

y = [
    # Aluno 1
    0,

    # Aluno 2
    0,

    # Aluno 3
    0,

    # Aluno 4
    1,

]

rede = MLPClassifier(
    # Quantidade de neuronios na camada oculta (3 neuronios)
    hidden_layer_sizes=(3,),

    # Numero maximo de tentativas de aprendizagem
    # Quanto maior o numero, mais o modelo tende a ajustar os pe
    max_iter=5000,

    # Garante que o resultado seja reproduzivel
    random_state=42
)

# TREINAMENTO DO MODELO

# A rede vai analisar todos os exemplos passados



# Treina o modelo
rede.fit(x,y)

print("Rede Treinada")

# TESTES DO MODELO NOS DADOS PREVISTOS

print("Testando alunos")
for aluno in x:
    previsao = rede.predict([aluno])

    # Exibe o resultado encontrado
    print(f"Aluno {aluno} -> Resultado {previsao[0]}")