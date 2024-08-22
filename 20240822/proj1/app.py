from flask import Flask, render_template, request, redirect

class proj1():
    def __init__(self):
        self.app = Flask(__name__)
        self.Rotas()

    def Rotas(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')
        
        #ativ 01
        @self.app.route('/ativ1')
        def ativ1():
            return render_template('ativ1.html')
        
        @self.app.route('/ativ1_submit', methods=['POST', 'GET'])
        def ativ1_submit():
            num1 = request.form.get('num1')
            while True:
                if num1 is None:
                    return render_template('ativ1.html', mensagem='Não foi possível obter o número')
                num1 = int(num1)
                if num1 <= 0:
                    return render_template('ativ1.html', mensagem='Número inválido. Tente novamente.')
                elif num1 > 10:
                    return render_template('ativ1.html', mensagem='Número inválido. Tente novamente.')
                else:
                    return render_template('ativ1.html', mensagem='Finalmente um número válido')
                    break

        #ativ 02
        @self.app.route('/ativ2')
        def ativ2():
            return render_template('ativ2.html')
        
        @self.app.route('/ativ2_submit', methods=['POST', 'GET'])
        def ativ2_submit():
            nome = "Pedro"
            senha = "12345678"
            usuario = request.form.get('usuario')
            senha_usuario = request.form.get('senha')

            if usuario is None or senha_usuario is None:
                return render_template('ativ2.html', mensagem='Não foi possível obter o usuário ou senha')
            elif usuario != nome:
                return render_template('ativ2.html', mensagem='Usuário inválido')
            elif senha_usuario != senha:
                return render_template('ativ2.html', mensagem='Senha inválida')
            else:
                return redirect('/')
            
        #ativ 03
        @self.app.route('/ativ3')
        def ativ3():
            return render_template('ativ3.html')
        
        @self.app.route('/ativ3_submit', methods=['POST', 'GET'])
        def ativ3_submit():
            num1 = request.form.get('num1')
            num2 = request.form.get('num2')
            num1 = int(num1)
            num2 = int(num2)
            menor = min(num1, num2)
            maior = max(num1, num2)
            numeros = list(range(menor + 1, maior))
            return render_template('ativ3.html', dados= numeros)
        
        #ativ 04
        @self.app.route('/ativ4')
        def ativ4():
            return render_template('ativ4.html')
        
        @self.app.route('/ativ4_submit', methods=['POST', 'GET'])
        def ativ4_submit():
            num1 = request.form.get('num1')
            num2 = request.form.get('num2')
            num1 = int(num1)
            num2 = int(num2)
            menor = min(num1, num2)
            maior = max(num1, num2)
            soma = sum(range(menor, maior + 1))
            return render_template('ativ4.html', soma= soma)
        
            

            


            


        

if __name__ == '__main__':
    Meuapp = proj1()
    Meuapp.app.run(debug=True)