
import random

def ler_sensores():
    temperatura = round(random.uniform(22.0, 28.0), 1)
    umidade = random.randint(30, 70)
    return temperatura, umidade
