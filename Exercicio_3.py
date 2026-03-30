total_arrecadado = 0

for i in range(10):
    print(f"\nCliente {i+1}")
    
    nome = input("Digite o nome do cliente: ")
    valor_compra = float(input("Digite o valor da compra: "))

    if valor_compra >= 250:
        desconto = valor_compra * 0.20
    else:
        desconto = valor_compra * 0.15
        
    valor_pagar = valor_compra - desconto

    total_arrecadado += valor_pagar

    print("Nome:", nome)
    print("Valor da compra: $", valor_compra)
    print("Valor do desconto: $", desconto)
    print("Valor a pagar: $", valor_pagar)

print("\nTotal arrecadado pela loja: $", total_arrecadado)