from flask import Flask, render_template, request

class proj1:
    def __init__(self):
        self.app = Flask(__name__)

        #rota inicial
        @self.app.route('/')
        def index():
            return render_template('index.html')
        
        #--------------------------------------
        @self.app.route('/exe01')
        def exe01():
            return "Início do e xercicio 01"
        
        #rota que recebe dados do front-end 'index.html'
        @self.app.route('/submit',methods=['POST'])
        def submit():
            nome = request.form.get('nome')
            return f'seu nome é {nome}'
        #--------------------------------------
        @self.app.route('/exe02')
        def exe02():
            return render_template('/exe02.html')
            
        @self.app.route('/exe02_submit', methods=['POST'])
        def calculo():
            valor1 = request.form.get('valor1')
            valor2 = request.form.get('valor2')
            soma = int(valor1) + int(valor2)
            return f' a soma dos valores é de {soma}.'
        
        @self.app.route('/exe03')
        def exe03():
            return render_template('/exe03.html')
        
        @self.app.route('/exe03_submit', methods=['POST'])
        def imprime():
            nome = request.form.get('nome')
            sobrenome = request.form.get('sobrenome')
            return f'seu nome é {nome} {sobrenome}'
        
        @self.app.route('/exe04')
        def exe04():
            return render_template('/exe04.html')
            
        @self.app.route('/exe04_submit', methods=['POST'])
        def media():
            nota1 = request.form.get('nota1')
            nota2 = request.form.get('nota2')
            nota3 = request.form.get('nota3')
            nota4 = request.form.get('nota4')
            media = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) / 4
            return f' a média das notas é {media}.'

if __name__ == '__main__':
    MeuApp = proj1()
    MeuApp.app.run(debug = True)
