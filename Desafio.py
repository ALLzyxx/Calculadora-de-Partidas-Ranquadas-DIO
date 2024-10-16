vitorias = float(input("Digite a quantidade de vitorias:\n"))
derrotas = float(input("Digite a quantidade de derrotas:\n"))
def calcular_nivel(vitorias, derrotas):
    # Calcula o saldo de vitórias
    saldo_vitorias = vitorias - derrotas
    nivel = ""

    # Determina o nível com base no número de vitórias
    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    elif vitorias >= 101:
        nivel = "Imortal"

    # Retorna a mensagem formatada
    return f"O Herói tem de saldo de {saldo_vitorias} está no nível de {nivel}"

# Exemplo de uso da função
resultado = calcular_nivel(vitorias, derrotas)
print(resultado)
