menu = """
======================================
 Selecione a operação desejada: 

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

======================================
"""

saldo = 0
limite_por_saque = 500
extrato = ""
numero_saques = 0
LIMITE_DIARIO_SAQUE = 3

while True:

  opcao = input(menu)

  if opcao == "0":
    valor_deposito = float(input("Digite o valor desejado: "))
    if valor_deposito > 0:
      saldo += valor_deposito
      extrato += f"Depósito: R${valor_deposito:.2f}\n"
      print(f"Depósito de R${valor_deposito} realizado com sucesso!")
    else:
      print("O valor do depósito é inválido.")

  elif opcao == "1":
    if numero_saques < LIMITE_DIARIO_SAQUE:
     valor_saque = float(input("Digite o valor do saque desejado: "))
     if saldo >= valor_saque and valor_saque <= limite_por_saque:
      saldo -= valor_saque
      extrato += f"Saque: R$ {valor_saque:.2f}\n"
      numero_saques += 1
      print(f"Saque de R${valor_saque} realizado!")

     elif saldo < valor_saque:
      print("Saldo insuficiente!")
    
     else:
      print(f"Valor do saque excedido. Seu limite de saque é de R${limite_por_saque}!")
    
    else:
      print(f"Limite diário de saques atingido. Seu limite atual é de {LIMITE_DIARIO_SAQUE}!")
    
    

  elif opcao == "2":
    print("Sem movimentações!" if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    
  elif opcao == "3":
    break

  else:
    print("Opção inválida, por favor, selecione novamente a operação desejada.")