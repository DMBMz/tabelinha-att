from flask import app, Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    number = None
    numbers = []
    if request.method == "POST":
        number = int(request.form["number"])
        numbers = [number + 1, number + 2, number + 3, number + 4]
    return render_template("home.html", numbers=numbers)


@app.route('/personalizada')
def home_perso():
    usu = 'PASTEL DE COXINHA'
    # Para ler dados do BD ou csv (usar pandas)
    # criar a variável com os dados da lista
    # enviar para a aplicação de modo similar.
    return render_template('home_personalizada.html', usuario=usu)

if __name__ == '__main__':
    app.run('0.0.0.0')
