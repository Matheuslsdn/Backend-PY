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
            tamanho = len(texto.strip())
            return render_template('texto.html', dados=tamanho, texto=texto)
        
        #atividade 12
        @self.app.route('/calchoras')
        def calc2():
            return render_template('calchoras.html')

        @self.app.route('/calchoras_submit', methods=['POST', 'GET'])
        def calcsalario():
            horas = request.form.get('horas')
            valor = request.form.get('valor')
            horas = horas.replace(',', '.')
            valor = valor.replace(',', '.')
            horas = float(horas)
            valor = float(valor)
            salario = horas * valor
            salario = f'{salario:.2f}'
            salario = salario.replace(".", ",")
            return render_template('calchoras.html', dados={'salario':salario, 'horas':horas, 'valor':valor})
        
        #atividade 13
        @self.app.route('/calcgasto')
        def calc3():
            return render_template('calcgasto.html')
        
        @self.app.route('/calcgasto_submit', methods=['POST', 'GET'])
        def calcgasto():
            gasolina = request.form.get('gasolina')
            distancia = request.form.get('distancia')
            consumo = request.form.get('consumo')
            gasolina = gasolina.replace(',', '.')
            distancia = distancia.replace(',', '.')
            consumo = consumo.replace(',', '.')
            gasolina = float(gasolina)
            distancia = float(distancia)
            consumo = float(consumo)
            gasto = (distancia / consumo) * gasolina
            gasto = f'{gasto:.2f}'
            gasto = gasto.replace(".", ",")
            return render_template('calcgasto.html', dados={'gasto':gasto,
                'gasolina':gasolina,'distancia':distancia,'consumo':consumo})
                                                            
        #atividade 14
        @self.app.route('/idade')
        def idadeDias():
            return render_template('idade.html')

        @self.app.route('/idade_submit', methods=['POST', 'GET'])
        def calc4():
            anos = request.form.get('anos')
            meses = request.form.get('meses')
            dias = request.form.get('dias')
            anos = anos.replace(',', '.')
            meses = meses.replace(',', '.')
            dias = dias.replace(',', '.')
            anos = int(anos)
            meses = int(meses)
            dias = int(dias)
            totalDias = anos * 365 + meses * 30 + dias
            totalDias = f'{totalDias}'
            return render_template('idade.html', dados={'totalDias':totalDias, 
                                    'anos':anos, 'meses':meses, 'dias':dias})

        #atividade 15
        @self.app.route('/salario')
        def salario():
            return render_template('salario.html')
        
        @self.app.route('/salario_submit', methods=['POST', 'GET'])
        def calc5():
            salarioMin = request.form.get('salarioMin')
            salarioGanho = request.form.get('salarioGanho')
            salarioMin = salarioMin.replace(',', '.')
            salarioGanho = salarioGanho.replace(',', '.')
            salarioMin = float(salarioMin)
            salarioGanho = float(salarioGanho)
            salario = salarioGanho / salarioMin
            salario = f'{salario:.2f}'
            salario = salario.replace(',', '.')
            return render_template('salario.html', dados={'salario':salario,
                        'salarioMin':salarioMin, 'salarioGanho':salarioGanho})

        #atividade 16
        @self.app.route('/arquivo')
        def arquivoMb():
             return render_template('arquivo.html')

        @self.app.route('/arquivo_submit', methods=['POST', 'GET'])
        def calc6():
            arquivo = request.form.get('arquivo')
            velocidade = request.form.get('velocidade')
            arquivo = arquivo.replace(',', '.')
            velocidade = velocidade.replace(',', '.')
            arquivo = float(arquivo)
            velocidade = float(velocidade)
            tempo = arquivo / velocidade
            tempo = f'{tempo:.2f}'
            tempo = float(tempo)
            minutos = tempo / 60
            minutos = f'{minutos:.2f}'
            minutos = minutos.replace(',', '.')
            return render_template('arquivo.html', dados={'tempo':tempo,
            'arquivo':arquivo, 'velocidade':velocidade, 'minutos':minutos})
        
        #atividade 17
        @self.app.route('/peso')
        def pesoIdeal():
            return render_template('peso.html')
        
        @self.app.route('/peso_submit', methods=['POST', 'GET'])
        def calc7():
            altura = request.form.get('altura')
            peso = request.form.get('peso')
            altura = altura.replace(',', '.')
            peso = peso.replace(',', '.')
            altura = float(altura)
            peso = float(peso)
            pesoatual = peso / (altura * 2)
            pesoatual = f'{pesoatual:.2f}'
            pesoatual = pesoatual.replace(',', '.')
            pesoIdeal = (72.7 * altura) - 58
            pesoIdeal = f'{pesoIdeal:.2f}'
            pesoIdeal = pesoIdeal.replace(',', '.')
            return render_template('peso.html', dados={'pesoIdeal':pesoIdeal, 
                        'peso':peso, 'altura':altura, 'pesoatual':pesoatual})


if __name__ == '__main__':
    Meuapp = proj2()
    Meuapp.app.run(debug=True)