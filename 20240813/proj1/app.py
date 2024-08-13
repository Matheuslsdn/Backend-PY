from flask import Flask, render_template

class proj1():
    def __init__(self):
        self.app = Flask(__name__)
        self.defineRotas()

    def defineRotas(self):
        @self.app.route('/')
        def rotaInicial():
            return render_template('index.html')
        


if __name__ == '__main__':
    Meuapp = proj1()
    Meuapp.app.run(debug=True)
    


