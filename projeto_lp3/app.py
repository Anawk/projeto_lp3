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
       {"nome" : "esmalte anita" , "descricao" : "coleção capadocia", "imagem" : "anita.png"},
       {"nome" : "esmalte risqué" , "descricao" : "coleção bridgertons", "imagem" : "risque.png"},
       {"nome" : "esmalte colorama" , "descricao" : "coleção divertidamente 2", "imagem" : "colorama.jpg"}
   ]

   return render_template("produtos.html", produtos=lista_produtos)


@app.route("/servicos")
def servicos():
    return "<h1> Nossos Serviços </h1>"

@app.route("/gerar-cpf")
def gerar_cpf():
    cpf_gerado = cpf.generate(True)
    return render_template("cpf.html", cpf=cpf_gerado)

@app.route("/gerar-cnpj")
def gerar_cnpj():
    cnpj_gerado = cnpj.generate(True)
    return render_template("cnpj.html", cnpj=cnpj_gerado)

@app.route("/termosdeuso")
def termosdeuso():
    return render_template("termosdeuso.html")

@app.route("/politicadeprivacidade")
def politicadeprivacidade():
    return render_template("politicadeprivacidade.html")

@app.route("/privacidade")
def privacidade():
    return render_template("privacidade.html")

app.run(debug=True)