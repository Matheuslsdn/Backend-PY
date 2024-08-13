from flask import Flask

class app_flask_rotas():
    def __init__(self):
        self.app = Flask(__name__)
        #O comando abaixo identifica quando a rota inicial é ativada. 
        @self.app.route('/')
        def rotanicial():
            return "Essa é a página da rota inicial."
        

if __name__ == '__main__':
    Meuapp = app_flask_rotas()
    Meuapp.app.run(debug=True)
