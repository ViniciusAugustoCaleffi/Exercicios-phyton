import math
import random

class Operacao:
    def __init__(self): #construtor
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
    def coletar(self, num1, num2,num3): #criando o metodo coletar
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def somar(self,num1, num2):

        self.coletar(num1,num2) #ultilizando o metodo coletar
        return self.num1 + self.num2

    def subtrair(self,num1,num2):

        self.coletar(num1,num2)
        return self.num1 - self.num2

    def multiplicar(self,num1,num2):
        self.coletar(num1,num2)
        return self.num1 * self.num2

    def dividir(self,num1,num2):
        self.coletar(num1,num2)
        if self.num2 <= 0:
            return "Impossivel dividir!"
        else:
            return self.num1 / self.num2

    def tabuada(self,num1):
        resultado = ""
        for i in range(0,11,1):
            resultado += f'\n{num1} * {i} = {num1 * i}  '
        return resultado

    def potencia(self,base,expoente):
        return pow(base,expoente)

    def raiz(self,num):
        return math.sqrt(num)

    def exercicio01(self):
        msg = ""
        for i in range(1, 11, 1):
            msg += F'\n{i}'
        return msg

    def exercicio02(self):

        msg = ""
        for i in range(2,21,2):
            msg += F'\n{i}'
        return msg

    def exercicio03(self):
        msg = ""
        for i in range(1, 101,1):
            msg += F'\n{i}'
        return msg

    def exercicio04(self):
        msg=""
        for i in range(1,51,1):
            if i % 5 == 0:
                msg += F'\n{i}'
        return msg

    def exercicio05(self,num1):
        self.coletar(self,num1)
        return "par" if num1 % 2 == 0 else "impar"

    def exercicio06(self,num1):
        if num1 > 0:
            return "positivo"
        elif num1 < 0:
            return "negativo"
        else:
            return "zero (0)"

    def exercicio07(self,num1):
            return [(f'{num1} x {i} = {num1 * i}')for i in range(1, 11, 1)]

    def exercicio08(self,num1):
            return list (range (1,num1 + 1))

    def exercicio09(self,num1):
            return sum (range (1,num1 + 1))

    def exercicio10(self,num1):

        self.coletar(self,num1)

        for i in range(2,num1 + 1):

            if (num1 % 2 != 0 and num1 % 3 != 0 and num1 % 5 != 0):

                return (num1)

    def exercicio11(self,num1):

        self.coletar(self,num1)

        if num1 % 2 or num1 % 3 or num1 % 5 != 0:

            return "O numero é primo"
        else:

            return "O numero não é primo"

    def exercicio12(self,num1):

        self.coletar(self,num1)

        resultado = math.factorial(num1)

        return (f"O fatorial de {num1} é {resultado}")

    def exercicio13(self):

        num1=5

        fatorial=1

        for i in range(1, num1 + 1):
            fatorial *= i
            if i == 1:
                print(f"{i}")
            else:
                print(f"\n * {i}")

        return fatorial

    def exercicio15(self,num1):
        num1 = input("Digite um número: ")
        num1_str = str(num1)
        soma = 0
        for digito in num1_str:
            soma += int(digito)
        return soma


    def exercicio16(self,num1):

        pares=[i for i in range(1,num1+1) if i % 2 == 0]

        impares=[i for i in range(1,num1+1) if i % 2 !=0]

        return f"pares:  {pares}\n impares: {impares}\n"

    def exercicio17(self,num1):

        self.coletar(self,num1)
        if num1 < 2:
            return False
        for i in range(2, int(num1 ** 0.5) + 1):
            if num1 % i == 0:
                return False
        return True

        for i in range(1, 21):  # Exemplo: de 1 a 20
            if eh_primo(i):
                return(f"{i} é primo.")
            else:
                return(f"{i} não é primo.")

    def exercicio18(self):
        resposta = 0
        contar = ""
        self.num = int(input('Informe um número: '))
        while self.num > 1:
            if self.num % 2 == 0:
                self.num = self.num / 2
                contar = f'\n{self.num}'
            else:
                self.num = 3 * self.num + 1
                resposta += 1
                contar = f'\n{self.num}'
            return f'{contar}\nresultado: {resposta}'

    def exercicio19(self):
        par = 0
        impar = 0
        self.num = int(input('Informe um número: '))
        for i in range(1, self.num, 1):
            if i % 2 == 0:
                par += i
            else:
                impar = i + impar
        return f'A soma dos pares é: {par}\nA soma dos ímpares é: {impar}'

    def exercicio20(self):
        resposta = ""
        self.num = int(input('Informe um número: '))
        for i in range(1, self.num, 1):
            if i % self.num == 0:
                resposta = resposta + 1
        if resposta == self.num:
            return f'O número {resposta} é um número perfeito'
        else:
            return f'O número {resposta - self.num} não é um número perfeito'

    def exercicio21(self):
        a = 10
        b = 20
        x = b
        a = b
        b = x
        return f'O número 10 agora é {b} e o número 20 agora é {a}'

    def exercicio22(self):
        num = int(input('Informe um número: '))
        num -= 1
        return f'O número anterior ao número digitado é {num}'

    def exercicio23(self):
        base = self.num = int(input('Informe a base: '))
        altura = self.num = int(input('Informe a altura: '))

        area = base * altura

        return f'A área do retângulo é: {area}'

    def exercicio24(self):
        ano = self.num = int(input('Informe o ano do seu nascimento: '))
        mes = self.num = int(input('Informe o mês do seu nascimento: '))
        dia = self.num = int(input('Informe o dia do seu nascimento: '))

        if mes < 1 or mes > 13:
            return f'Erro! Informe um número maior que zero e/ou menor que 12'
        mes = mes * 30
        ano = ano * 365
        dia = dia + mes + ano
        return f'A sua idade expressa em dias é {dia}'

    def exercicio25(self):
        eleitor = self.num = int(input('Informe o total de eleitores: '))
        branco = self.num = int(input('Informe o total de votos brancos: '))
        nulo = self.num = int(input('Informe o total de votos nulos: '))
        valido = self.num = int(input('Informe o total de votos válidos: '))

        percentualBranco = branco / eleitor * 100
        percentualNulo = nulo / eleitor * 100
        percentualValido = valido / eleitor * 100

        return f'O número total de votos brancos representa {percentualBranco} do número total de eleitores: {eleitor}.' \
               f'O número total de votos nulos representa {percentualNulo} do número total de eleitores: {eleitor}' \
               f'O número total de votos válidos representa {percentualValido} do número total de eleitores: {eleitor}'

    def exercicio26(self,num1,num2):

        self.coletar(self.num1,num2)

        num2 = num2/100
        num1 = num1 * (num2) + num1
        return f"O salário reajustado é: {num1}"

    def exercicio27(self,num1):

        self.coletar(self.num1,self.num2,self.num3)
        num3 = num1

        num4 = num3 * 0.28
        i = num3 * 0.45
        num5 = num3 + num4 + i
        return f'O custo final ao consumidor é: {num5}'

    def exercicio28(self,num1,num2,num3):

        self.coletar(self.num1,self.num2,self.num3)

        i = (num1 + num2 + num3) /3

        return i

    def exercicio29(self,num1):

        if num1 < 12:
            num1 = num1 * 1.30
        elif num1 >= 12:
            num1 = num1 * 1.00

        return num1

    def exercicio30(self):

        random_numbers = [random.randint(0, 10) for _ in range(10)]
        sorted_numbers = sorted(random_numbers)

        print("Números aleatórios:", random_numbers)
        return("Números ordenados:", sorted_numbers)

    def exercicio31(self, num1, num2):
        i = 0
        j = 0

        if num2 < 1.500:
            i = num2 * 0.03
        else:
            i = num2 * 0.03
            j = i * 0.05


        vf = num1 + i + j

        return vf

    def exercicio32(self,num1,num2,num3):

        self.coletar(self.num1,self.num2,self.num3)

        sf = num1 - num2 + num3

        if sf < 0:
            return "o saldo é negativo"
        else:
            return "o saldo é postivo"

    def exercicio33(self,num1):

        if num1 >10:
            return "o numero é maior que 10 tente novamente"

        else:
                resultado = ""
                for i in range(0, 11, 1):
                    resultado += f'\n{num1} * {i} = {num1 * i}  '
                return resultado


    def exercicio34(self,num1):

        random_numbers = [random.randint(0, 10) for _ in range(10)]
        sorted_numbers = sorted(random_numbers)

        if random_numbers < 0:

            print("Números aleatórios:", random_numbers)
            return ("Números ordenados:", sorted_numbers)














