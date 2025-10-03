# Easy Issues Backend

API REST em FastAPI para gerenciamento de issues com MongoDB.

## 🚀 Tecnologias

- FastAPI
- MongoDB
- Pydantic
- PyMongo
- Uvicorn
- python-dotenv

## 📦 Instalação

1. **Clone e entre no diretório**
   ```bash
   git clone <url-do-repositorio>
   cd easy-issues-back
   ```

2. **Crie e ative o ambiente virtual**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate.bat  # Windows
   # source .venv/bin/activate  # Linux/Mac
   ```

3. **Instale as dependências**
   ```bash
   pip install fastapi uvicorn pymongo pydantic python-dotenv
   ```

   
   **Edite o arquivo `.env` com suas credenciais:**
   ```env
   MONGODB_URL= MONGODB_URL="mongodb+srv://<USER>:<PASS>@cluster.mongodb.net/...”
   MONGODB_DATABASE=
   MONGODB_COLLECTION=
   ```

## 🏃‍♂️ Executar

```bash
uvicorn main:app --reload
```

API disponível em: `http://localhost:8000`

**Documentação:** `http://localhost:8000/docs`
