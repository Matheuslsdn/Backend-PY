from flask import Flask, render_template, request

#desafio do 6 ao 15
class proj2():
    def __init__(self):
        self.app = Flask(__name__)
        self.rotas()
    
    def rotas(self):
        #atividade 06
        @self.app.route('/')
        def index():
            return render_template('index.html')
        
        @self.app.route('/form_submit', methods=['POST'])
        def form_submit():
            nome = request.form.get('nome')
            sobrenome = request.form.get('sobrenome')
            return render_template('index.html', dados={'nome':nome, 'sobrenome': sobrenome})
        
        #atividade 07
        @self.app.route('/calc')
        def calc():
            return render_template('calc.html')
        
        @self.app.route('/calc_submit', methods=['POST', 'GET'])
        def cacl_submit():
            num1 = request.form.get('num1')
            num2 = request.form.get('num2')
            num1 = num1.replace('.', '.')
            num2 = num2.replace('.', '.')
            soma = float(num1) + float(num2)
            soma = f'{soma:.2f}'
            soma = soma.replace(".", ",")
            return render_template('calc.html', dados={'num1': num1, 'num2': num2, 'soma': soma})
        
        #atividade 08
        @self.app.route('/media')
        def media():
            return render_template('media.html')
        
        @self.app.route('/media_submit', methods=['POST', 'GET'])
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
            return render_template('media.html', dados= media)
        
        #atividade 09
        @self.app.route('/trans')
        def transforme():
            return render_template('transforme.html')
        
        @self.app.route('/transforme_submit', methods=['POST', 'GET'])
        def transforme_submit():
            metros = request.form.get('metros')
            metros = metros.replace('.', '.')
            metros = float(metros)
            metros = metros * 100
            return render_template('transforme.html', dados= metros)
        
        #atividade 10
        @self.app.route('/area')
        def area():
            return render_template('area.html')
        
        @self.app.route('/area_submit', methods=['POST', 'GET'])
        def area_submit():
            base = request.form.get('base')
            altura = request.form.get('altura')
            base = base.replace('.', '.')
            altura = altura.replace('.', '.')
            base = float(base)
            altura = float(altura)
            quadrado = base * altura
            quadrado = f'{quadrado:.2f}'
            quadrado = quadrado.replace(".", ",")
            cubo = base ** 3
            cubo = f'{cubo:.2f}'
            cubo = cubo.replace(".", ",")
            return render_template('area.html', dados={'quadrado': quadrado, 'cubo': cubo})

        #atividade 11
        @self.app.route('/texto')
        def texto():
            return render_template('texto.html')  

        @self.app.route('/texto_submit', methods=['POST', 'GET']) 
        def tamanho():
            texto = request.form.get('texto')
            tamanho = texto(len)
            return render_template('texto.html', dados=tamanho)



if __name__ == '__main__':
    Meuapp = proj2()
    Meuapp.app.run(debug=True)