import matplotlib.pyplot as plt

# Função para calcular projeção de retorno
def calcular_projecao(valor_inicial, taxa_juros_anual, anos=10):
    valores = [valor_inicial]
    for _ in range(anos):
        valor_inicial *= (1 + taxa_juros_anual)
        valores.append(valor_inicial)
    return valores

# Função para sugerir valor ideal com base no tipo de investimento e perfil de risco
def valor_ideal(tipo_investimento, perfil_risco):
    base = 10000
    multiplicador = {
        'baixo': 1.2,
        'médio': 1.5,
        'alto': 2.0
    }
    tipo_bonus = {
        'imobiliário': 1.1,
        'cotas': 1.3
    }
    return base * multiplicador[perfil_risco] * tipo_bonus[tipo_investimento]

# Função principal do simulador
def simulador_investimento():
    print("Bem-vindo ao Simulador de Investimentos!")
    print("Perfis de risco disponíveis: baixo, médio, alto")
    perfil = input("Escolha seu perfil de risco: ").strip().lower()

    print("Tipos de investimento disponíveis: imobiliário, cotas")
    tipo = input("Escolha o tipo de investimento: ").strip().lower()

    valor_inicial = float(input("Digite o valor que deseja investir: R$ "))

    # Taxas de juros simuladas por perfil e tipo
    taxas = {
        'baixo': {'imobiliário': 0.04, 'cotas': 0.05},
        'médio': {'imobiliário': 0.06, 'cotas': 0.08},
        'alto': {'imobiliário': 0.09, 'cotas': 0.12}
    }

    taxa_juros = taxas[perfil][tipo]
    valores_projetados = calcular_projecao(valor_inicial, taxa_juros)
    valor_sugerido = valor_ideal(tipo, perfil)

    print(f"\nValor ideal sugerido para esse tipo de investimento: R$ {valor_sugerido:,.2f}")
    print(f"Valor projetado após 10 anos: R$ {valores_projetados[-1]:,.2f}")

    # Visualização gráfica
    anos = list(range(11))
    plt.plot(anos, valores_projetados, marker='o')
    plt.title(f"Projeção de Investimento ({tipo.capitalize()}, Risco {perfil.capitalize()})")
    plt.xlabel("Ano")
    plt.ylabel("Valor (R$)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Executar o simulador
simulador_investimento()
