from flask import Flask, render_template, request

class proj1():
    def __init__(self):
        self.app = Flask(__name__)
        self.rotas()

    def rotas(self):
        @self.app.route('/')
        def inicio():
            return render_template('index.html')
        
        @self.app.route('/contact')
        def form():
            return render_template('contact.html')
        
        @self.app.route('/contact_submit', methods=['POST', 'GET'])
        def rotacontact_submit():
            nome = request.form.get('nome')
            return render_template('contact.html', dados= nome)
        

if __name__ == '__main__':
    Meuapp = proj1()
    Meuapp.app.run(debug=True)