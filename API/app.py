from flask import Flask, jsonify, request, render_template
from database import inicializar_banco

inicializar_banco()

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

#puxar um livro

@app.route('/')
def incio():
    return render_template("index.html")
    
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#puxar um livro por id 

@app.route('/livros/<int:id>',methods=['GET'])
def obter_por_id(id):
    for livro in livros:
       if livro.get('id') == id:
        return jsonify(livro)
    
#editar um livro

@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    request.get_json()
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livros.get('id') == id:
            livros[indice].update(livro_alterado)
        
        return jsonify(livros[indice])
    
 #criar um novo livro 
@app.route('/livros',methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    
    return jsonify(livros)

#excluir livros
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get(id) == id:
            del livros[indice]
            
    return jsonify(livros)
        

    
if __name__ == '__main__':
    app.run(port=5001, host='127.0.0.1', debug=True)
    
