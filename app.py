from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id':1,
        'titulo' : 'O príncipe',
        'autor' : 'Nicolau Maquiavel'
    },
    {
        'id':2,
        'titulo' : 'Dom casmurro',
        'autor' : 'Machado de Assis'
    },
    {
        'id':3,
        'titulo' : 'Memorias postumas de Brás Cubas',
        'autor' : 'Machado de Assis'
    },
]

@app.route('/')
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['GET'])
def obter_por_id(id):
    for livro in livros:
       if livro.get('id') == id:
        return jsonify(livro)
    
if __name__ == '__main__':
    app.run(port=5001, host='127.0.0.1', debug=True)
    
