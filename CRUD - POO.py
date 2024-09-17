import json
import os

class Sistema:
    def __init__(self):
        self.dicionarios = {}  # Inicializa um dicionário vazio para armazenar os dicionários criados
        self.carregar_dados()

    def criar(self, nome):
        if nome in self.dicionarios:  # Verifica se já existe um dicionário com o mesmo nome
            return f"Um dicionário com o nome '{nome}' já existe."
        self.dicionarios[nome] = {}  # Cria um novo dicionário vazio com o nome fornecido
        self.salvar_dados()  # Salva os dicionários no arquivo dicionarios.json
        return f"Dicionário '{nome}' criado com sucesso."

    def ler(self, nome):
        if nome in self.dicionarios:  # Verifica se o dicionário com o nome fornecido existe
            return self.dicionarios[nome]  # Retorna o dicionário correspondente
        return f"Dicionário '{nome}' não encontrado."

    def inserir(self, nome, chave, valor):
        if nome in self.dicionarios:  # Verifica se o dicionário com o nome fornecido existe
            if chave not in self.dicionarios[nome]:  # Verifica se a chave já existe no dicionário
                self.dicionarios[nome][chave] = valor  # Insere a chave e o valor no dicionário
                self.salvar_dados()  # Salva os dicionários no arquivo dicionarios.json
                return f"Chave '{chave}' inserida no dicionário '{nome}'."
            return f"A chave '{chave}' já existe no dicionário '{nome}'."
        return f"Dicionário '{nome}' não encontrado."

    def atualizar(self, nome, chave_antiga, chave_nova, valor_novo):
        if nome in self.dicionarios:  # Verifica se o dicionário com o nome fornecido existe
            if chave_antiga in self.dicionarios[nome]:  # Verifica se a chave antiga existe no dicionário
                self.dicionarios[nome][chave_nova] = self.dicionarios[nome].pop(chave_antiga)  # Renomeia a chave
                self.dicionarios[nome][chave_nova] = valor_novo  # Atualiza o valor da chave
                self.salvar_dados()  # Salva os dicionários no arquivo dicionarios.json
                return f"Chave '{chave_antiga}' atualizada para '{chave_nova}' com o novo valor no dicionário '{nome}'."
            return f"A chave '{chave_antiga}' não existe no dicionário '{nome}'."
        return f"Dicionário '{nome}' não encontrado."

    def deletar(self, nome):
        if nome in self.dicionarios:  # Verifica se o dicionário com o nome fornecido existe
            del self.dicionarios[nome]  # Deleta o dicionário
            self.salvar_dados()
            return f"Dicionário '{nome}' deletado com sucesso."
        return f"Dicionário '{nome}' não encontrado."

    def deletar_chave(self, nome, chave): 
        if nome in self.dicionarios:  # Verifica se o dicionário com o nome fornecido existe
            if chave in self.dicionarios[nome]:  # Verifica se a chave existe no dicionário
                del self.dicionarios[nome][chave]  # Deleta a chave do dicionário
                self.salvar_dados()  # Salva os dicionários no arquivo dicionarios.json
                return f"Chave '{chave}' deletada do dicionário '{nome}'."
            return f"Chave '{chave}' não encontrada no dicionário '{nome}'."
        return f"Dicionário '{nome}' não encontrado."
    
    def listar_dicionarios(self):
        return list(self.dicionarios.keys())  # Retorna uma lista com os nomes de todos os dicionários

    def listar_chaves(self, nome):
        return list(self.dicionarios[nome].keys())  # Retorna uma lista com as chaves do dicionário fornecido

    def salvar_dados(self):
        with open("dicionarios.json", "w") as arquivo_json: # Abre o arquivo dicionarios.json
            json.dump(self.dicionarios, arquivo_json)  # Salva os dicionários no arquivo dicionarios.json

    def carregar_dados(self):
        if os.path.exists("dicionarios.json"): # Verifica se o arquivo dicionarios.json existe
            with open("dicionarios.json", "r") as arquivo_json: # Abre o arquivo dicionarios.json
                self.dicionarios = json.load(arquivo_json)  # Carrega os dicionários do arquivo dicionarios.json


class Interface:
    def __init__(self):
        self.sistema = Sistema()  # Inicializa uma instância da classe Sistema

    def menu(self):
        while True:
            print('\n'*5)
            print('┌───────────────────────────────────────┐') 
            print("|Escolha uma opção:                     |")
            print("| 1. Criar dicionário                   |")
            print("| 2. Visualizar dicionário              |")
            print("| 3. Inserir dados no dicionário        |")
            print("| 4. Atualizar dados no dicionário      |")
            print("| 5. Deletar dicionário                 |")
            print("| 6. Deletar chave de um dicionário     |")
            print("| 7. Sair                               |")
            print('└───────────────────────────────────────┘')
            escolha = input("Opção: ")

            if escolha == '1':
                nome = input("Digite o nome do dicionário: ")
                print(self.sistema.criar(nome))  # Chama o método criar da classe Sistema
                print('\n')
                enter = input("Aperte <ENTER> para continuar...")

            elif escolha == '2':
                if not self.sistema.listar_dicionarios():  # Verifica se existem dicionários cadastrados
                    print("Ainda não há dicionários cadastrados.")
                    print('\n')
                    enter = input("Aperte <ENTER> para continuar...")
                    continue
                print("Dicionários cadastrados:")
                print(self.sistema.listar_dicionarios())  # Chama o método listar_dicionarios da classe Sistema
                nome = input("Digite o nome do dicionário: ")
                print(self.sistema.ler(nome))  # Chama o método ler da classe Sistema
                print('\n')
                enter = input("Aperte <ENTER> para continuar...")

            elif escolha == '3':
                if not self.sistema.listar_dicionarios():  # Verifica se existem dicionários cadastrados
                    print("Ainda não há dicionários cadastrados.")
                    print('\n')
                    enter = input("Aperte <ENTER> para continuar...")
                    continue
                print("Dicionários cadastrados:")
                print(self.sistema.listar_dicionarios())  # Chama o método listar_dicionarios da classe Sistema
                nome = input("Digite o nome do dicionário: ")
                if nome not in self.sistema.listar_dicionarios():
                    print(f"Ainda não existe dicionario com o nome {nome}.")
                    print('\n')
                    enter = input("Aperte <ENTER> para continuar...")
                    continue
                chave = input("Digite a chave que deseja inserir: ")
                valor = input("Digite o valor: ")
                print(self.sistema.inserir(nome, chave, valor))  # Chama o método inserir da classe Sistema
                print('\n')
                enter = input("Aperte <ENTER> para continuar...")

            elif escolha == '4':
                if not self.sistema.listar_dicionarios():  # Verifica se existem dicionários cadastrados
                    print("Ainda não há dicionários cadastrados.")
                    print('\n')
                    enter = input("Aperte <ENTER> para continuar...")
                    continue
                print("Dicionários cadastrados:")
                print(self.sistema.listar_dicionarios())  # Chama o método listar_dicionarios da classe Sistema
                nome = input("Digite o nome do dicionário: ")
                if nome not in self.sistema.listar_dicionarios():
                    print(f"Ainda não existe dicionario com o nome {nome}.")
                    print('\n')
                    enter = input("Aperte <ENTER> para continuar...")
                    continue
                if not self.sistema.listar_chaves(nome):  # Verifica se existem chaves cadastradas no dicionário
                    print("Ainda não há chaves cadastradas neste dicionário.")
                    print('\n')
                    enter = input("Aperte <ENTER> para continuar...")
                    continue
                else:
                    print("Chaves cadastradas:")
                    print(self.sistema.listar_chaves(nome))  # Chama o método listar_chaves da classe Sistema
                chave_antiga = input("Digite a chave que deseja alterar: ")
                chave_nova = input("Digite o novo nome da chave: ")
                valor_novo = input("Digite o novo valor: ")
                print(self.sistema.atualizar(nome, chave_antiga, chave_nova, valor_novo))  # Chama o método atualizar da classe Sistema
                print('\n')
                enter = input("Aperte <ENTER> para continuar...")

            elif escolha == '5':
                if not self.sistema.listar_dicionarios():  # Verifica se existem dicionários cadastrados
                    print("Ainda não há dicionários cadastrados.")
                    print('\n')
                    enter = input("Aperte <ENTER> para continuar...")
                    continue
                print("Dicionários cadastrados:")
                print(self.sistema.listar_dicionarios())  # Chama o método listar_dicionarios da classe Sistema
                nome = input("Digite o nome do dicionário: ")
                print(self.sistema.deletar(nome))  # Chama o método deletar da classe Sistema
                print('\n')
                enter = input("Aperte <ENTER> para continuar...")

            elif escolha == '6':
                if not self.sistema.listar_dicionarios():  # Verifica se existem dicionários cadastrados
                    print("Ainda não há dicionários cadastrados.")
                    print('\n')
                    enter = input("Aperte <ENTER> para continuar...")
                    continue
                print("Dicionários cadastrados:")
                print(self.sistema.listar_dicionarios())  # Chama o método listar_dicionarios da classe Sistema
                nome = input("Digite o nome do dicionário: ")
                if not self.sistema.listar_chaves(nome):  # Verifica se existem chaves cadastradas no dicionário
                    print("Ainda não há chaves cadastradas neste dicionário.")
                    print('\n')
                    enter = input("Aperte <ENTER> para continuar...")
                    continue
                print("Chaves cadastradas:")
                print(self.sistema.listar_chaves(nome))  # Chama o método listar_chaves da classe Sistema
                chave = input("Digite a chave que deseja deletar: ")
                if chave not in self.sistema.listar_chaves(nome):  # Verifica se a chave existe no dicionário
                    print(f"A chave '{chave}' não existe no dicionário '{nome}'.")
                    print('\n')
                    enter = input("Aperte <ENTER> para continuar...")
                    continue
                print(self.sistema.deletar_chave(nome, chave))  # Chama o método deletar_chave da classe Sistema
                print('\n')
                enter = input("Aperte <ENTER> para continuar...")

            elif escolha == '7':
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")

# Para rodar a interface
if __name__ == "__main__":
    interface = Interface()
    interface.menu()

