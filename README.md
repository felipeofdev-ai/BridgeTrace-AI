# 🌉 BridgeTrace AI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

![BridgeTrace AI](https://img.shields.io/badge/BridgeTrace-AI-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9+-green?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-teal?style=for-the-badge&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Unified Financial Traceability Engine for Banking, PIX and Crypto**

Uma solução de rastreabilidade financeira que modela, correlaciona e explica fluxos financeiros através de sistemas bancários tradicionais (incluindo PIX) e redes blockchain, utilizando teoria de grafos e IA Generativa.

[🚀 Demo](#-demonstração) • [📖 Documentação](#-documentação) • [💻 Instalação](#-instalação-rápida) • [🤝 Contribuir](#-contribuindo)

</div>

---

## 🎯 Visão Geral

BridgeTrace AI é um sistema de pesquisa focado em **rastreabilidade financeira, explicabilidade e análise de risco**, permitindo uma visão unificada de ecossistemas financeiros híbridos onde moeda fiduciária e criptomoedas coexistem.

### ✨ Principais Funcionalidades

- 🔗 **Modelagem Unificada de Grafos** - Integração de banking + crypto
- 🔍 **Rastreamento Multi-Hop** - Trace transações através de múltiplos saltos
- 🎲 **Correlação Probabilística** - Ligação de contas bancárias ↔ carteiras crypto
- ⚠️ **Análise de Risco** - Scoring baseado em padrões comportamentais
- 🤖 **Explicações com IA** - Narrativas para compliance e auditoria
- 📊 **Dashboard Interativo** - Visualização em tempo real
- 🌐 **API REST Completa** - Endpoints documentados (Swagger/ReDoc)

---

## 🖥️ Demonstração

### Dashboard Principal

O dashboard oferece uma visão completa do sistema de rastreabilidade:

- **Estatísticas em Tempo Real** - Nós, transações, volume, risco
- **Visualizações Gráficas** - Charts e grafos interativos
- **Rastreamento de Fluxo** - Interface para traçar caminhos financeiros
- **Análise de Risco** - Avaliação de entidades e padrões
- **Gerenciamento de Nós** - CRUD de entidades do grafo

### API REST

Acesse a documentação interativa em:
- **Swagger UI:** `http://localhost:8000/api/docs`
- **ReDoc:** `http://localhost:8000/api/redoc`

---

## 🚀 Instalação Rápida

### Pré-requisitos

- Python 3.9 ou superior
- Git
- Navegador moderno

### Opção 1: Setup Automático (Recomendado)

```bash
# Clone o repositório
git clone https://github.com/felipeofdev-ai/BridgeTrace-AI.git
cd BridgeTrace-AI

# Execute o script de setup
chmod +x setup.sh
./setup.sh

# Inicie o sistema
./start_all.sh
```

### Opção 2: Setup Manual

```bash
# Clone o repositório
git clone https://github.com/felipeofdev-ai/BridgeTrace-AI.git
cd BridgeTrace-AI

# Crie e ative ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements-api.txt

# Inicie a API
cd api
python main.py
```

Em outro terminal:

```bash
# Inicie o frontend
cd frontend
python3 -m http.server 8080
```

### Acessar o Sistema

- **Dashboard:** http://localhost:8080/dashboard.html
- **API Docs:** http://localhost:8000/api/docs
- **API ReDoc:** http://localhost:8000/api/redoc

---

## 📁 Estrutura do Projeto

```
BridgeTrace-AI/
├── api/
│   └── main.py              # API FastAPI principal
├── frontend/
│   ├── dashboard.html       # Interface web
│   ├── styles.css          # Estilos CSS
│   └── app.js              # Lógica JavaScript
├── core/
│   ├── graph_builder.py    # Construção de grafos
│   ├── entity_linker.py    # Correlação de entidades
│   └── trace_engine.py     # Motor de rastreamento
├── data/
│   └── synthetic/          # Dados sintéticos
├── docs/
│   └── architecture.md     # Documentação arquitetural
├── tests/
│   └── test_api.py         # Testes automatizados
├── requirements-api.txt    # Dependências Python
├── setup.sh               # Script de setup automático
├── INSTALLATION.md        # Guia detalhado de instalação
└── README.md             # Este arquivo
```

---

## 🔌 API Endpoints

### Principais Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/api/health` | Status da API |
| `GET` | `/api/nodes` | Lista todos os nós |
| `GET` | `/api/nodes/{id}` | Detalhes de um nó |
| `GET` | `/api/transactions` | Histórico de transações |
| `POST` | `/api/trace` | Rastreamento de fluxo |
| `POST` | `/api/risk-analysis` | Análise de risco |
| `GET` | `/api/statistics` | Estatísticas do sistema |
| `POST` | `/api/explain` | Explicação com IA |

### Exemplo de Uso

```python
import requests

# Rastrear fluxo financeiro
response = requests.post('http://localhost:8000/api/trace', json={
    "source_id": "bank_001",
    "max_hops": 5,
    "min_amount": 1000.0
})

trace_result = response.json()
print(f"Encontrados {len(trace_result['hops'])} saltos")
print(f"Volume total: R$ {trace_result['total_amount']}")
```

---

## 🎨 Tecnologias Utilizadas

### Backend
- **FastAPI** - Framework web moderno e rápido
- **Uvicorn** - Servidor ASGI de alta performance
- **Pydantic** - Validação de dados
- **Python 3.9+** - Linguagem principal

### Frontend
- **HTML5/CSS3** - Estrutura e estilo
- **JavaScript (Vanilla)** - Lógica da aplicação
- **Chart.js** - Visualização de gráficos
- **Vis.js Network** - Renderização de grafos
- **Font Awesome** - Ícones

### Futuras Integrações
- **NetworkX** - Algoritmos de grafos avançados
- **SQLAlchemy** - ORM para banco de dados
- **OpenAI/Anthropic** - Explicações com IA Generativa
- **PostgreSQL** - Banco de dados relacional

---

## 🧪 Casos de Uso

### 1. Rastreamento de Fundos
Simule o rastreamento de fundos de uma transferência PIX até uma carteira de criptomoedas:

```
Conta Bancária → PIX → Exchange → Carteira Crypto
```

### 2. Análise de Risco
Avalie o perfil de risco de uma entidade baseado em:
- Volume de transações
- Frequência de operações
- Canais utilizados
- Padrões comportamentais

### 3. Correlação de Entidades
Identifique links probabilísticos entre:
- Contas bancárias e carteiras crypto
- Múltiplas chaves PIX do mesmo titular
- Redes de entidades relacionadas

### 4. Compliance e Auditoria
Gere relatórios explicativos para:
- Investigações financeiras
- Análises de compliance
- Auditorias regulatórias

---

## ⚠️ Aviso Importante

> **Este projeto utiliza 100% dados sintéticos e simulados.**
>
> O BridgeTrace AI **NÃO se conecta a**:
> - Sistemas do Banco Central do Brasil
> - Infraestrutura PIX real
> - APIs bancárias reais
> - Redes blockchain em produção
>
> O projeto é destinado **exclusivamente para**:
> - Pesquisa acadêmica
> - Demonstração arquitetural
> - Fins educacionais
> - Prototipagem de conceitos

---

## 🗺️ Roadmap

### Versão 1.0 (Atual)
- ✅ API REST com FastAPI
- ✅ Dashboard web interativo
- ✅ Rastreamento básico de transações
- ✅ Análise de risco simplificada
- ✅ Visualização de grafos

### Versão 1.1 (Próxima)
- 🔄 Integração com banco de dados (PostgreSQL)
- 🔄 Autenticação JWT
- 🔄 Algoritmos avançados de grafos
- 🔄 Exportação de relatórios (PDF)

### Versão 2.0 (Futuro)
- 📅 Integração com IA Generativa
- 📅 Análise preditiva de risco
- 📅 Sistema de alertas em tempo real
- 📅 API GraphQL
- 📅 Mobile app (React Native)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Add: Nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

### Diretrizes de Commit

Use commits semânticos:

```
feat: Nova funcionalidade
fix: Correção de bug
docs: Documentação
style: Formatação
refactor: Refatoração
test: Testes
chore: Tarefas gerais
```

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## 👤 Autor

**Felipe de Oliveira Fernandes**

- GitHub: [@felipeofdev-ai](https://github.com/felipeofdev-ai)
- Especialidades: Python | GenAI | Fintech | Cybersecurity

---

## 🙏 Agradecimentos

- Comunidade Python
- FastAPI Framework
- Vis.js Network Library
- Chart.js Library
- Todos os contribuidores

---

## 📞 Suporte

Encontrou um bug? Tem uma sugestão?

- 🐛 Abra uma [Issue](https://github.com/felipeofdev-ai/BridgeTrace-AI/issues)
- 💡 Inicie uma [Discussion](https://github.com/felipeofdev-ai/BridgeTrace-AI/discussions)
- 📧 Entre em contato

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela!**

**Desenvolvido com ❤️ por Felipe de Oliveira Fernandes**

</div>
