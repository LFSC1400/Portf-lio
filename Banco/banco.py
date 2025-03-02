class Banco:
    def __init__(self):
        self.saldo = 1500
        self.sd = 0
        self.limite_saques = 3
        self.ls = 500

    def sacar(self, valor):
        if self.sd >= self.limite_saques:
            print("Limite diário de saques atingido.")
        elif valor > self.ls:
            print(f"Valor máximo por saque é de R${self.limite_saque:.2f}.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.sd += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def mostrar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

def main():
    banco = Banco()

    while True:
        print("\nEscolha uma opção:")
        print("1 - Sacar")
        print("2 - Depositar")
        print("3 - Ver Saldo")
        print("4 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor que deseja sacar: "))
            banco.sacar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor que deseja depositar: "))
            banco.depositar(valor)
        elif opcao == "3":
            banco.mostrar_saldo()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()