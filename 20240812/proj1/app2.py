from flask import Flask

class app2:
    #método contrutor
    def __init__(self):
    #aqui deve estar o código inicial da classe
        pass
    
    #métodos secundários
    #todo método deve ser como primeiro parâmetro
    #o indicador "self" --- isso mostra para o compilador que
    #este método faz parte do contexto da classe app2
    def saudacaoInicial(self):
        print("Bem vindo ao Python da massa")

    def escreva(self, texto):
        print(texto)


p = app2()
p.saudacaoInicial()
p.escreva('Este é o segundo exercicio em python 0.0.')
    