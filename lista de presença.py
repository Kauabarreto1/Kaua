alunos_presentes = []

print("Digite o nome dos alunos presentes (Digite 'fim' quando terminar):")
while True:
    aluno = input("Nome do aluno (ou 'fim' para terminar): ")
#Quando não tiver mais alunos escrever "fim" para encerrar o programa
    if aluno.lower() == 'fim':
        break
    else:
        alunos_presentes.append(aluno)

print("\nAlunos presentes:")
for aluno in alunos_presentes:
    print(aluno)
