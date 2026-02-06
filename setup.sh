#!/bin/bash

# BridgeTrace AI - Setup Automático
# Este script configura todo o ambiente automaticamente

set -e

echo "╔════════════════════════════════════════════════════════════╗"
echo "║         BridgeTrace AI - Setup Automático                  ║"
echo "║    Unified Financial Traceability Engine                   ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Função para printar com cor
print_step() {
    echo -e "${BLUE}➜${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# 1. Verificar Python
print_step "Verificando instalação do Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    print_success "Python encontrado: $PYTHON_VERSION"
else
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3.9 ou superior."
    exit 1
fi

# 2. Criar estrutura de diretórios
print_step "Criando estrutura de diretórios..."
mkdir -p api
mkdir -p frontend
mkdir -p data
mkdir -p logs
print_success "Diretórios criados"

# 3. Criar ambiente virtual
print_step "Criando ambiente virtual Python..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    print_success "Ambiente virtual criado"
else
    print_warning "Ambiente virtual já existe"
fi

# 4. Ativar ambiente virtual
print_step "Ativando ambiente virtual..."
source venv/bin/activate
print_success "Ambiente virtual ativado"

# 5. Atualizar pip
print_step "Atualizando pip..."
pip install --upgrade pip > /dev/null 2>&1
print_success "pip atualizado"

# 6. Instalar dependências
print_step "Instalando dependências Python..."
if [ -f "requirements-api.txt" ]; then
    pip install -r requirements-api.txt
    print_success "Dependências instaladas"
else
    print_warning "Arquivo requirements-api.txt não encontrado"
    print_step "Instalando dependências básicas..."
    pip install fastapi uvicorn[standard] pydantic python-multipart
    print_success "Dependências básicas instaladas"
fi

# 7. Verificar arquivos necessários
print_step "Verificando arquivos necessários..."

files_missing=0

if [ ! -f "api/main.py" ]; then
    print_warning "Arquivo api/main.py não encontrado"
    files_missing=1
fi

if [ ! -f "frontend/dashboard.html" ]; then
    print_warning "Arquivo frontend/dashboard.html não encontrado"
    files_missing=1
fi

if [ ! -f "frontend/styles.css" ]; then
    print_warning "Arquivo frontend/styles.css não encontrado"
    files_missing=1
fi

if [ ! -f "frontend/app.js" ]; then
    print_warning "Arquivo frontend/app.js não encontrado"
    files_missing=1
fi

if [ $files_missing -eq 1 ]; then
    echo ""
    print_warning "Alguns arquivos estão faltando. Por favor, siga o guia de instalação."
    echo ""
else
    print_success "Todos os arquivos necessários encontrados"
fi

# 8. Criar script de inicialização
print_step "Criando scripts de inicialização..."

# Script para iniciar a API
cat > start_api.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
cd api
python main.py
EOF

chmod +x start_api.sh
print_success "Script start_api.sh criado"

# Script para iniciar o frontend
cat > start_frontend.sh << 'EOF'
#!/bin/bash
cd frontend
python3 -m http.server 8080
EOF

chmod +x start_frontend.sh
print_success "Script start_frontend.sh criado"

# Script para iniciar tudo
cat > start_all.sh << 'EOF'
#!/bin/bash

echo "🚀 Iniciando BridgeTrace AI..."
echo ""

# Iniciar API em background
echo "📡 Iniciando API na porta 8000..."
source venv/bin/activate
cd api
python main.py &
API_PID=$!
cd ..

# Aguardar API iniciar
sleep 3

# Iniciar frontend em background
echo "🌐 Iniciando Frontend na porta 8080..."
cd frontend
python3 -m http.server 8080 &
FRONTEND_PID=$!
cd ..

echo ""
echo "✅ BridgeTrace AI está rodando!"
echo ""
echo "📊 Dashboard:  http://localhost:8080/dashboard.html"
echo "📚 API Docs:   http://localhost:8000/api/docs"
echo "🔍 API ReDoc:  http://localhost:8000/api/redoc"
echo ""
echo "Pressione Ctrl+C para parar os serviços"
echo ""

# Aguardar interrupção
trap "kill $API_PID $FRONTEND_PID 2>/dev/null; exit" INT TERM

wait
EOF

chmod +x start_all.sh
print_success "Script start_all.sh criado"

# 9. Criar .gitignore se não existir
if [ ! -f ".gitignore" ]; then
    print_step "Criando .gitignore..."
    cat > .gitignore << 'EOF'
# Python
venv/
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Logs
logs/
*.log

# OS
.DS_Store
Thumbs.db

# Environment
.env
.env.local

# Database
*.db
*.sqlite
*.sqlite3
EOF
    print_success ".gitignore criado"
fi

# 10. Resumo final
echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║               Setup Concluído com Sucesso! ✨              ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
print_success "Ambiente configurado e pronto para uso!"
echo ""
echo "📝 Próximos passos:"
echo ""
echo "   1. Certifique-se de que todos os arquivos estão no lugar:"
echo "      - api/main.py"
echo "      - frontend/dashboard.html"
echo "      - frontend/styles.css"
echo "      - frontend/app.js"
echo ""
echo "   2. Para iniciar o sistema:"
echo "      ${GREEN}./start_all.sh${NC}"
echo ""
echo "   3. Ou inicie separadamente:"
echo "      API:      ${GREEN}./start_api.sh${NC}"
echo "      Frontend: ${GREEN}./start_frontend.sh${NC}"
echo ""
echo "   4. Acesse o dashboard:"
echo "      ${BLUE}http://localhost:8080/dashboard.html${NC}"
echo ""
echo "   5. Consulte a documentação da API:"
echo "      ${BLUE}http://localhost:8000/api/docs${NC}"
echo ""
echo "📚 Para mais informações, consulte: INSTALLATION.md"
echo ""

if [ $files_missing -eq 1 ]; then
    print_warning "Lembre-se de adicionar os arquivos faltantes antes de iniciar!"
fi

echo ""
