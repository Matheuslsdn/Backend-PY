from flask import Flask, render_template

class proj3():
    def __init__(self):
        self.app = Flask(__name__)
        @self.app.route('/')
        def rotainicial():
            return render_template('index.html')
        
        @self.app.route('/exe01')
        def exe01():
            return render_template('exe01.html')
        
        @self.app.route('/exe02')
        def exe02():
            return render_template('exe02.html')
        

if __name__ == '__main__':
    Meuapp = proj3()
    Meuapp.app.run(debug=True)