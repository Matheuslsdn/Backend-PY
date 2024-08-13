from flask import Flask

class log1:
    def __init__(self):
        self.app = Flask(__name__)
        print("ola")
        self.setRotas()    

    def setRotas(self):
        @self.app.route('/')
        def hello():
            return "Hello, World!"


if __name__ == '__main__':
    Meuapp = log1()
    Meuapp.app.run()