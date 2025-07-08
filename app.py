class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class FilaHospital:
    def __init__(self):
        self.head = None
        self.contador_verde = 1
        self.contador_amarelo = 201
    
    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = nodo
    
    def inserirComPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        elif self.head.cor == "V":
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None and atual.proximo.cor == "A":
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo
    
    def inserir(self):
        cor = input("Digite a cor do cartão (A ou V): ").upper()
        
        if cor == "V":
            numero = self.contador_verde
            self.contador_verde += 1
        elif cor == "A":
            numero = self.contador_amarelo
            self.contador_amarelo += 1
        else:
            print("Cor inválida! Digite A ou V.")
            return
        
        nodo = Nodo(numero, cor)
        
        if self.head is None:
            self.head = nodo
        elif cor == "V":
            self.inserirSemPrioridade(nodo)
        elif cor == "A":
            self.inserirComPrioridade(nodo)
    
    def imprimirListaEspera(self):
        if self.head is None:
            print("Fila vazia!")
            return
        
        atual = self.head
        print("Lista de espera:")
        while atual is not None:
            print(f"Cartão {atual.cor}{atual.numero}")
            atual = atual.proximo
    
    def atenderPaciente(self):
        if self.head is None:
            print("Não há pacientes na fila!")
            return
        
        paciente = self.head
        self.head = self.head.proximo
        print(f"Chamando paciente com cartão {paciente.cor}{paciente.numero} para atendimento!")
    
    def menu(self):
        while True:
            print("\n=== SISTEMA DE TRIAGEM HOSPITALAR ===")
            print("1 - Adicionar paciente à fila")
            print("2 - Mostrar pacientes na fila")
            print("3 - Chamar paciente")
            print("4 - Sair")
            
            try:
                opcao = input("Escolha uma opção: ")
                
                if opcao == "1":
                    self.inserir()
                elif opcao == "2":
                    self.imprimirListaEspera()
                elif opcao == "3":
                    self.atenderPaciente()
                elif opcao == "4":
                    print("Encerrando o programa...")
                    break
                else:
                    print("Opção inválida! Escolha uma opção entre 1 e 4.")
            except KeyboardInterrupt:
                print("\nPrograma interrompido pelo usuário.")
                break
            except Exception as e:
                print(f"Erro: {e}")

# Execução do programa
if __name__ == "__main__":
    fila = FilaHospital()
    fila.menu()
