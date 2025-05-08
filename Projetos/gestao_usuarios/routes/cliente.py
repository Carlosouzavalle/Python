from flask import Blueprint, render_template, request
from database.cliente import CLIENTES


cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_clientes():
    
    data = request.json
    
    novo_usuario  = {
        "id": len(CLIENTES) + 1,
        "nome": data['nome'],
        "Email": data['email'],
    }
    
    CLIENTES.append(novo_usuario)
    
    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def formulario_cliente():
    return render_template('formulario_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    return render_template('detalhe_cliente.html')


@cliente_route.route('/<int:cliente_id>/edit')
def form_cliente(cliente_id):
    
    cliente = next((c for c in CLIENTES if c['id'] == cliente_id), None)        
    return render_template('formulario_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
    cliente_editado = None
    
    data = request.json
    for c in CLIENTES:
        if c['id'] == cliente_id:
            c['nome'] = data['nome']
            c['email'] = data['email']


            cliente_editado = c
            
    return render_template('item_cliente.html', cliente=cliente_editado)

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_cliente(cliente_id):
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id ]
    
    return {'deleted': 'ok'}