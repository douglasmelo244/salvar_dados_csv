import csv
import os
arquivo_csv = 'estudantes.csv'

class SistemaEstudantes:
    def __init__(self):
        self.estudantes=[]
        self.carregarDados()

    def carregarDados(self):
        try:
            with open(arquivo_csv, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.estudantes = list(reader)
              
        except FileNotFoundError:
            print('Arquivo csv não encontrado')
        except csv.Error:
            print('Erro ao ler o arquivo csv')

    def salvar_dados(self):
        with open(arquivo_csv, mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ['Nome', 'Idade', 'Nota_Matematica', 'Nota_Ciencias', 'Nota_Ingles']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  
            writer.writerows(self.estudantes) 

    def adicionar_estudante(self):
        nome = input('Nome: ')
        idade = input('Idade: ')
        nota_matematica = input('Nota em matemática: ')
        nota_ciencia = input('Nota em Ciências: ')
        nota_ingles = input('Nota em inglês: ') 

        novo_estudante = {
            'Nome':nome,
            'Idade':idade,
            'Nota_Matematica':nota_matematica,
            'Nota_Ciencias': nota_ciencia,
            'Nota_Ingles': nota_ingles
        }
        self.estudantes.append(novo_estudante) 
        self.salvar_dados() 
        print('Estudante adicionado com sucesso')    

    def listar_estudantes(self):
        if not  self.estudantes:
            print('Nenhum estudante cadastrado')
        for aluno in enumerate(self.estudantes):
            print(aluno)  

    def atualizar(self):
        self.listar_estudantes()
        if not self.estudantes:
            return
        
        try:
            indice = int(input("Digite o número do índice do aluno a ser atualizado: "))
            if 0 <= indice < len(self.estudantes):
                nome = input('Nome: ')
                idade = input('Idade: ')
                nota_matematica = input('Nota em matemática: ')
                nota_ciencia = input('Nota em Ciências: ')
                nota_ingles = input('Nota em inglês: ') 
                self.estudantes[indice] = {'Nome':nome,'Idade': idade, 'Nota_Matematica': nota_matematica,'Nota_Ciencias': nota_ciencia,'Nota_Ingles': nota_ingles}
                self.salvar_dados()
                print('Aluno atualizado com sucesso!')
            else:
                print("Índice inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")

    def deletar(self):
        self.listar_estudantes()
        if not self.estudantes:
            return
        
        try:
            indice = int(input("Digite o número do índice do aluno a ser deletado: "))
            if 0 <= indice < len(self.estudantes):
                self.estudantes.pop(indice)
                self.salvar_dados()
                
                print('Aluno deletado com sucesso!')
            else:
                print("Índice inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")     

    def media(self):
        print(f"{'Nome':<20}{'Média':<10}{'Situação':<10}")
       
        for estudante in self.estudantes:
            notas = [float(estudante['Nota_Matematica']), float(estudante['Nota_Ciencias']), float(estudante['Nota_Ingles'])]
            media = sum(notas) / len(notas)
            if media<70:
                situacao='Reprovado'
            else:
                situacao='Aprovado'    
            print(f"{estudante['Nome']:<20}{media:<10.2f}{situacao:<10}")   

    def filtrarPorIdade(self):
        try:
            idade_filtro = int(input("Digite a idade para filtrar: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            return
        
        estudantes_filtrados = [estudante for estudante in self.estudantes if int(estudante['Idade']) == idade_filtro]

        if not estudantes_filtrados:
            print(f"Nenhum aluno encontrado com idade {idade_filtro}.")
        else:
            # Cabeçalho
            print(f"{'Nome':<20}{'Idade':<10}{'Matematica':<15}{'Ciencias':<15}{'Ingles':<15}")
            print('-' * 70)
            
            for estudante in estudantes_filtrados:
                print(f"{estudante['Nome']:<20}{estudante['Idade']:<10}{estudante['Nota_Matematica']:<15}{estudante['Nota_Ciencias']:<15}{estudante['Nota_Ingles']:<15}")
          
    def limpar_terminal(self):
        # Detecta o sistema operacional e executa o comando de limpeza apropriado
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Linux e Mac
            os.system('clear')               

    def menu(self):
        while True:
            print('1 - Adicionar Estudante')
            print('2 - Listar Estudantes')
            print('3 - Atualizar Estudante')
            print('4 - Deletar Estudante')
            print('5 - Mostrar Média de Notas')
            print('6 - Filtrar Estudantes por Idade')
            print('7 - Sair')
            escolha = input('Escolha uma opção: ')
            
            if escolha == '1':
                self.limpar_terminal()
                self.adicionar_estudante()

            elif escolha == '2':
                self.limpar_terminal()
                self.listar_estudantes()

            elif escolha == '3':
                self.limpar_terminal()
                self.atualizar()
                
            elif escolha == '4':
                self.limpar_terminal()
                self.deletar()
            
            elif escolha == '5':
                self.limpar_terminal()
                self.media()

            elif escolha == '6':
                self.limpar_terminal()
                self.filtrarPorIdade()

            elif escolha == '7':
                self.limpar_terminal()
                print('Encerrando o programa.')
                break
            else:
                print('Opção inválida.')            







alunos= SistemaEstudantes()
alunos.menu()


                            