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
                escolha = request.form['escolha']
                produtos = {
                    "produto1": {"nome": "Dog-frango", "preco": 14.90},
                    "produto2": {"nome": "Dog-calabresa", "preco": 14.90},
                    "produto3": {"nome": "Dog-tudo", "preco": 19.90}
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

        #ativ 09
        @self.app.route('/ativ9')
        def ativ9():
            return render_template('ativ9.html')
        
        @self.app.route('/ativ9_submit', methods=['POST', 'GET'])
        def ativ9_submit():
            num1 = request.form.get('num1')
            num2 = request.form.get('num2')
            num3 = request.form.get('num3')
            num1 = float(num1.replace(',', '.'))
            num2 = float(num2.replace(',', '.'))
            num3 = float(num3.replace(',', '.'))
    
            numeros = [num1, num2, num3]
            numeros.sort(reverse=True)
    
            return render_template('ativ9.html', dados={'num1': numeros[0], 'num2': numeros[1], 'num3': numeros[2]})
        
        #ativ 10
        @self.app.route('/ativ10')
        def ativ10():
            return render_template('ativ10.html')
        
        @self.app.route('/ativ10_submit', methods=['POST', 'GET'])
        def ativ10_submit():
            num1 = request.form.get('num1')
            num2 = request.form.get('num2')
            num3 = request.form.get('num3')
            num1 = float(num1.replace(',', '.'))
            num2 = float(num2.replace(',', '.'))
            num3 = float(num3.replace(',', '.'))
    
            numeros = [num1, num2, num3]
            numeros.sort()
    
            return render_template('ativ10.html', dados={'num1': numeros[0], 'num2': numeros[1], 'num3': numeros[2]})
        
        #ativ 11
        @self.app.route('/ativ11')
        def ativ11():
            return render_template('ativ11.html')
        
        @self.app.route('/ativ11_submit', methods=['POST', 'GET'])
        def ativ11_submit():
            m = "manha"
            t = "tarde"
            n = "noite"
            escolha = request.form.get('turno')
            if escolha == 'm':
                return render_template('ativ11.html', dados={'turno': 'Bom dia'})
            elif escolha == 't':
                return render_template('ativ11.html', dados={'turno': 'Boa tarde'})
            elif escolha == 'n':
                return render_template('ativ11.html', dados={'turno': 'Boa noite'})
            else:
                return render_template('ativ11.html', dados={'turno': 'turno invalido'})
            
        #ativ 12
        @self.app.route('/ativ12')
        def ativ12():
            return render_template('ativ12.html')
        
        @self.app.route('/ativ12_submit', methods=['POST', 'GET'])
        def ativ12_submit():
            lado1 = request.form.get('lado1')
            lado2 = request.form.get('lado2')
            lado3 = request.form.get('lado3')
            lado1 = int(lado1)
            lado2 = int(lado2)
            lado3 = int(lado3)
            if lado1 == lado2 and lado1 == lado3:
                return render_template('ativ12.html', dados={'resultado': 'Equilatero'})
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                return render_template('ativ12.html', dados={'resultado': 'Isosceles'})
            elif lado1 != lado2 or lado2 != lado3 or lado1 != lado3:
                return render_template('ativ12.html', dados={'resultado': 'Escaleno'})
            else:
                return render_template('ativ12.html', dados={'resultado': 'Invalido'})
            
        #ativ 13
        @self.app.route('/ativ13')
        def ativ13():
            return render_template('ativ13.html')
        
        @self.app.route('/ativ13_submit', methods=['POST', 'GET'])
        def ativ13_submit():
            if request.method == 'POST':
                nome = request.form.get('nome')
                salario = request.form.get('salario')
                salario = float(salario.replace(',', '.'))
                reajuste = ['20', '15', '10', '5']
                if salario <= 280: 
                    novo_salario = salario + (salario * 0.20)
                    diferenca = novo_salario - salario
                    return render_template('ativ13.html', dados={'nome': nome, 'salario': salario, 'reajuste': '20%', 'novo_salario': novo_salario, 'diferenca': diferenca})
                elif salario > 280 and salario <= 700:
                    novo_salario = salario + (salario * 0.15)
                    diferenca = novo_salario - salario
                    return render_template('ativ13.html', dados={'nome': nome, 'salario': salario,'reajuste': reajuste[1] + '%', 'novo_salario': novo_salario, 'diferenca': diferenca})
                elif salario > 700 and salario <= 1500:
                    novo_salario = salario + (salario * 0.10)
                    diferenca = novo_salario - salario
                    return render_template('ativ13.html', dados={'nome': nome, 'salario': salario,'reajuste': reajuste[2] + '%', 'novo_salario': novo_salario, 'diferenca': diferenca})
                elif salario > 1500:
                    novo_salario = salario + (salario * 0.05)
                    diferenca = novo_salario - salario
                    return render_template('ativ13.html', dados={'nome': nome, 'salario': salario,'reajuste': reajuste[3] + '%', 'novo_salario': novo_salario, 'diferenca': diferenca})
                else:
                    return render_template('ativ13.html', dados= 'informações inválidas')

        


            





if __name__ == '__main__':
    Meuapp = proj1()
    Meuapp.app.run(debug=True)