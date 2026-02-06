# 📋 QUICK START GUIDE - BridgeTrace AI

## ✅ FILE CHECKLIST

All files have been added to the repository:

### 📄 Files in Repository:

1. **api/main.py** - FastAPI Backend ✅
2. **frontend/dashboard.html** - Web Dashboard ✅
3. **frontend/styles.css** - CSS Styling ✅
4. **frontend/app.js** - JavaScript Logic ✅
5. **requirements-api.txt** - Python Dependencies ✅
6. **INSTALLATION.md** - Installation Guide ✅
7. **setup.sh** - Automated Setup Script ✅
8. **README.md** - Project Documentation ✅

---

## 🚀 QUICK INSTALLATION

### Option A: Automated Setup (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/felipeofdev-ai/BridgeTrace-AI.git
cd BridgeTrace-AI

# 2. Make setup script executable
chmod +x setup.sh

# 3. Run setup
./setup.sh

# 4. Start the system
./start_all.sh
```

### Option B: Manual Setup

```bash
# 1. Clone the repository
git clone https://github.com/felipeofdev-ai/BridgeTrace-AI.git
cd BridgeTrace-AI

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# 4. Install dependencies
pip install -r requirements-api.txt

# 5. Start API (Terminal 1)
cd api
python main.py
```

In another terminal:

```bash
# 6. Start Frontend (Terminal 2)
cd frontend
python3 -m http.server 8080
```

---

## 🌐 ACCESS THE APPLICATION

After starting the services:

- **Dashboard:** http://localhost:8080/dashboard.html
- **API Documentation (Swagger):** http://localhost:8000/api/docs
- **API Documentation (ReDoc):** http://localhost:8000/api/redoc
- **API Health Check:** http://localhost:8000/api/health

---

## 📁 PROJECT STRUCTURE

```
BridgeTrace-AI/
├── api/
│   └── main.py              # FastAPI backend
├── frontend/
│   ├── dashboard.html       # Web interface
│   ├── styles.css          # Styling
│   └── app.js              # Application logic
├── core/                    # (Future) Core modules
├── data/                    # (Future) Data storage
├── docs/                    # Documentation
├── tests/                   # (Future) Tests
├── requirements-api.txt     # Python dependencies
├── setup.sh                # Automated setup script
├── INSTALLATION.md         # Detailed installation guide
└── README.md              # Project documentation
```

---

## ✅ VERIFY INSTALLATION

### Test 1: API Health Check

```bash
curl http://localhost:8000/api/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2026-02-06T...",
  "version": "1.0.0"
}
```

### Test 2: Dashboard

1. Open: http://localhost:8080/dashboard.html
2. Check if statistics cards appear
3. Navigate between sections
4. Test the trace form

### Test 3: API Documentation

1. Access: http://localhost:8000/api/docs
2. Test the `/api/statistics` endpoint
3. Verify the response

---

## 🎯 MAIN FEATURES

### Dashboard Section
- **Real-time Statistics** - Nodes, transactions, volume, risk
- **Interactive Visualizations** - Charts and network graphs
- **Dark Mode Support** - Toggle between light/dark themes

### Tracing Section
- **Financial Flow Tracing** - Track funds through multiple hops
- **Configurable Parameters** - Max hops, minimum amount
- **Detailed Results** - Complete transaction path visualization

### Risk Analysis Section
- **Entity Risk Scoring** - Behavioral pattern analysis
- **Time-based Analysis** - Configurable time ranges
- **Risk Metrics** - Volume, frequency, channels used

### Nodes Management
- **Filter by Type** - Bank accounts, PIX keys, crypto wallets, entities
- **Detailed Metadata** - Complete information for each node
- **Real-time Updates** - Refresh data on demand

---

## 🔌 API ENDPOINTS

### Core Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/health` | API health status |
| `GET` | `/api/nodes` | List all nodes |
| `GET` | `/api/nodes/{id}` | Get node details |
| `GET` | `/api/transactions` | Transaction history |
| `POST` | `/api/trace` | Trace financial flow |
| `POST` | `/api/risk-analysis` | Risk analysis |
| `GET` | `/api/statistics` | System statistics |
| `POST` | `/api/explain` | AI-powered explanation |

### Example Usage

```python
import requests

# Trace financial flow
response = requests.post('http://localhost:8000/api/trace', json={
    "source_id": "bank_001",
    "max_hops": 5,
    "min_amount": 1000.0
})

result = response.json()
print(f"Found {len(result['hops'])} transaction hops")
print(f"Total volume: R$ {result['total_amount']:,.2f}")
```

```bash
# Using curl
curl -X POST "http://localhost:8000/api/trace" \
  -H "Content-Type: application/json" \
  -d '{
    "source_id": "bank_001",
    "max_hops": 5,
    "min_amount": 0.0
  }'
```

---

## 🐛 TROUBLESHOOTING

### Issue: API doesn't start

**Solution:**
```bash
# Check if port 8000 is available
lsof -i :8000  # Linux/Mac
netstat -ano | findstr :8000  # Windows

# If occupied, change port in api/main.py
# Last line: uvicorn.run(..., port=8001)
```

### Issue: Frontend doesn't load data

**Solutions:**
1. Open browser console (F12)
2. Check for CORS errors
3. Verify API is running at http://localhost:8000
4. Check the API URL in `app.js` (line 3)

### Issue: Python modules not found

**Solution:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# Reinstall dependencies
pip install -r requirements-api.txt
```

### Issue: Permission denied on setup.sh

**Solution:**
```bash
# Make script executable
chmod +x setup.sh

# If still issues, run directly with bash
bash setup.sh
```

---

## 🔒 MAKING FILES EXECUTABLE ON GITHUB

### Method 1: Via Git Command (Recommended)

```bash
# Make setup.sh executable
git update-index --chmod=+x setup.sh

# Commit the permission change
git add setup.sh
git commit -m "chore: Make setup.sh executable"
git push origin main
```

### Method 2: Via Local Change + Push

```bash
# Make executable locally
chmod +x setup.sh

# Check the change
git ls-files --stage setup.sh

# If mode is 100644, update it
git update-index --chmod=+x setup.sh

# Verify (should show 100755)
git ls-files --stage setup.sh

# Commit and push
git add setup.sh
git commit -m "chore: Add executable permission to setup.sh"
git push origin main
```

### Method 3: Create New File with Correct Permissions

```bash
# Remove from git (keep local)
git rm --cached setup.sh

# Add with executable permission
chmod +x setup.sh
git add setup.sh

# Commit
git commit -m "chore: Re-add setup.sh with executable permission"
git push origin main
```

### Verify Executable Status on GitHub

After pushing, clone in a fresh directory:
```bash
cd /tmp
git clone https://github.com/felipeofdev-ai/BridgeTrace-AI.git
cd BridgeTrace-AI
ls -l setup.sh
# Should show: -rwxr-xr-x (executable)
```

---

## 🎨 TECHNOLOGY STACK

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **Python 3.9+** - Programming language

### Frontend
- **HTML5/CSS3** - Structure and styling
- **JavaScript (Vanilla)** - Application logic
- **Chart.js** - Data visualization
- **Vis.js Network** - Graph rendering
- **Font Awesome** - Icons

### Future Integrations
- **NetworkX** - Advanced graph algorithms
- **SQLAlchemy** - Database ORM
- **OpenAI/Anthropic** - AI explanations
- **PostgreSQL** - Production database

---

## 📊 SAMPLE DATA

The system comes with synthetic sample data:

### Nodes
- **Bank Accounts** - Traditional banking nodes
- **PIX Keys** - Brazilian instant payment keys
- **Crypto Wallets** - Blockchain wallet nodes
- **Entities** - Legal entities (companies/individuals)

### Transactions
- **PIX Transfers** - Instant payments
- **Bank Transfers** - Traditional transfers
- **Crypto Transactions** - On-chain movements
- **Bridge Events** - Fiat ↔ Crypto conversions

---

## 🌟 NEXT STEPS

After successful installation:

1. **Explore the Dashboard** - Navigate through all sections
2. **Test API Endpoints** - Use Swagger UI
3. **Run Trace Analysis** - Try different parameters
4. **Analyze Risk** - Evaluate entity patterns
5. **Review Code** - Understand the architecture
6. **Customize Data** - Add your own synthetic data
7. **Extend Features** - Build on top of the system

---

## 📚 ADDITIONAL RESOURCES

- **Full Installation Guide:** INSTALLATION.md
- **API Documentation:** http://localhost:8000/api/docs
- **Project README:** README.md
- **GitHub Repository:** https://github.com/felipeofdev-ai/BridgeTrace-AI

---

## ⚠️ IMPORTANT NOTICE

> **This project uses 100% synthetic and simulated data.**
>
> BridgeTrace AI does **NOT** connect to:
> - Central Bank systems
> - Real PIX infrastructure
> - Real bank APIs
> - Live blockchain networks
>
> Intended for:
> - Research purposes
> - Educational demonstrations
> - Architectural prototyping
> - Concept validation

---

## 🤝 CONTRIBUTING

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add: Amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Commit Convention

Use semantic commits:

```
feat: New feature
fix: Bug fix
docs: Documentation
style: Formatting
refactor: Code refactoring
test: Tests
chore: General tasks
```

---

## 📞 SUPPORT

Need help?

1. ✅ Check this guide (QUICK_START.md)
2. ✅ Review INSTALLATION.md
3. ✅ Check terminal logs
4. ✅ Open a GitHub Issue
5. ✅ Join Discussions

---

## ✨ FINAL CHECKLIST

Before starting:

- [ ] All files in correct locations
- [ ] setup.sh is executable
- [ ] Python 3.9+ is installed
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] API starts without errors
- [ ] Frontend loads correctly
- [ ] Dashboard displays data
- [ ] Navigation works
- [ ] Forms submit requests
- [ ] Charts render

---

## 🎓 LEARNING PATH

### Beginner
1. Run the system
2. Explore the dashboard
3. Test API endpoints
4. Understand data flow

### Intermediate
1. Read the source code
2. Modify sample data
3. Add new endpoints
4. Customize UI

### Advanced
1. Integrate database
2. Add authentication
3. Implement AI features
4. Deploy to production

---

## 🚀 DEPLOYMENT OPTIONS

### Heroku

```bash
# Create Procfile
echo "web: uvicorn api.main:app --host 0.0.0.0 --port \$PORT" > Procfile

# Deploy
heroku create bridgetrace-ai
git push heroku main
```

### Railway

1. Connect GitHub repository
2. Set start command: `uvicorn api.main:app --host 0.0.0.0 --port $PORT`
3. Auto-deploy on push

### Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements-api.txt .
RUN pip install --no-cache-dir -r requirements-api.txt

COPY . .

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
docker build -t bridgetrace-ai .
docker run -p 8000:8000 bridgetrace-ai
```

---

## 🎉 SUCCESS!

If you've reached this point, congratulations! 

Your BridgeTrace AI system is ready to use.

**Developed with ❤️ by Felipe de Oliveira Fernandes**

**BridgeTrace AI - Unified Financial Traceability Engine**

---

## 📈 PERFORMANCE TIPS

- Use virtual environment to avoid conflicts
- Keep dependencies updated
- Monitor API response times
- Optimize graph rendering for large datasets
- Use caching for frequently accessed data

---

## 🔐 SECURITY NOTES

For production deployment:

- [ ] Enable HTTPS
- [ ] Add authentication (JWT)
- [ ] Implement rate limiting
- [ ] Validate all inputs
- [ ] Use environment variables
- [ ] Enable CORS only for trusted origins
- [ ] Regular security audits

---

**Last Updated:** February 6, 2026  
**Version:** 1.0.0  
**License:** MIT
