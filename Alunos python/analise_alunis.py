import pandas as pd 
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

#Define o diretório de trabalho como a pasta onde está o script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Aluno:
    #Construtor da classe Aluno que recebe os atributos do csv
    def __init__(self, nome, curso, sexo, ano_ingresso):
        self.nome = nome
        self.curso = curso
        self.sexo = sexo
        self.ano_ingresso = ano_ingresso
    
    #Exibe os dados do csv
    def __str__(self):
        return f"{self.nome} | {self.curso} | {self.sexo} | {self.ano_ingresso}"

    #metodo estatico para ordenar a lista por nome e ano de ingresso
    @staticmethod
    def ordenar_nome_ano(alunos, criterio):
        if criterio == "nome":
            return sorted(alunos, key=lambda x: x.nome)
        elif criterio == "ano":
            return sorted(alunos, key=lambda x: x.ano_ingresso)
        
    # Busca um aluno pelo nome exato e retorna seus dados
    @staticmethod
    def buscar_nome(alunos, nome):
        for aluno in alunos:
            if aluno.nome.lower() == nome.lower():
                return aluno
        return None
    
    # Conta quantos alunos ingressaram em cada ano
    @staticmethod
    def alunos_por_ano(alunos):
        contagem = {}  # dicionário vazio
        for aluno in alunos:
            if aluno.ano_ingresso in contagem:
                contagem[aluno.ano_ingresso] += 1  # já existe, soma +1
            else:
                contagem[aluno.ano_ingresso] = 1   # primeiro aluno daquele ano
        return contagem

#Le o arquivo csv sem o header
df = pd.read_csv("Alunos.csv", header=None)

#Define os nomes das colunas manualmente
df.columns = ["Nome", "Curso", "Sexo", "Ano_Ingresso"]

#Cria uma lista de objetos Aluno a partir do DF
alunos = []

# '_' recebe o indice da linha e 'linha' recebe os dados da linha
for _, linha in df.iterrows():
    aluno = Aluno(linha["Nome"], linha["Curso"], linha["Sexo"], linha["Ano_Ingresso"])
    alunos.append(aluno)

#teste para exibir os 3 primeiros alunos
for a in alunos[:3]:
    print(a)

ordenados = Aluno.ordenar_nome_ano(alunos, criterio="ano")
print("=== Ordenado por Ano de Ingresso ===")
for a in ordenados:
    print(a)

ordenados = Aluno.ordenar_nome_ano(alunos, criterio="nome")
print("=== Ordenado por Nome ===")
for a in ordenados:
    print(a)

# Busca um aluno pelo nome
print("\n=== Busca por Nome ===")
resultado = Aluno.buscar_nome(alunos, "Ana Silva")
if resultado:
    print(f"Encontrado: {resultado}")
else:
    print("Aluno não encontrado.")

# Conta quantos alunos ingressaram em cada ano
print("\n=== Alunos por Ano de Ingresso ===")
contagem = Aluno.alunos_por_ano(alunos)
for ano, quantidade in contagem.items():
    print(f"Ano {ano}: {quantidade} alunos")