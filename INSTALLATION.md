# 🚀 Guia Completo de Instalação - BridgeTrace AI

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.9+** (recomendado 3.10 ou 3.11)
- **Git** para controle de versão
- **Navegador moderno** (Chrome, Firefox, Edge, Safari)

## 🔧 Passo a Passo de Instalação

### 1️⃣ Estrutura de Diretórios

Primeiro, vamos organizar os arquivos no seu repositório. Crie a seguinte estrutura:

```
BridgeTrace-AI/
├── api/
│   └── main.py              # ← Cole o arquivo api_main.py aqui
├── frontend/
│   ├── dashboard.html       # ← Dashboard principal
│   ├── styles.css           # ← Estilos CSS
│   └── app.js              # ← Lógica JavaScript
├── requirements.txt         # ← Dependências Python (já existe)
├── requirements-api.txt     # ← Nova versão atualizada
└── README.md               # ← Documentação
```

### 2️⃣ Colocar os Arquivos

#### **Arquivo 1: api/main.py**
- **Nome do arquivo:** `main.py`
- **Localização:** `api/main.py`
- **Conteúdo:** Todo o código do arquivo `api_main.py` que criei

#### **Arquivo 2: frontend/dashboard.html**
- **Nome do arquivo:** `dashboard.html`
- **Localização:** `frontend/dashboard.html`
- **Conteúdo:** Todo o HTML do dashboard

#### **Arquivo 3: frontend/styles.css**
- **Nome do arquivo:** `styles.css`
- **Localização:** `frontend/styles.css`
- **Conteúdo:** Todo o CSS criado

#### **Arquivo 4: frontend/app.js**
- **Nome do arquivo:** `app.js`
- **Localização:** `frontend/app.js`
- **Conteúdo:** Todo o JavaScript da aplicação

#### **Arquivo 5: requirements-api.txt**
- **Nome do arquivo:** `requirements-api.txt`
- **Localização:** Raiz do projeto
- **Conteúdo:** Lista de dependências Python atualizada

### 3️⃣ Comandos de Instalação

#### No Linux/Mac:

```bash
# 1. Clone seu repositório (se ainda não tiver)
git clone https://github.com/felipeofdev-ai/BridgeTrace-AI.git
cd BridgeTrace-AI

# 2. Crie um ambiente virtual Python
python3 -m venv venv

# 3. Ative o ambiente virtual
source venv/bin/activate

# 4. Instale as dependências
pip install -r requirements-api.txt

# 5. Execute a API
cd api
python main.py
```

#### No Windows:

```cmd
# 1. Clone seu repositório
git clone https://github.com/felipeofdev-ai/BridgeTrace-AI.git
cd BridgeTrace-AI

# 2. Crie um ambiente virtual Python
python -m venv venv

# 3. Ative o ambiente virtual
venv\Scripts\activate

# 4. Instale as dependências
pip install -r requirements-api.txt

# 5. Execute a API
cd api
python main.py
```

### 4️⃣ Acessar o Sistema

Após executar a API, você terá acesso a:

1. **Dashboard Principal:** 
   - Abra o arquivo `frontend/dashboard.html` no navegador
   - Ou acesse: `http://localhost:8000/dashboard.html` (se configurar static files)

2. **API Swagger Docs:**
   - Acesse: `http://localhost:8000/api/docs`

3. **API ReDoc:**
   - Acesse: `http://localhost:8000/api/redoc`

### 5️⃣ Servir Frontend com Python

Para servir os arquivos HTML corretamente, você tem duas opções:

#### Opção A: Servidor HTTP Simples do Python

```bash
# Na pasta frontend
cd frontend
python -m http.server 8080
```

Depois acesse: `http://localhost:8080/dashboard.html`

#### Opção B: Integrar com FastAPI

Adicione estas linhas no arquivo `api/main.py`:

```python
from fastapi.staticfiles import StaticFiles

# Adicione depois da linha: app = FastAPI(...)
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")
```

Depois acesse diretamente: `http://localhost:8000/dashboard.html`

## 📤 Comandos Git para Commit

### Commit 1: Adicionar API Backend

```bash
git add api/main.py
git commit -m "feat: Add FastAPI backend with financial traceability endpoints

- Implemented REST API with FastAPI
- Added endpoints for nodes, transactions, trace, and risk analysis
- Integrated CORS middleware for frontend communication
- Created synthetic data samples for demonstration
- Added health check and statistics endpoints"

git push origin main
```

### Commit 2: Adicionar Frontend Dashboard

```bash
git add frontend/
git commit -m "feat: Add modern web dashboard for financial visualization

- Created responsive HTML dashboard with multiple sections
- Implemented CSS styling with dark mode support
- Added JavaScript logic for API integration
- Integrated Chart.js for data visualization
- Added vis-network for graph rendering
- Implemented trace and risk analysis forms"

git push origin main
```

### Commit 3: Atualizar Requirements

```bash
git add requirements-api.txt
git commit -m "chore: Update Python dependencies for API

- Added FastAPI and Uvicorn
- Included CORS middleware support
- Added Pydantic for data validation
- Included development tools (pytest, black, flake8)"

git push origin main
```

### Commit 4: Adicionar Documentação

```bash
git add INSTALLATION.md
git commit -m "docs: Add comprehensive installation guide

- Created step-by-step installation instructions
- Added directory structure documentation
- Included commands for Linux/Mac/Windows
- Added Git commit guidelines
- Documented deployment options"

git push origin main
```

## 🔍 Verificar Instalação

Para verificar se tudo está funcionando:

1. **Teste a API:**
   ```bash
   curl http://localhost:8000/api/health
   ```
   
   Deve retornar:
   ```json
   {
     "status": "healthy",
     "timestamp": "2026-02-06T...",
     "version": "1.0.0"
   }
   ```

2. **Teste o Dashboard:**
   - Abra o navegador
   - Acesse o dashboard
   - Verifique se os cards de estatísticas aparecem
   - Teste a navegação entre seções

## 🐛 Solução de Problemas

### Erro: "Module not found"
```bash
# Certifique-se de que o ambiente virtual está ativado
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Reinstale as dependências
pip install -r requirements-api.txt
```

### Erro: "CORS policy"
- Verifique se a API está rodando em `http://localhost:8000`
- Confirme que o CORS middleware está configurado no `main.py`

### Erro: "Port already in use"
```bash
# Mude a porta no main.py
# Linha: uvicorn.run(..., port=8001)  # Use outra porta
```

### Dashboard não carrega dados
1. Verifique se a API está rodando
2. Abra o console do navegador (F12)
3. Verifique erros de conexão
4. Confirme que a URL da API no `app.js` está correta

## 📚 Próximos Passos

Após a instalação básica, você pode:

1. **Adicionar dados reais** (mantendo sintéticos)
2. **Integrar banco de dados** (SQLite, PostgreSQL)
3. **Implementar autenticação** (JWT, OAuth)
4. **Adicionar mais algoritmos** de análise de grafo
5. **Integrar com GenAI** (OpenAI, Anthropic)
6. **Fazer deploy** (Heroku, Railway, AWS)

## 🌐 Deploy na Produção

### Heroku

```bash
# Criar Procfile
echo "web: uvicorn api.main:app --host 0.0.0.0 --port $PORT" > Procfile

# Deploy
heroku create bridgetrace-ai
git push heroku main
```

### Railway

1. Conecte seu repositório GitHub
2. Configure o comando de inicialização: `uvicorn api.main:app --host 0.0.0.0 --port $PORT`
3. Deploy automático

### Docker

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements-api.txt .
RUN pip install --no-cache-dir -r requirements-api.txt

COPY . .

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# Build e Run
docker build -t bridgetrace-ai .
docker run -p 8000:8000 bridgetrace-ai
```

## 📞 Suporte

Em caso de dúvidas:
- Abra uma issue no GitHub
- Consulte a documentação da API em `/api/docs`
- Revise os logs de erro no terminal

---

**Desenvolvido por Felipe de Oliveira Fernandes**
**Projeto BridgeTrace AI - 2026**
