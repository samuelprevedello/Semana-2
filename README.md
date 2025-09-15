# Projeto Semana 2 — Hello Flask (Python)

Pequeno projeto para cumprir a Semana 2:
- Repositório público
- Criar um branch além do `main`
- Fazer 5+ commits
- Abrir uma Pull Request e fazer merge

## Como rodar localmente

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

pip install -r requirements.txt
flask --app app/main.py run -p 5000
# Acesse: http://localhost:5000
```

## Rodar testes
```bash
pytest -q
```