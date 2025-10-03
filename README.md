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

4. **Configure as variáveis de ambiente**
   
   Copie o arquivo de exemplo:
   ```bash
   copy env.example .env  # Windows
   # cp env.example .env  # Linux/Mac
   ```
   
   Edite o arquivo `.env` com suas credenciais:
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

## 📚 Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/` | Lista todas as issues |
| `POST` | `/` | Cria uma nova issue |
| `PUT` | `/{id}` | Atualiza uma issue |
| `DELETE` | `/{id}` | Remove uma issue |

## 📝 Modelo de Dados

```json
{
  "issue_number": 1,
  "reason": "Descrição do problema"
}
```

## 🔧 CORS

Configurado para aceitar requisições de:
- `http://localhost:5173`
- `http://127.0.0.1:5173`

## 🔐 Segurança

- As credenciais do MongoDB estão protegidas em variáveis de ambiente
- O arquivo `.env` está no `.gitignore` e não será commitado
- Use o arquivo `env.example` como template para configurar suas credenciais