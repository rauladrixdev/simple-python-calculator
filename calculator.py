"""
Calculadora simples de terminal.
Autor: Raul
"""

OPERADORES = ["+", "-", "*", "/", "//", "**"]


def calcular(n1, n2, operador):
    # verifica se o operador é válido
    if operador not in OPERADORES:
        return "Operador inválido."

    if operador in ("/", "//") and n2 == 0:
        return "Erro: divisão por zero."

    if operador == "+":
        return n1 + n2
    elif operador == "-":
        return n1 - n2
    elif operador == "*":
        return n1 * n2
    elif operador == "/":
        return n1 / n2
    elif operador == "//":
        return n1 // n2
    elif operador == "**":
        return n1 ** n2


def pedir_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite apenas números.")


def main():
    print("=" * 35)
    print("      Calculadora Simples")
    print("=" * 35)
    print("Operadores: +  -  *  /  //  **")
    print("Digite 0 nos dois campos para sair.\n")

    while True:
        n1 = pedir_numero("Primeiro número: ")
        n2 = pedir_numero("Segundo número:  ")

        if n1 == 0 and n2 == 0:
            print("Encerrando... até mais!")
            break

        operador = input("Operador: ").strip()
        resultado = calcular(n1, n2, operador)

        print(f"Resultado: {resultado}\n")


if __name__ == "__main__":
    main()
