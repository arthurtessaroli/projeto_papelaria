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

produtos = [
    {
        "id": 1,
        "nome": "Caderno Universitário",
        "codigo_barras": "7891234567890",
        "preco_venda": 24.90,
        "estoque_atual": 35,
    },
    {
        "id": 2,
        "nome": "Caneta Esferográfica Azul",
        "codigo_barras": "7899876543210",
        "preco_venda": 2.50,
        "estoque_atual": 120,
    },
    {
        "id": 3,
        "nome": "Lápis HB",
        "codigo_barras": "7894561237890",
        "preco_venda": 1.75,
        "estoque_atual": 80,
    },
]

fornecedores = [
    {
        "id": 1,
        "razao_social": "Distribuidora Papel & Cia Ltda.",
        "cnpj": "12.345.678/0001-90",
        "telefone": "(11) 3333-4444",
        "principal_produto": "Cadernos",
    },
    {
        "id": 2,
        "razao_social": "ABC Materiais Escolares Ltda.",
        "cnpj": "98.765.432/0001-10",
        "telefone": "(11) 5555-6666",
        "principal_produto": "Canetas e lápis",
    },
]

# Credenciais fixas, só para a atividade
LOGIN_EMAIL = "admin@papelaria.com"
LOGIN_SENHA = "123456"


def proximo_id(lista):
    """Retorna um novo ID baseado no maior ID existente."""
    if not lista:
        return 1

    return max(item["id"] for item in lista) + 1

@app.route("/", methods=["GET", "POST"])
def login():
    """Exibe a tela de login e confere e-mail e senha."""

    erros = []
    email = ""

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        senha = request.form.get("senha", "").strip()

        if not email:
            erros.append("O e-mail é obrigatório.")
        if not senha:
            erros.append("A senha é obrigatória.")

        # Campos preenchidos: confere e-mail e senha
        if not erros:
            if email == LOGIN_EMAIL and senha == LOGIN_SENHA:
                return redirect(url_for("index"))
            erros.append("E-mail ou senha incorretos.")

    return render_template("login.html", email=email, erros=erros)


@app.route("/inicio")
def index():
    """Página inicial, aberta depois do login."""
    return render_template("index.html")


@app.route("/usuarios")
def usuarios_listar():
    """Exibe a lista de usuários."""
    return render_template("usuarios_listar.html", usuarios=usuarios)


@app.route("/usuarios/cadastrar", methods=["GET", "POST"])
def usuarios_cadastrar():
    """Exibe o formulário e cadastra um novo usuário."""

    if request.method == "POST":
        usuario = {
            "id": proximo_id(usuarios),
            "nome": request.form.get("nome", "").strip(),
            "email": request.form.get("email", "").strip(),
            "celular": request.form.get("celular", "").strip(),
            "data_nasc": request.form.get("data_nasc", ""),
            "doc_nac": request.form.get("doc_nac", "").strip(),
            "nivel_acesso": request.form.get("nivel_acesso", "user"),
            "cep": request.form.get("cep", "").strip(),
            "endereco": request.form.get("endereco", "").strip(),
            "numero": request.form.get("numero", "").strip(),
            "complemento": request.form.get("complemento", "").strip(),
            "cidade": request.form.get("cidade", "").strip(),
            "estado": request.form.get("estado", "").strip(),
        }

        usuarios.append(usuario)

        return redirect(url_for("usuarios_listar"))

    return render_template("usuarios_cadastrar.html")


@app.route("/usuarios/<int:id>")
def usuario_visualizar(id):
    """Exibe os dados de um usuário específico."""

    usuario = next((item for item in usuarios if item["id"] == id), None)

    if usuario is None:
        return "Usuário não encontrado", 404

    return render_template(
        "usuarios_listar.html", usuarios=[usuario], visualizacao=True
    )


@app.route("/usuarios/<int:id>/excluir", methods=["POST"])
def usuario_excluir(id):
    """Exclui um usuário da lista simulada."""

    global usuarios

    usuarios = [usuario for usuario in usuarios if usuario["id"] != id]

    return redirect(url_for("usuarios_listar"))


@app.route("/produtos")
def produtos_listar():
    """Exibe a lista de produtos."""
    return render_template("produtos_listar.html", produtos=produtos)



@app.route("/produtos/cadastrar", methods=["GET", "POST"])
def produtos_cadastrar():
    """Exibe o formulário e cadastra um novo produto."""

    if request.method == "POST":
        try:
            preco_venda = float(
                request.form.get("preco_venda", "0").replace(",", ".")
            )
        except ValueError:
            preco_venda = 0

        try:
            estoque_atual = int(
                request.form.get("estoque_atual", "0")
            )
        except ValueError:
            estoque_atual = 0

        produto = {
            "id": proximo_id(produtos),
            "nome": request.form.get("nome", "").strip(),
            "codigo_barras": request.form.get("codigo_barras", "").strip(),
            "preco_venda": preco_venda,
            "estoque_atual": estoque_atual,
        }

        produtos.append(produto)

        return redirect(url_for("produtos_listar"))

    return render_template("produtos_cadastrar.html")


@app.route("/produtos/<int:id>")
def produto_visualizar(id):
    """Exibe os dados de um produto específico."""

    produto = next(
        (item for item in produtos if item["id"] == id),
        None
    )

    if produto is None:
        return "Produto não encontrado", 404

    return render_template(
        "produtos_listar.html",
        produtos=[produto],
        visualizacao=True
    )


@app.route("/produtos/<int:id>/excluir", methods=["POST"])
def produto_excluir(id):
    """Exclui um produto da lista simulada."""

    global produtos

    produtos = [
        produto for produto in produtos
        if produto["id"] != id
    ]

    return redirect(url_for("produtos_listar"))

@app.route("/fornecedores")
def fornecedores_listar():
    """Exibe a lista de fornecedores."""
    return render_template("fornecedores_listar.html", fornecedores=fornecedores)


@app.route("/fornecedores/cadastrar", methods=["GET", "POST"])
def fornecedores_cadastrar():
    """Exibe o formulário e cadastra um novo fornecedor."""

    if request.method == "POST":
        fornecedor = {
            "id": proximo_id(fornecedores),
            "razao_social": request.form.get(
                "razao_social", ""
            ).strip(),
            "cnpj": request.form.get(
                "cnpj", ""
            ).strip(),
            "telefone": request.form.get(
                "telefone", ""
            ).strip(),
            "principal_produto": request.form.get(
                "principal_produto", ""
            ).strip(),
        }

        fornecedores.append(fornecedor)

        return redirect(url_for("fornecedores_listar"))

    return render_template("fornecedores_cadastrar.html")


@app.route("/fornecedores/<int:id>")
def fornecedor_visualizar(id):
    """Exibe os dados de um fornecedor específico."""

    fornecedor = next(
        (item for item in fornecedores if item["id"] == id),
        None
    )

    if fornecedor is None:
        return "Fornecedor não encontrado", 404

    return render_template(
        "fornecedores_listar.html",
        fornecedores=[fornecedor],
        visualizacao=True
    )


@app.route("/fornecedores/<int:id>/excluir", methods=["POST"])
def fornecedor_excluir(id):
    """Exclui um fornecedor da lista simulada."""

    global fornecedores

    fornecedores = [
        fornecedor for fornecedor in fornecedores
        if fornecedor["id"] != id
    ]

    return redirect(url_for("fornecedores_listar"))



# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)

