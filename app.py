def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida")
    return a / b

def eh_par(n):
    return n % 2 == 0

if __name__ == "__main__":
    print("Projeto DevOps funcionando!")
