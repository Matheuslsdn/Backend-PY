from flask import Flask, render_template, request

class proj2():
    def __init__(self):
        self.app = Flask(__name__)
        self.defineRotas()

    def defineRotas(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')
        
        @self.app.route('/exe01')
        def exe01():
            return render_template('exe01.html')
        
        @self.app.route('/form_submit', methods=['POST'])
        def form_submit():
            nome = request.form.get('nome')
            return f'Olá {nome}'
        

if __name__ == '__main__':
    Meuapp1 = proj2()
    Meuapp1.app.run(debug=True)