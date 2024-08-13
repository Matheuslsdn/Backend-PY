from flask import Flask

class app_flask():
    def __init__(self):
        self.app = Flask(__name__)
        print("Primeiro projeto python flask")

if __name__ == '__main__':
    Meuapp = app_flask()
    Meuapp.app.run(debug=True)

