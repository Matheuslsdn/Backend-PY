from flask import Flask, render_template, request, redirect

class proj1():
    def __init__(self):
        self.app = Flask(__name__)
        self.Rotas()
    #função atividade 8
    #sempre que for criar uma função, você sempre deve colocar o self como o primeiro parametro e depois você deve colocar antes das rotas para que a função seja devidamente chamada.
    #nessa função da atividade 8 eu estou verificando se o numero é primo, ou seja se o numero é < ou = a 1 ele já retorna falso, e se 
    def eh_primo(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
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

        #ativ 05
        @self.app.route('/ativ5')
        def tabuada():
            return render_template('ativ5.html')
        
        @self.app.route('/ativ5_submit', methods=['POST', 'GET'])
        def ativ5_submit():
            num = request.form.get('num')
            tabuada = []
            for i in range(1, 11):
                tabuada.append(f'{num} x {i} = {int(num) * i}')
    
            return render_template('ativ5.html', tabuada=tabuada)

        #ativ 06
        @self.app.route('/ativ6')
        def ativ6():
            return render_template('ativ6.html')
        
        @self.app.route('/ativ6_submit', methods=['POST', 'GET'])
        def ativ6_submit():
            if request.method == 'POST':
                numeros = [int(request.form.get(f'num{i}')) for i in range(1, 7)]
        
                # Inicializando variáveis
                multiplicacao_positivos = 1
                soma_negativos = 0
                contagem_zeros = 0

                for numero in numeros:
                    if numero > 0:
                        multiplicacao_positivos *= numero
                    elif numero < 0:
                        soma_negativos += numero
                    else:
                        contagem_zeros += 1

                return render_template('ativ6.html', 
                               multiplicacao_positivos=multiplicacao_positivos, 
                               soma_negativos=soma_negativos, 
                               contagem_zeros=contagem_zeros)
            return render_template('ativ6.html')

        #ativ 07
        @self.app.route('/ativ7')
        def ativ7():
            return render_template('ativ7.html')
        
        @self.app.route('/ativ7_submit', methods=['POST', 'GET'])
        def ativ7_submit():
            palavra = request.form.get('palavra')
            contador = 0
            for letra in palavra:
                if letra.isalpha():
                    contador += 1
                
            return render_template('ativ7.html', contador= contador)
        
        #ativ 08
        @self.app.route('/ativ8')
        def ativ8():
            return render_template('ativ8.html')

        @self.app.route('/ativ8_submit', methods=['POST', 'GET'])
        def ativ8_submit():
            numeros = []
            for i in range(1, 9):
                numero = request.form.get(f'numero{i}')
                if numero:
                    numeros.append(int(numero))

            pares = [n for n in numeros if n % 2 == 0]
            impares = [n for n in numeros if n % 2 != 0]
            primos = [n for n in numeros if self.eh_primo(n)]

            soma_impares = sum(impares)
            mult_primos = 1
            for primo in primos:
                mult_primos *= primo                

                return render_template('ativ8.html', numeros=numeros, pares=pares, impares=impares, primos=primos, soma_impares=soma_impares, mult_primos=mult_primos)

        #ativ 09
        @self.app.route('/ativ9')
        def ativ9():
            return render_template('ativ9.html')
        
        @self.app.route('/ativ9_submit', methods=['POST', 'GET'])
        def ativ9_submit():
            frase = request.form.get('frase')
            frase = frase.lower()
            vogais = 'aeiouãõáóéí'
            contador = 0
            for letra in frase:
                if letra in vogais:
                    contador += 1
            return render_template('ativ9.html', frase= frase, contador_vogais= contador)
            
        #ativ 10
        @self.app.route('/ativ10')
        def ativ10():
            return render_template('ativ10.html')
        
        @self.app.route('/ativ10_submit', methods=['GET', 'POST'])
        def ativ10_submit():
            if request.method == 'POST':
                quantidade = int(request.form.get('quantidade'))
                numeros = {float(request.form.get(f'numero{i}')) for i in range(quantidade)}
                menor_valor = min(numeros)
                maior_valor = max(numeros)
                soma = sum(numeros)
                return render_template('ativ10.html', menor_valor=menor_valor, maior_valor=maior_valor, soma=soma)
            return render_template('ativ10.html')
        
        #ativ 11



            


            


        

if __name__ == '__main__':
    Meuapp = proj1()
    Meuapp.app.run(debug=True)
