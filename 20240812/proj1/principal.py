from flask import Flask
from app import proj1
from app2 import app2

#por causa da importação das linhas 2 e 3 essa classe consegue 
#instanciar e controlar os objetos gerados pelas classes proj1 e app2
class principal():
    def __init__(self):
        print('Bem vindo a classe principal. Ou será quem não!!!')

MeuApp = principal()
primeiro = proj1()
segundo = app2()
segundo.escreva("Consegui, Calaio")




