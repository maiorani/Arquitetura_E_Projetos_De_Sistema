import abc  #importar abstract method
from unittest import TestCase, main #import de testes unitarios 


#opçoes de operaçoes
class Operacao (metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def doit(self, numero_1, numero_2):
        pass

class Soma (Operacao):
    def doit(self, numero_1, numero_2):
        resultado=numero_1 + numero_2
        return resultado

class Subtracao (Operacao):
    def doit(self, numero_1, numero_2):
        resultado=numero_1 - numero_2
        return resultado

class Multiplicacao (Operacao):
    def doit(self, numero_1, numero_2):
        resultado=numero_1 * numero_2
        return resultado

class Divisao (Operacao):
    def doit(self, numero_1, numero_2):
        resultado=numero_1 / numero_2
        return resultado


#opçoes de operadores(sinais)
class Operadores (object):
    def operar(self, operacao):
        if(operacao =='soma'):
            return Soma()
        elif(operacao == 'subtracao'):
            return Subtracao()
        elif(operacao == 'multiplicacao'):
            return Multiplicacao()
        elif(operacao == 'divisao'):
            return Divisao()

#definicao da calculadora
class Calc():
    def calcular(self, numero_1, numero_2, operacao):
        operadores = Operadores()
        operacao = operadores.operar(operacao)
        if(operacao == None):
            return 0
        else:
            resultado = operacao.doit(numero_1, numero_2)
            return resultado

#bateria de testes
class Testes (TestCase):
    def teste_soma(self):
        testesoma = Calc()
        resultado = testesoma.calcular(25,0,'soma')
        self.assertEqual(resultado, 25)    
        print ("OK_01_SOMA")

    def teste_subtracao(self):
        testesub = Calc()
        resultado = testesub.calcular(37,7,'subtracao')
        self.assertEqual(resultado, 30)        
        print ("OK_02_SUB")
    def teste_multiplicacao(self):
        testemulti = Calc()
        resultado = testemulti.calcular(7,7,'multiplicacao')
        self.assertEqual(resultado, 49)
        print ("OK_03_MULTI")
    
    def teste_divisao(self):
        testediv = Calc()
        resultado = testediv.calcular(1000,100, 'divisao')
        self.assertEqual(resultado, 10)
        print ("OK_04_DIV")
 

 # chamada do main
if __name__ == '__main__':  
    main()

