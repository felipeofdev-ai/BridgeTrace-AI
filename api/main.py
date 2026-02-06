"""
BridgeTrace AI - FastAPI Main Application
Financial Traceability Engine API
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
import uvicorn
import json
from pathlib import Path

# Initialize FastAPI app
app = FastAPI(
    title="BridgeTrace AI API",
    description="Unified Financial Traceability Engine for Banking, PIX and Crypto",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models
class TransactionNode(BaseModel):
    id: str
    type: str  # 'bank_account', 'pix_key', 'crypto_wallet', 'entity'
    name: str
    metadata: Dict[str, Any]

class TransactionEdge(BaseModel):
    source: str
    target: str
    amount: float
    currency: str
    timestamp: str
    channel: str  # 'pix', 'bank_transfer', 'crypto', 'bridge'
    risk_score: Optional[float] = 0.0

class TraceRequest(BaseModel):
    source_id: str
    max_hops: int = 5
    min_amount: Optional[float] = 0.0

class RiskAnalysisRequest(BaseModel):
    entity_id: str
    time_range_days: int = 30

# Sample synthetic data for demonstration
SAMPLE_NODES = [
    {
        "id": "bank_001",
        "type": "bank_account",
        "name": "Conta Corrente - Banco X",
        "metadata": {
            "bank": "Banco X S.A.",
            "account_type": "Corrente",
            "balance": 150000.00
        }
    },
    {
        "id": "pix_001",
        "type": "pix_key",
        "name": "PIX Key - CPF ***123**",
        "metadata": {
            "key_type": "CPF",
            "masked_key": "***123**",
            "active": True
        }
    },
    {
        "id": "crypto_001",
        "type": "crypto_wallet",
        "name": "BTC Wallet",
        "metadata": {
            "blockchain": "Bitcoin",
            "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
            "balance_btc": 0.5
        }
    },
    {
        "id": "entity_001",
        "type": "entity",
        "name": "Empresa ABC Ltda",
        "metadata": {
            "document": "CNPJ",
            "masked_doc": "**.***.***/**01-**",
            "type": "PJ"
        }
    }
]

SAMPLE_TRANSACTIONS = [
    {
        "source": "bank_001",
        "target": "pix_001",
        "amount": 5000.00,
        "currency": "BRL",
        "timestamp": "2026-02-01T10:30:00",
        "channel": "pix",
        "risk_score": 0.2
    },
    {
        "source": "pix_001",
        "target": "crypto_001",
        "amount": 4800.00,
        "currency": "BRL",
        "timestamp": "2026-02-01T14:20:00",
        "channel": "bridge",
        "risk_score": 0.5
    },
    {
        "source": "bank_001",
        "target": "entity_001",
        "amount": 25000.00,
        "currency": "BRL",
        "timestamp": "2026-02-02T09:15:00",
        "channel": "bank_transfer",
        "risk_score": 0.1
    }
]

# API Endpoints

@app.get("/", response_class=HTMLResponse)
async def root():
    """Redirect to dashboard"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="refresh" content="0; url=/dashboard.html">
    </head>
    <body>
        <p>Redirecting to dashboard...</p>
    </body>
    </html>
    """

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }

@app.get("/api/nodes")
async def get_nodes(
    node_type: Optional[str] = Query(None, description="Filter by node type")
):
    """Get all nodes in the financial graph"""
    nodes = SAMPLE_NODES
    if node_type:
        nodes = [n for n in nodes if n["type"] == node_type]
    return {"nodes": nodes, "count": len(nodes)}

@app.get("/api/nodes/{node_id}")
async def get_node(node_id: str):
    """Get specific node details"""
    node = next((n for n in SAMPLE_NODES if n["id"] == node_id), None)
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")
    return node

@app.get("/api/transactions")
async def get_transactions(
    limit: int = Query(100, description="Maximum number of transactions"),
    min_amount: Optional[float] = Query(None, description="Minimum transaction amount")
):
    """Get transaction history"""
    transactions = SAMPLE_TRANSACTIONS
    if min_amount:
        transactions = [t for t in transactions if t["amount"] >= min_amount]
    return {
        "transactions": transactions[:limit],
        "count": len(transactions)
    }

@app.post("/api/trace")
async def trace_flow(request: TraceRequest):
    """
    Trace financial flow from a source node
    Returns multi-hop path analysis
    """
    # Simplified trace logic (in production, use graph algorithms)
    source_node = next((n for n in SAMPLE_NODES if n["id"] == request.source_id), None)
    if not source_node:
        raise HTTPException(status_code=404, detail="Source node not found")
    
    # Find related transactions
    related_txs = [
        t for t in SAMPLE_TRANSACTIONS 
        if t["source"] == request.source_id and t["amount"] >= request.min_amount
    ]
    
    # Build trace path
    trace_path = {
        "source": source_node,
        "hops": [],
        "total_amount": 0.0,
        "max_risk_score": 0.0
    }
    
    for tx in related_txs[:request.max_hops]:
        target_node = next((n for n in SAMPLE_NODES if n["id"] == tx["target"]), None)
        if target_node:
            trace_path["hops"].append({
                "transaction": tx,
                "target_node": target_node
            })
            trace_path["total_amount"] += tx["amount"]
            trace_path["max_risk_score"] = max(trace_path["max_risk_score"], tx["risk_score"])
    
    return trace_path

@app.post("/api/risk-analysis")
async def analyze_risk(request: RiskAnalysisRequest):
    """
    Perform risk analysis on an entity
    Returns risk scoring and behavioral patterns
    """
    entity_node = next((n for n in SAMPLE_NODES if n["id"] == request.entity_id), None)
    if not entity_node:
        raise HTTPException(status_code=404, detail="Entity not found")
    
    # Analyze transactions involving this entity
    related_txs = [
        t for t in SAMPLE_TRANSACTIONS 
        if t["source"] == request.entity_id or t["target"] == request.entity_id
    ]
    
    # Calculate risk metrics
    total_volume = sum(t["amount"] for t in related_txs)
    avg_risk = sum(t["risk_score"] for t in related_txs) / len(related_txs) if related_txs else 0
    
    risk_analysis = {
        "entity": entity_node,
        "period_days": request.time_range_days,
        "metrics": {
            "transaction_count": len(related_txs),
            "total_volume": total_volume,
            "average_risk_score": round(avg_risk, 2),
            "high_risk_transactions": len([t for t in related_txs if t["risk_score"] > 0.7]),
            "channels_used": list(set(t["channel"] for t in related_txs))
        },
        "risk_level": "LOW" if avg_risk < 0.3 else "MEDIUM" if avg_risk < 0.7 else "HIGH",
        "transactions": related_txs
    }
    
    return risk_analysis

@app.get("/api/statistics")
async def get_statistics():
    """Get overall system statistics"""
    return {
        "total_nodes": len(SAMPLE_NODES),
        "total_transactions": len(SAMPLE_TRANSACTIONS),
        "node_types": {
            "bank_accounts": len([n for n in SAMPLE_NODES if n["type"] == "bank_account"]),
            "pix_keys": len([n for n in SAMPLE_NODES if n["type"] == "pix_key"]),
            "crypto_wallets": len([n for n in SAMPLE_NODES if n["type"] == "crypto_wallet"]),
            "entities": len([n for n in SAMPLE_NODES if n["type"] == "entity"])
        },
        "total_volume": sum(t["amount"] for t in SAMPLE_TRANSACTIONS),
        "average_risk_score": round(
            sum(t["risk_score"] for t in SAMPLE_TRANSACTIONS) / len(SAMPLE_TRANSACTIONS),
            2
        ) if SAMPLE_TRANSACTIONS else 0
    }

@app.post("/api/explain")
async def generate_explanation(trace_data: Dict[str, Any]):
    """
    Generate AI-powered explanation for trace results
    (Simulated - in production, integrate with GenAI)
    """
    explanation = {
        "summary": "Financial flow analysis completed",
        "narrative": f"""
        Análise de fluxo financeiro detectou {len(trace_data.get('hops', []))} saltos transacionais.
        O montante total rastreado foi de R$ {trace_data.get('total_amount', 0):,.2f}.
        
        Padrão identificado: Transferências iniciadas em conta bancária tradicional,
        intermediadas via PIX e possivelmente convertidas para criptomoedas através de ponte.
        
        Nível de risco: {"BAIXO" if trace_data.get('max_risk_score', 0) < 0.3 else "MÉDIO" if trace_data.get('max_risk_score', 0) < 0.7 else "ALTO"}
        """,
        "recommendations": [
            "Verificar identidade dos beneficiários finais",
            "Analisar frequência de transações similares",
            "Investigar conexão com carteiras crypto conhecidas"
        ],
        "compliance_notes": "Análise gerada com dados sintéticos para fins de demonstração"
    }
    
    return explanation

if __name__ == "__main__":
    uvicorn.run(
        "api_main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
