from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    """Redireciona para a página inicial de usuários."""
    return render_template('index.html')




# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)