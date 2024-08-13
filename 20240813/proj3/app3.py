from flask import Flask, render_template, request

class proj3():
    def __init__(self):
        self.app = Flask(__name__)
        self.defineRotas()

    def defineRotas(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')
        
        @self.app.route('/form_submit', methods=['POST'])
        def form_submit():
            nome = request.form.get('nome')
            sobrenome = request.form.get('sobrenome')
            return f'Olá {nome} {sobrenome}'

        @self.app.route('/calc')
        def calc():
            return render_template('calc.html')
        
        @self.app.route('/calc_submit', methods=['POST'])
        def cacl_submit():
            num1 = request.form.get('num1')
            num2 = request.form.get('num2')
            num1 = num1.replace('.', '.')
            num2 = num2.replace('.', '.')
            soma = float(num1) + float(num2)
            soma = f'{soma:.2f}'
            soma = soma.replace(".", ",")
            return f'O valor da soma é {soma}'
        
        @self.app.route('/media')
        def media():
            return render_template('media.html')
        
        @self.app.route('/media_submit', methods=['POST'])
        def media_submit():
            nota1 = request.form.get('nota1')
            nota2 = request.form.get('nota2')
            nota3 = request.form.get('nota3')
            nota4 = request.form.get('nota4')
            nota1 = nota1.replace('.', '.')
            nota2 = nota2.replace('.', '.')
            nota3 = nota3.replace('.', '.')
            nota4 = nota4.replace('.', '.')
            media = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) / 4
            media = f'{media:.2f}'
            media = media.replace(".", ",")
            return f'A média é {media}'
        
        @self.app.route('/trans')
        def transforme():
            return render_template('transforme.html')
        
        @self.app.route('/transforme_submit', methods=['POST'])
        def transforme_submit():
            metros = request.form.get('metros')
            metros = metros.replace('.', '.')
            metros = float(metros)
            metros = metros * 100
            return f'O valor em centímetros é {metros: .0f}'
        
        

if __name__ == '__main__':
    Meuapp2 = proj3()
    Meuapp2.app.run(debug=True)