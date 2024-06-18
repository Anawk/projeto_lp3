from flask import Flask, render_template
from validate_docbr import CPF, CNPJ

cpf = CPF()
cnpj = CNPJ()

app = Flask("Minha App")

# Uma página do flask é igual a: rota + função

#/ home page - Home 
@app.route("/")

def home():
    return render_template("home.html")

#/ contato - página de contato
@app.route("/contato")

def contato():
    return render_template("contato.html")

#/produtos - pagina produtos
@app.route("/produtos")

def produtos():
   lista_produtos = [
       {"nome" : "esmalte anita" , "descricao" : "coleção capadocia"},
       {"nome" : "esmalte risqué" , "descricao" : "coleção bridgertons"},
       {"nome" : "esmalte colorama" , "descricao" : "coleção divertidamente 2"}
   ]

   return render_template("produtos.html", produtos=lista_produtos)


# Abaixo está o exercicio sobre rotas, praticado em aula de reposição.

# página/servicos retornar "Nossos Serviços"
# pagina /gerar-cpf retornar Cpf Aleatorio
# pagina /gerar-cnpj retornar Cnpj aleatório


# /servicos - pagina serviços

@app.route("/servicos")
def servicos():
    return "<h1> Nossos Serviços </h1>"


@app.route("/gerar-cpf")
def gerar_cpf():
    return f"CPF: {cpf.generate(True)}"

@app.route("/gerar-cnpj")
def gerar_cnpj():
    return f"CNPJ: {cnpj.generate(True)}"

@app.route("/gerar-5-cpfs")
def gerar_5_cpfs():
    cpfs = []
    for i in range(5):
        cpfs.append(cpf.generate(True))
    return  f'CPFS: {cpfs} '

@app.route("/gerar-5-cnpjs")
def gerar_5_cnpjs():
    cnpjs = []
    for i in range(5):
        cnpjs.append(cnpj.generate(True))
    return  f'CNPJS: {cnpjs} '

app.run(debug=True)