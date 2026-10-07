from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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