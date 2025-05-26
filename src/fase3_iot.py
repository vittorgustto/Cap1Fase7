
# Simulação de irrigação inteligente com sensores

def verificar_irrigacao(umidade, ph, temperatura):
    if umidade < 40:
        return "Acionar irrigação: Umidade baixa"
    elif ph < 5.5 or ph > 7.5:
        return "Corrigir pH do solo"
    elif temperatura > 35:
        return "Atenção: Temperatura elevada"
    else:
        return "Condições ideais - Irrigação não necessária"

# Exemplo de chamada
if __name__ == "__main__":
    resposta = verificar_irrigacao(35, 6.2, 32)
    print(resposta)
