from flask import Flask, render_template, request

class proj4():
    def __init__(self):
        self.app = Flask(__name__)
        self.rotas()

    def rotas(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')
        
        @self.app.route('/form1_submit', methods=['POST'])
        def form1_submit():
            nome = request.form.get('nome')
            return f'Olá {nome}'



if __name__ == '__main__':
    Meuapp4 = proj4()
    Meuapp4.app.run(debug=True)