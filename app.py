import string
import random
import os
from flask import Flask, redirect, render_template, request

app = Flask(__name__, template_folder='templates')
url_mapping = {}

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/encurtar', methods=['POST'])
def encurtar():
    if request.method == 'POST':
        original_url = request.form['url']
        short_url = gerar_short_url()
        url_mapping[short_url] = original_url
        return render_template('encurtado.html', short_url=request.host_url + short_url)
    else:
        return redirect('/')

@app.route('/<short_url>', methods=['GET'])
def redirecionar(short_url):
    if short_url in url_mapping:
        original_url = url_mapping[short_url]
        return redirect(original_url)
    else:
        return render_template('nao_encontrado.html', short_url=short_url), 404

def gerar_short_url():
    caracteres = string.ascii_letters + string.digits
    tamanho = 6
    short_url = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return short_url

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
