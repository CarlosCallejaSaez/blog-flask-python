from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


blog_posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        blog_posts.append({'titulo': titulo, 'contenido': contenido})
        return redirect(url_for('index'))
    return render_template('agregar.html')

if __name__ == '__main__':
    app.run(debug=True)
