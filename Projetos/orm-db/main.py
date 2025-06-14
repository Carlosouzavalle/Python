from database import db, Anuncio, Usuario

db.connect()


db.create_tables([Usuario, Anuncio])

# usuario =  Usuario.create(nome="ProgramadorPython", email="teste@teste.com", senha="12345")

# print(f"novo usuario: {usuario.id}, {usuario.nome}, {usuario.email}")

#Usuario.create(nome="ProgramadorPython", email="teste22@teste.com", senha="12345")
# Usuario.create(nome="Joao", email="test3@teste.com", senha="12345")
#Usuario.create(nome="carlos", email="test2@teste.com", senha="12345")

lista_usuarios = Usuario.select()
print("listando usuarios: ")

for u in lista_usuarios:
    print("-", u.id, u.nome)

# usuario1 = Usuario.get(Usuario.id == 1)
# print(usuario1.id, usuario1.nome)

joao = Usuario.get(Usuario.email == "test3@teste.com")
print(joao.id, joao.nome, joao.email)

programadorpython = Usuario.get(Usuario.email == "teste22@teste.com")
programadorpython.nome = "Maria Python"
programadorpython.save()

print(programadorpython.nome)