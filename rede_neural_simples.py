#################################
# EXEMPLO DE REDE NEURAL SIMPLES
#################################
print("Rede Neural de Gestao de Aprovados \n")

# Entrada de dados
# Essas informações representam os inputs que chegam aos neurônios
nota = float(input ("Informe a nota do aluno: \n"))
frequencia = float(input("Informe a frequência do aluno (%): \n"))

# Pesos das entradas
# Quanto maior o peso, maior a influência dessa variável na decisão final
peso_nota = 0.7
peso_frequencia = 0.3

print(f"Nota {nota} , Peso nota: {peso_nota}")
print(f"Frequencia {frequencia} Peso Frequência: {peso_frequencia}")

# Soma Ponderada
# Multiplica cada entrada pelo seu peso e soma os resultados

resultado = (
    nota * peso_nota + frequencia * peso_frequencia
)

print(f"Resultado calculado: {resultado}")

# Função de ativação
# O que decidirá a saída do modelo

if resultado >= 60:
    print("Aprovado")
else: 
    print("Reprovado")    

