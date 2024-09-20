from operacao import Operacao

class  Menu:
    def __init__(self):
        self.opcao = -1
        self.opera = Operacao()
        self.num1  = 0
        self.num2  = 0

    def mostrarmenu(self):
        print('\n ------ MENU ------\n\n'
              'Escolha uma das opcões abaixo: ' +
              '\n0.  sair'       +
              '\n1.  somar'      +
              '\n2.  subtrair'   +
              '\n3.  dividir'    +
              '\n4.  multiplicar'+
              '\n5.  Potencia'   +
              '\n6   raiz'       +
              '\n7.  tabuada'    +
              '\n8.  Exercicio 1'+
              '\n9.  Exercicio 2'+
              '\n10. Exercicio 3'+
              '\n11. Exercicio 4'+
              '\n12. Exercicio 5'+
              '\n13. Exercicio 6'+
              '\n14. Exercicio 7'+
              '\n15. Exercicio 8'+
              '\n16. Exercicio 9'+
              '\n17. Exercicio 10'+
              '\n18. Exercicio 11'+
              '\n19. Exercicio 12'+
              '\n20. Exercicio 13'+
              '\n21. Exercicio 14'+
              '\n22. Exercicio 15'+
              '\n23. Exercicio 16'+
              '\n24. Exercicio 17'+
              '\n25. Exercicio 18'+
              '\n26. Exercicio 19'+
              '\n27. Exercicio 20'+
              '\n ================SEGUNDA LISTA============='+
              '\n1(28). Exercicio 1'+
              '\n2(29). Exercicio 2'
              '\n3(30). Exercicio 3')




    def coletar(self):
        self.num1 = int(input('informe o primeiro numero'))
        self.num2 = int(input('informe o segundo numero'))

    def operacao(self):
        while self.opcao !=0:
            self.mostrarmenu()  # Chamando as opcões
            self.opcao = int(input('Escolha uma das opcoes acima: '))
            if self.opcao == 0:
                print('Obrigado!!!')
            if self.opcao == 1:
                self.coletar() #chamando o input por meio do coletar
                print(f'A soma dos números é: {self.opera.somar(self.num1, self.num2)}')
            elif self.opcao == 2:
                self.coletar()
                print(f'A subtracao dos numeros digitados é: `{self.opera.subtrair(self.num1, self.num2)}')
            elif self.opcao == 3:
                self.coletar()
                print(f'A multiplicação dos numeros digitados é:{self.opera.multiplicar(self.num1, self.num2)}')

            elif self.opcao == 4:
                self.coletar()
                print(f'A divisao dos numeros digitados é:{self.opera.dividir(self.num1, self.num2)}')
            elif self.opcao == 5:
                self.coletar()
                print(f'A potencia dos numeros digitados é:{self.opera.exercicio01(self.num1, self.num2)}')

            elif self.opcao == 6:
                self.coletar()
                print(f'A raiz de {self.num1} é :{self.opera.raiz(self.num1)}')
                print(f'A raiz de {self.num1} é :{self.opera.raiz(self.num2)}')

            elif self.opcao == 7:
                self.coletar()
                print(f'A tabuada de {self.num1} é: {self.opera.tabuada(self.num1)}')
                print(f'A tabuada de {self.num2} é: {self.opera.tabuada(self.num2)}')

            elif self.opcao == 8:
                print(f'Sequencia dos numero é: {self.opera.exercicio01()}')

            elif self.opcao == 9:
                print(f'Sequencia dos numeros é: {self.opera.exercicio02()}')

            elif self.opcao == 10:
                print(f'Sequencia dos numeros é: {self.opera.exercicio03()}')

            elif self.opcao == 11:
                print(f'Sequencia dos numeros é: {self.opera.exercicio04()}')

            elif self.opcao == 12:
                self.num1 = int(input('Digite um numero: '))
                print(f'O numero é: {self.opera.exercicio05(self.num1)}')

            elif self.opcao == 13:
                self.num1 = int(input('Digite um numero: '))
                print(f'O numero é: {self.opera.exercicio06(self.num1)}')

            elif self.opcao == 14:
                self.num1 = int(input('Digite um numero: '))
                print(f'Tabuada do numero informado: {self.opera.exercicio07(self.num1)}')

            elif self.opcao == 15:
                self.num1 = int(input('Digite um numero: '))
                print(f'A sequencia de numeros é: {self.opera.exercicio08(self.num1)}')

            elif self.opcao == 16:
                self.num1 = int(input('Digite um numero: '))
                print(f'A sequencia de numeros é: {self.opera.exercicio09(self.num1)}')

            elif self.opcao == 17:
                self.num1 = int(input('Digite um numero: '))
                print(f'A sequencia de numeros é: {self.opera.exercicio10(self.num1)}')

            elif self.opcao == 18:
                self.num1 = int(input('Digite um numero: '))
                print(f': {self.opera.exercicio11(self.num1)}')

            elif self.opcao == 19:
                self.num1 = int(input('Digite um numero: '))
                print(f': {self.opera.exercicio12(self.num1)}')

            elif self.opcao == 20:
                print(f': {self.opera.exercicio13()}')

            elif self.opcao == 21:
                self.num1 = int(input('Digite um numero: '))
                print(f'a soma dos : {self.opera.exercicio15(self.num1)}')

            elif self.opcao == 22:
                self.num1 = int(input('Digite um numero: '))
                print(f' {self.opera.exercicio16(self.num1)}')

            elif self.opcao == 23:
                self.num1 = int(input('Digite um numero: '))
                print(f' {self.opera.exercicio19(self)}')

            elif self.opcao == 28:
                self.num1 = int(input('Digite o salario: '))
                self.num2 = int(input('Digite o percentual de reajuste: '))
                print(f' {self.opera.exercicio26(self.num1,self.num2)}')

            elif self.opcao == 29:
                self.num1 = int(input('Digite o custo de fabrica: '))
                print(f'{self.opera.exercicio27(self.num1)}')

            elif self.opcao == 30:
                self.num1 = int(input('Primeira nota: '))
                self.num2 = int(input('segunda nota: '))
                self.num3 = int(input('terceira nota: '))
                print(f'{self.opera.exercicio28(self.num1,self.num2,self.num3)}')

            elif self.opcao == 31:
                self.num1 = int(input('Quantas maças vc ira comprar?: '))
                print(f'{self.opera.exercicio29(self.num1)}')

            elif self.opcao == 32:
                print(f'{self.opera.exercicio30()}')

            elif self.opcao == 33:
                self.num1 = int(input('Qual o seu salari?: '))
                self.num2 = int(input('Qual o total de vendas?: '))
                print(f'{self.opera.exercicio31(self.num1,self.num2)}')

            elif self.opcao == 34:
                self.num1 = int(input('Qual o saldo atual de sua conta?: '))
                self.num2 = int(input('Qual o debito de sua conta?: '))
                self.num3 = int(input('qual o credito de sua conta?: '))
                print(f'{self.opera.exercicio32(self.num1,self.num2,self.num3)}')

            elif self.opcao == 35:
                self.num1 = int(input('Informe um numero de 1 a 10: '))
                print(f'{self.opera.exercicio33(self.num1)}')

            elif self.opcao == 36:
                print(f'{self.opera.exercicio34(self.num1)}')



            else:
                print("Codigo incorreto")
