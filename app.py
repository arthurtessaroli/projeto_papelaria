from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

usuarios = [
    {
        "id": 1,
        "nome": "Ana Souza",
        "email": "ana@papelaria.com",
        "celular": "(14) 99999-1111",
        "data_nasc": "1995-03-15",
        "doc_nac": "123.456.789-00",
        "nivel_acesso": "admin",
        "cep": "17200-000",
        "endereco": "Rua das Flores",
        "numero": "100",
        "complemento": "",
        "cidade": "Jaú",
        "estado": "SP",
    },
    {
        "id": 2,
        "nome": "Carlos Oliveira",
        "email": "carlos@papelaria.com",
        "celular": "(14) 98888-2222",
        "data_nasc": "1998-07-22",
        "doc_nac": "987.654.321-00",
        "nivel_acesso": "user",
        "cep": "17201-000",
        "endereco": "Avenida Central",
        "numero": "250",
        "complemento": "Sala 2",
        "cidade": "Jaú",
        "estado": "SP",
    },
]

@app.route("/")
def index():
    """Redireciona para a página inicial de usuários."""
    return render_template('index.html')

@app.route("/usuarios")
def usuarios_listar():
    """Exibe a lista de usuários."""
    return render_template(
        "usuarios_listar.html",
        usuarios=usuarios
    )

@app.route("/produtos")
def produtos_listar():
    """Exibe a lista de produtos."""
    return render_template(
        "produtos_listar.html",
        produtos=produtos
    )    

@app.route("/fornecedores")
def fornecedores_listar():
    """Exibe a lista de fornecedores."""
    return render_template(
        "fornecedores_listar.html",
        fornecedores=fornecedores
    )


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)