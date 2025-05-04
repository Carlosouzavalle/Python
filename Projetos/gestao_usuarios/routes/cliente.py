from flask import Blueprint, render_template
from database.cliente import CLIENTES


cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_clientes():
    pass

@cliente_route.route('/new')
def formulario_cliente():
    return render_template('formulario_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    return render_template('detalhe_cliente.html')


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    return render_template('form_edit_cliente.html')


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_cliente(cliente_id):
    pass