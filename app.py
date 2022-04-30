from flask import Flask, render_template, request, url_for

app = Flask(__name__)
app.config.update(
    DEBUG = True,
    ENV = 'development'
    )

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/perfil', methods=['GET','POST'])
def perfil():
    name = request.form.get('nombre')
    surename = request.form.get('apellido')
    username = request.form.get('username')
    birthday = request.form.get('birthday')
    email = request.form.get('email')
    cellphone = request.form.get('telefono')
    bibliography = request.form.get('biografia')
    context = {
            'name': name,
            'surename': surename,
            'username': username,
            'birthday': birthday,
            'email': email,
            'cellphone': cellphone,
            'bibliography': bibliography
    }
    return render_template('perfil.html', **context)

if __name__=='__main__':
    app.run(host='127.0.0.1', port=8000)
