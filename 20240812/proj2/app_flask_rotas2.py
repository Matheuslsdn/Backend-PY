from flask import Flask

class app_flask_rotas2():
    def __init__(self):
        self.app = Flask(__name__)
        self.defineRotas()

    def defineRotas(self):
        @self.app.route("/")
        def rotaInicial():
            return "Essa é a página da rota INICIAL"
        
        @self.app.route("/exe01")
        def rotaExe01():
            return "<h1>Essa é a página da rota EXE01</h1>"
        
        @self.app.route("/exe02")
        def rotaExe02():
            return "<h2>Essa é a página da rota EXE02</h2>"
        
        
if __name__ == '__main__':
    Meuapp = app_flask_rotas2()
    Meuapp.app.run(debug=True)

