# Função para calcular o custo total de produção de cada sanduíche
#custos_totais.append. Esse método está sendo usado para adicionar os 
# resultados de cada cálculo de custo à lista custos_totais
def calcular_custo_total(quantidades, precos):
    custos_totais = []
    for quantidades_sanduiche in quantidades:
        custo_total = sum(q * p for q, p in zip(quantidades_sanduiche, precos))  # Fórmula de multiplicação
        custos_totais.append(round(custo_total, 2))  # Arredondamos o resultado
    return custos_totais

# Função para aplicar a correção de 70% no custo
def aplicar_correcao(custos):
    return [round(custo * 1.7, 2) for custo in custos]  # Aplicando correção de 70%

# Quantidades de ingredientes para cada sanduíche (X-Delícia e X-Super)
quantidades = [
    [1, 0.20, 0.15, 0.15, 0],  # X-Delícia: (pão, presunto, queijo, tomate, ovo)
    [1, 0.25, 0.20, 0.15, 2]   # X-Super: (pão, presunto, queijo, tomate, ovo)
]

# Preços dos ingredientes no Supermercado 1
precos_mercado1 = [1.20, 29.90, 42.00, 6.00, 1.60]

# Preços dos ingredientes no Supermercado 2
precos_mercado2 = [1.04, 41.25, 42.90, 8.00, 0.90]

# Calculando os custos totais para cada supermercado
custos_mercado1 = calcular_custo_total(quantidades, precos_mercado1)
custos_mercado2 = calcular_custo_total(quantidades, precos_mercado2)

# Aplicando a correção de 70%
custos_mercado1_corrigido = aplicar_correcao(custos_mercado1)
custos_mercado2_corrigido = aplicar_correcao(custos_mercado2)

# Exibindo os resultados
print("Custo total no Supermercado 1 (sem correção):", custos_mercado1)  # [14.38, 21.18]
print("Custo total no Supermercado 2 (sem correção):", custos_mercado2)  # [16.93, 22.93]
print("Custo total no Supermercado 1 (com correção):", custos_mercado1_corrigido)  # [24.44, 36.01]
print("Custo total no Supermercado 2 (com correção):", custos_mercado2_corrigido)  # [28.78, 38.98]

# Função para atualizar preços do Supermercado 1
def atualizar_precos_mercado1():
    global custos_mercado1_corrigido, custos_mercado1  # Atualiza as variáveis globais
    print("Digite os preços atualizados dos ingredientes para o Supermercado 1:")
    preco_pao1 = float(input("Preço do pão (por unidade): "))
    preco_presunto1 = float(input("Preço do presunto (por kg): "))
    preco_queijo1 = float(input("Preço do queijo (por kg): "))
    preco_tomate1 = float(input("Preço do tomate (por unidade): "))
    preco_ovo1 = float(input("Preço do ovo (por unidade): "))
    
    # Cria a lista com os novos preços para o Supermercado 1
    precos_novos_mercado1 = [preco_pao1, preco_presunto1, preco_queijo1, preco_tomate1, preco_ovo1]
    
    # Calcula o custo total sem correção
    custos_mercado1 = calcular_custo_total(quantidades, precos_novos_mercado1)
    # Calcula o custo total com a correção
    custos_mercado1_corrigido = aplicar_correcao(custos_mercado1)
    
    # Exibe os resultados
    print("\nCusto total com preços atualizados no Supermercado 1 (sem correção):", custos_mercado1)
    print("Custo total com preços atualizados no Supermercado 1 (com correção):", custos_mercado1_corrigido)

# Função para atualizar preços do Supermercado 2
def atualizar_precos_mercado2():
    global custos_mercado2_corrigido, custos_mercado2  # Atualiza as variáveis globais
    print("Digite os preços atualizados dos ingredientes para o Supermercado 2:")
    preco_pao2 = float(input("Preço do pão (por unidade): "))
    preco_presunto2 = float(input("Preço do presunto (por kg): "))
    preco_queijo2 = float(input("Preço do queijo (por kg): "))
    preco_tomate2 = float(input("Preço do tomate (por unidade): "))
    preco_ovo2 = float(input("Preço do ovo (por unidade): "))
    
    # Cria a lista com os novos preços para o Supermercado 2
    precos_novos_mercado2 = [preco_pao2, preco_presunto2, preco_queijo2, preco_tomate2, preco_ovo2]
    
    # Calcula o custo total sem correção
    custos_mercado2 = calcular_custo_total(quantidades, precos_novos_mercado2)
    # Calcula o custo total com a correção
    custos_mercado2_corrigido = aplicar_correcao(custos_mercado2)
    
    # Exibe os resultados
    print("\nCusto total com preços atualizados no Supermercado 2 (sem correção):", custos_mercado2)
    print("Custo total com preços atualizados no Supermercado 2 (com correção):", custos_mercado2_corrigido)

# Função para exibir as tabelas de custos totais corrigidos e sem correção
def exibir_tabelas_custos():
    print("\nTabela de custos totais (sem correção):")
    print("Supermercado 1 (sem correção):", custos_mercado1)
    print("Supermercado 2 (sem correção):", custos_mercado2)
    print("\nTabela de custos totais corrigidos:")
    print("Supermercado 1 (com correção):", custos_mercado1_corrigido)
    print("Supermercado 2 (com correção):", custos_mercado2_corrigido)

# Menu para o usuário escolher a ação
def menu():
    while True:
        print("\nSelecione uma opção:")
        print("1 - Alterar preços do Supermercado 1")
        print("2 - Alterar preços do Supermercado 2")
        print("3 - Exibir tabelas de custos totais corrigidos e sem correção")
        print("4 - Encerrar o programa")
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            atualizar_precos_mercado1()
        elif opcao == '2':
            atualizar_precos_mercado2()
        elif opcao == '3':
            exibir_tabelas_custos()
        elif opcao == '4':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, selecione 1, 2, 3 ou 4.")

# Chamando o menu para iniciar o programa
menu()
