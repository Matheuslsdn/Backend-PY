from flask import Flask, render_template, request

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
            num_list = []
            for i in range(4):  
                num = request.form.get(f'num_{i+1}')  
                if num:
                    num = num.replace(',', '.')
                    num_list.append(float(num))
    
            if num_list:
                max_num = max(num_list)
                return render_template('ativ1.html', dados= {'max_num': max_num, 'num_list': num_list})
            else:
                return render_template('ativ1.html', dados= {'msg': 'nenhum número foi inserido'})
            
        #ativ 02
        @self.app.route('/ativ2')
        def ativ2():
            return render_template('ativ2.html')
        
        @self.app.route('/ativ2_submit', methods=['POST', 'GET'])
        def ativ2_submit():
            num1 = request.form.get('num1')
            num1 = num1.replace(',', '.')
            num1 = float(num1)
            if num1 > 0:
                num1 = float(num1)
                return render_template('ativ2.html', dados= {'num1': 'Positivo'})
            elif num1 < 0:
                num1 = float(num1)
                return render_template('ativ2.html', dados= {'num1': 'Negativo'})
            else:
                return render_template('ativ2.html', dados= {'num1': 'Zero ou não foi inserido'})
            
        #ativ 03
        @self.app.route('/ativ3')
        def ativ3():
            return render_template('ativ3.html')
        
        @self.app.route('/ativ3_submit', methods=['POST'])
        def ativ3_submit():
            genero = request.form.get('genero')
            if genero.lower() == "f":
                return render_template('ativ3.html', dados={'genero': 'Você é do sexo feminino'})
            elif genero.lower() == "m":
                return render_template('ativ3.html', dados={'genero': 'Você é do sexo masculino'})
            else:
                return render_template('ativ3.html', dados={'genero': 'O sexo não foi inserido'})
        
        #ativ 04
        @self.app.route('/ativ4')
        def ativ4():
            return render_template('ativ4.html')
            
        @self.app.route('/ativ4_submit', methods=['POST', 'GET'])
        def ativ4_submit():
            letra = request.form.get('letra')
            if letra.lower() in 'aeiou':
                return render_template('ativ4.html', dados={'letra': 'Vogal'})
            elif letra.lower() in 'bcdfghjklmnpqrstvwxyz':
                return render_template('ativ4.html', dados={'letra': 'Consoante'})
            else:
                return render_template('ativ4.html', dados={'letra': 'Não foi inserido uma letra'})
            
        #ativ 05
        @self.app.route('/ativ5')
        def ativ5():
            return render_template('ativ5.html')
        
        @self.app.route('/ativ5_submit', methods=['POST', 'GET'])
        def ativ5_submit():
            nota1 = request.form.get('nota1')
            nota2 = request.form.get('nota2')
    
            if not nota1 or not nota2:
                return render_template('ativ5.html', dados={'erro': 'Preencha todos os campos'})
    
            nota1 = nota1.replace(',', '.')
            nota2 = nota2.replace(',', '.')
    
            if nota1.replace('.', '', 1).isdigit() and nota2.replace('.', '', 1).isdigit():
                nota1 = float(nota1)
                nota2 = float(nota2)
                if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
                    media = (nota1 + nota2) / 2
                    if media >= 7:
                        return render_template('ativ5.html', dados={'media': 'Aprovado'})
                    else:
                        return render_template('ativ5.html', dados={'media': 'Reprovado'})
                else:
                    return render_template('ativ5.html', dados={'media': 'Nota inválida'})
            else:
                return render_template('ativ5.html', dados={'media': 'Nota inválida'})

        #ativ 06
        @self.app.route('/ativ6')
        def ativ6():
            return render_template('ativ6.html')
        
        @self.app.route('/ativ6_submit', methods=['POST', 'GET'])
        def ativ6_submit():
            num1 = request.form.get('num1')
            num2 = request.form.get('num2')
            num3 = request.form.get('num3')

            if not num1 or not num2 or not num3:
                return render_template('ativ6.html', dados={'maior': 'Preencha todos os campos'})

            num1 = float(num1.replace(',', '.'))
            num2 = float(num2.replace(',', '.'))
            num3 = float(num3.replace(',', '.'))

            maior = max(num1, num2, num3)
            if num1 == num2 == num3:
                return render_template('ativ6.html', dados={'maior': 'Os números são iguais'})
            else:
                return render_template('ativ6.html', dados={'maior': maior})
            
        #ativ 07
        @self.app.route('/ativ7')
        def ativ7():
            return render_template('ativ7.html')
        
        @self.app.route('/ativ7_submit', methods=['POST', 'GET'])
        def ativ7_submit():
            num1 = request.form.get('num1')
            num2 = request.form.get('num2')
            num3 = request.form.get('num3')
            num4 = request.form.get('num4')

            if not num1 or not num2 or not num3 or not num4:
                return render_template('ativ7.html', notify='Preencha todos os campos')
            
            num1 = float(num1.replace(',', '.'))
            num2 = float(num2.replace(',', '.'))
            num3 = float(num3.replace(',', '.'))
            num4 = float(num4.replace(',', '.'))

            maior = max(num1, num2, num3, num4)
            menor = min(num1, num2, num3, num4)
            if num1 == num2 == num3 == num4:
                return render_template('ativ7.html', igual='Os números são iguais')
            else:
                return render_template('ativ7.html', dados={'maior': maior, 'menor': menor})
            
        #ativ 08
        @self.app.route('/ativ8')
        def ativ8():
            return render_template('ativ8.html')
        
        @self.app.route('/ativ8_submit', methods=['POST', 'GET'])
        def ativ8_submit():
            if request.method == 'POST':
                escolha = request.form.get('escolha')
                produto1 = request.form.get('produto1')
                produto2 = request.form.get('produto2')
                produto3 = request.form.get('produto3')
                preco1 = float(request.form.get('preco1').replace(',', '.'))
                preco2 = float(request.form.get('preco2').replace(',', '.'))
                preco3 = float(request.form.get('preco3').replace(',', '.'))

                produtos = {
                    "produto1": {"nome": produto1, "preco": preco1},
                    "produto2": {"nome": produto2, "preco": preco2},
                    "produto3": {"nome": produto3, "preco": preco3}
                }

                if escolha:
                    for produto in produtos.values():
                        if produto['nome'] == escolha:
                            return render_template('ativ8.html', mensagem=f"Você escolheu {produto['nome']} por R$ {produto['preco']:.2f}")
                    return render_template('ativ8.html', erro='Produto não encontrado')
                else:
                    return render_template('ativ8.html', erro='Selecione um produto')
            else:
                return render_template('ativ8.html')

            





if __name__ == '__main__':
    Meuapp = proj1()
    Meuapp.app.run(debug=True)