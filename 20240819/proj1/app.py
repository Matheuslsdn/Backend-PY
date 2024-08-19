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
        
        @self.app.route('/ativ3_submit', methods=['POST', 'GET'])
        def ativ3_submit():
            gen = request.form.get(gen)
            if gen == "F" or "f":
                return render_template('ativ3.html', dados= {'gen': 'Você é do sexo feminino'})
            elif gen == "M" or "m":
                return render_template('ativ3.html', dados= {'gen': 'Você é do sexo masculino'})
            else:
                return render_template('ativ3.html', dados= {'gen': 'O sexo não foi inserido'})
            
        #ativ 04
        @self.app.route('/ativ4')
        def ativ4():
            return render_template('ativ4.html')
        









if __name__ == '__main__':
    Meuapp = proj1()
    Meuapp.app.run(debug=True)