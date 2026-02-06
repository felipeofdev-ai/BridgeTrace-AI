// BridgeTrace AI - Dashboard Application Logic

const API_BASE_URL = 'http://localhost:8000/api';

// Application State
const app = {
    nodes: [],
    transactions: [],
    statistics: {},
    charts: {},
    network: null
};

// Utility Functions
function showLoading() {
    document.getElementById('loadingOverlay').style.display = 'flex';
}

function hideLoading() {
    document.getElementById('loadingOverlay').style.display = 'none';
}

function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(value);
}

function formatDate(dateString) {
    return new Date(dateString).toLocaleString('pt-BR');
}

async function fetchAPI(endpoint, options = {}) {
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, options);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        alert('Erro ao conectar com a API. Verifique se o servidor está rodando.');
        throw error;
    }
}

// Navigation
function initNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.content-section');
    
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Update active nav link
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            
            // Show corresponding section
            const sectionId = link.getAttribute('data-section');
            sections.forEach(section => {
                section.classList.remove('active');
                if (section.id === `section-${sectionId}`) {
                    section.classList.add('active');
                }
            });
        });
    });
}

// Theme Toggle
function initThemeToggle() {
    const themeToggle = document.getElementById('themeToggle');
    const icon = themeToggle.querySelector('i');
    
    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        
        if (document.body.classList.contains('dark-mode')) {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        }
    });
}

// Dashboard Functions
async function loadDashboard() {
    showLoading();
    
    try {
        // Load statistics
        const stats = await fetchAPI('/statistics');
        app.statistics = stats;
        updateStatistics(stats);
        
        // Load nodes
        const nodesData = await fetchAPI('/nodes');
        app.nodes = nodesData.nodes;
        
        // Load transactions
        const txData = await fetchAPI('/transactions');
        app.transactions = txData.transactions;
        
        // Initialize charts
        initCharts(stats);
        
        // Initialize network graph
        initNetworkGraph();
        
    } catch (error) {
        console.error('Error loading dashboard:', error);
    } finally {
        hideLoading();
    }
}

function updateStatistics(stats) {
    document.getElementById('stat-nodes').textContent = stats.total_nodes;
    document.getElementById('stat-transactions').textContent = stats.total_transactions;
    document.getElementById('stat-volume').textContent = formatCurrency(stats.total_volume);
    document.getElementById('stat-risk').textContent = stats.average_risk_score.toFixed(2);
}

function initCharts(stats) {
    // Node Distribution Pie Chart
    const nodeCtx = document.getElementById('nodeDistributionChart').getContext('2d');
    app.charts.nodeDistribution = new Chart(nodeCtx, {
        type: 'doughnut',
        data: {
            labels: ['Contas Bancárias', 'Chaves PIX', 'Carteiras Crypto', 'Entidades'],
            datasets: [{
                data: [
                    stats.node_types.bank_accounts,
                    stats.node_types.pix_keys,
                    stats.node_types.crypto_wallets,
                    stats.node_types.entities
                ],
                backgroundColor: [
                    '#2563eb',
                    '#8b5cf6',
                    '#10b981',
                    '#f59e0b'
                ]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
    
    // Channel Volume Bar Chart
    const channelCtx = document.getElementById('channelVolumeChart').getContext('2d');
    
    // Calculate volume by channel
    const channelVolumes = {};
    app.transactions.forEach(tx => {
        channelVolumes[tx.channel] = (channelVolumes[tx.channel] || 0) + tx.amount;
    });
    
    app.charts.channelVolume = new Chart(channelCtx, {
        type: 'bar',
        data: {
            labels: Object.keys(channelVolumes),
            datasets: [{
                label: 'Volume (R$)',
                data: Object.values(channelVolumes),
                backgroundColor: '#2563eb'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) {
                            return 'R$ ' + value.toLocaleString('pt-BR');
                        }
                    }
                }
            }
        }
    });
}

function initNetworkGraph() {
    const container = document.getElementById('networkGraph');
    
    // Prepare nodes for vis.js
    const visNodes = app.nodes.map(node => {
        let color = '#2563eb';
        switch(node.type) {
            case 'pix_key': color = '#8b5cf6'; break;
            case 'crypto_wallet': color = '#10b981'; break;
            case 'entity': color = '#f59e0b'; break;
        }
        
        return {
            id: node.id,
            label: node.name,
            color: color,
            shape: 'dot',
            size: 20
        };
    });
    
    // Prepare edges for vis.js
    const visEdges = app.transactions.map((tx, index) => ({
        id: index,
        from: tx.source,
        to: tx.target,
        label: formatCurrency(tx.amount),
        arrows: 'to',
        color: {
            color: tx.risk_score > 0.7 ? '#ef4444' : 
                   tx.risk_score > 0.4 ? '#f59e0b' : '#10b981',
            highlight: '#2563eb'
        },
        width: Math.max(1, tx.amount / 5000)
    }));
    
    const data = {
        nodes: new vis.DataSet(visNodes),
        edges: new vis.DataSet(visEdges)
    };
    
    const options = {
        nodes: {
            font: {
                size: 14,
                color: '#1e293b'
            },
            borderWidth: 2,
            borderWidthSelected: 4
        },
        edges: {
            font: {
                size: 12,
                align: 'middle'
            },
            smooth: {
                type: 'continuous'
            }
        },
        physics: {
            stabilization: true,
            barnesHut: {
                gravitationalConstant: -2000,
                springConstant: 0.001,
                springLength: 200
            }
        },
        interaction: {
            hover: true,
            tooltipDelay: 100
        }
    };
    
    app.network = new vis.Network(container, data, options);
    
    // Reset graph button
    document.getElementById('resetGraph').addEventListener('click', () => {
        app.network.fit();
    });
}

// Trace Functions
function initTraceForm() {
    const form = document.getElementById('traceForm');
    const sourceSelect = document.getElementById('sourceNode');
    
    // Populate source node select
    app.nodes.forEach(node => {
        const option = document.createElement('option');
        option.value = node.id;
        option.textContent = `${node.name} (${node.type})`;
        sourceSelect.appendChild(option);
    });
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const sourceId = document.getElementById('sourceNode').value;
        const maxHops = parseInt(document.getElementById('maxHops').value);
        const minAmount = parseFloat(document.getElementById('minAmount').value);
        
        showLoading();
        
        try {
            const result = await fetchAPI('/trace', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    source_id: sourceId,
                    max_hops: maxHops,
                    min_amount: minAmount
                })
            });
            
            displayTraceResults(result);
            
        } catch (error) {
            console.error('Trace error:', error);
        } finally {
            hideLoading();
        }
    });
}

function displayTraceResults(result) {
    const resultsDiv = document.getElementById('traceResults');
    const contentDiv = document.getElementById('traceResultsContent');
    
    let html = `
        <div class="trace-summary">
            <h4>Nó de Origem</h4>
            <div class="node-card">
                <div class="node-header">
                    <div class="node-icon"><i class="fas fa-circle"></i></div>
                    <div class="node-title">
                        <h4>${result.source.name}</h4>
                        <span class="node-type">${result.source.type}</span>
                    </div>
                </div>
            </div>
            
            <div class="stats-grid" style="margin-top: 1rem;">
                <div class="stat-card">
                    <div class="stat-icon transactions">
                        <i class="fas fa-route"></i>
                    </div>
                    <div class="stat-info">
                        <h3>${result.hops.length}</h3>
                        <p>Saltos Detectados</p>
                    </div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon volume">
                        <i class="fas fa-dollar-sign"></i>
                    </div>
                    <div class="stat-info">
                        <h3>${formatCurrency(result.total_amount)}</h3>
                        <p>Volume Total</p>
                    </div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon risk">
                        <i class="fas fa-exclamation-triangle"></i>
                    </div>
                    <div class="stat-info">
                        <h3>${result.max_risk_score.toFixed(2)}</h3>
                        <p>Risco Máximo</p>
                    </div>
                </div>
            </div>
            
            <h4 style="margin-top: 2rem;">Caminho de Transações</h4>
        </div>
    `;
    
    result.hops.forEach((hop, index) => {
        const tx = hop.transaction;
        const target = hop.target_node;
        
        html += `
            <div class="trace-hop" style="margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 0.5rem;">
                    <span style="font-weight: 700; color: var(--primary-color);">Salto ${index + 1}</span>
                    <i class="fas fa-arrow-right" style="color: var(--text-secondary);"></i>
                </div>
                
                <div class="node-card">
                    <div class="node-header">
                        <div class="node-icon"><i class="fas fa-circle"></i></div>
                        <div class="node-title">
                            <h4>${target.name}</h4>
                            <span class="node-type">${target.type}</span>
                        </div>
                    </div>
                    <div class="node-metadata">
                        <div class="metadata-item">
                            <span class="metadata-label">Valor:</span>
                            <span class="metadata-value">${formatCurrency(tx.amount)}</span>
                        </div>
                        <div class="metadata-item">
                            <span class="metadata-label">Canal:</span>
                            <span class="metadata-value">${tx.channel}</span>
                        </div>
                        <div class="metadata-item">
                            <span class="metadata-label">Data:</span>
                            <span class="metadata-value">${formatDate(tx.timestamp)}</span>
                        </div>
                        <div class="metadata-item">
                            <span class="metadata-label">Score de Risco:</span>
                            <span class="metadata-value" style="color: ${tx.risk_score > 0.7 ? 'var(--danger-color)' : tx.risk_score > 0.4 ? 'var(--warning-color)' : 'var(--success-color)'}">
                                ${tx.risk_score.toFixed(2)}
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        `;
    });
    
    contentDiv.innerHTML = html;
    resultsDiv.style.display = 'block';
    
    // Scroll to results
    resultsDiv.scrollIntoView({ behavior: 'smooth' });
}

// Risk Analysis Functions
function initRiskForm() {
    const form = document.getElementById('riskForm');
    const entitySelect = document.getElementById('entityNode');
    
    // Populate entity select
    app.nodes.forEach(node => {
        const option = document.createElement('option');
        option.value = node.id;
        option.textContent = `${node.name} (${node.type})`;
        entitySelect.appendChild(option);
    });
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const entityId = document.getElementById('entityNode').value;
        const timeRange = parseInt(document.getElementById('timeRange').value);
        
        showLoading();
        
        try {
            const result = await fetchAPI('/risk-analysis', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    entity_id: entityId,
                    time_range_days: timeRange
                })
            });
            
            displayRiskResults(result);
            
        } catch (error) {
            console.error('Risk analysis error:', error);
        } finally {
            hideLoading();
        }
    });
}

function displayRiskResults(result) {
    const resultsDiv = document.getElementById('riskResults');
    const contentDiv = document.getElementById('riskResultsContent');
    
    const riskColor = result.risk_level === 'HIGH' ? 'var(--danger-color)' :
                      result.risk_level === 'MEDIUM' ? 'var(--warning-color)' :
                      'var(--success-color)';
    
    let html = `
        <div class="risk-summary">
            <h4>Entidade Analisada</h4>
            <div class="node-card">
                <div class="node-header">
                    <div class="node-icon"><i class="fas fa-building"></i></div>
                    <div class="node-title">
                        <h4>${result.entity.name}</h4>
                        <span class="node-type">${result.entity.type}</span>
                    </div>
                </div>
            </div>
            
            <div style="background: ${riskColor}20; border-left: 4px solid ${riskColor}; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0;">
                <h4 style="color: ${riskColor}; margin-bottom: 0.5rem;">
                    <i class="fas fa-shield-alt"></i> Nível de Risco: ${result.risk_level}
                </h4>
                <p style="color: var(--text-secondary);">Baseado em análise de ${result.period_days} dias</p>
            </div>
            
            <div class="stats-grid" style="margin-top: 1rem;">
                <div class="stat-card">
                    <div class="stat-icon transactions">
                        <i class="fas fa-exchange-alt"></i>
                    </div>
                    <div class="stat-info">
                        <h3>${result.metrics.transaction_count}</h3>
                        <p>Transações</p>
                    </div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon volume">
                        <i class="fas fa-dollar-sign"></i>
                    </div>
                    <div class="stat-info">
                        <h3>${formatCurrency(result.metrics.total_volume)}</h3>
                        <p>Volume Total</p>
                    </div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon risk">
                        <i class="fas fa-exclamation-triangle"></i>
                    </div>
                    <div class="stat-info">
                        <h3>${result.metrics.average_risk_score.toFixed(2)}</h3>
                        <p>Score Médio</p>
                    </div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon" style="background: linear-gradient(135deg, var(--danger-color), #dc2626);">
                        <i class="fas fa-exclamation-circle"></i>
                    </div>
                    <div class="stat-info">
                        <h3>${result.metrics.high_risk_transactions}</h3>
                        <p>Transações Alto Risco</p>
                    </div>
                </div>
            </div>
            
            <h4 style="margin-top: 2rem;">Canais Utilizados</h4>
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 1rem;">
                ${result.metrics.channels_used.map(channel => 
                    `<span class="node-type">${channel}</span>`
                ).join('')}
            </div>
            
            <h4 style="margin-top: 2rem;">Histórico de Transações</h4>
        </div>
    `;
    
    result.transactions.forEach((tx, index) => {
        html += `
            <div class="node-card" style="margin-bottom: 1rem;">
                <div class="node-metadata">
                    <div class="metadata-item">
                        <span class="metadata-label">Transação ${index + 1}:</span>
                        <span class="metadata-value">${tx.source} → ${tx.target}</span>
                    </div>
                    <div class="metadata-item">
                        <span class="metadata-label">Valor:</span>
                        <span class="metadata-value">${formatCurrency(tx.amount)}</span>
                    </div>
                    <div class="metadata-item">
                        <span class="metadata-label">Canal:</span>
                        <span class="metadata-value">${tx.channel}</span>
                    </div>
                    <div class="metadata-item">
                        <span class="metadata-label">Risco:</span>
                        <span class="metadata-value" style="color: ${tx.risk_score > 0.7 ? 'var(--danger-color)' : tx.risk_score > 0.4 ? 'var(--warning-color)' : 'var(--success-color)'}">
                            ${tx.risk_score.toFixed(2)}
                        </span>
                    </div>
                </div>
            </div>
        `;
    });
    
    contentDiv.innerHTML = html;
    resultsDiv.style.display = 'block';
    
    // Scroll to results
    resultsDiv.scrollIntoView({ behavior: 'smooth' });
}

// Nodes Management
function initNodesManagement() {
    loadNodes();
    
    document.getElementById('nodeTypeFilter').addEventListener('change', () => {
        loadNodes();
    });
    
    document.getElementById('refreshNodes').addEventListener('click', () => {
        loadNodes();
    });
}

async function loadNodes() {
    const filterType = document.getElementById('nodeTypeFilter').value;
    
    showLoading();
    
    try {
        const endpoint = filterType ? `/nodes?node_type=${filterType}` : '/nodes';
        const data = await fetchAPI(endpoint);
        
        displayNodes(data.nodes);
        
    } catch (error) {
        console.error('Error loading nodes:', error);
    } finally {
        hideLoading();
    }
}

function displayNodes(nodes) {
    const grid = document.getElementById('nodesGrid');
    
    if (nodes.length === 0) {
        grid.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">Nenhum nó encontrado</p>';
        return;
    }
    
    grid.innerHTML = nodes.map(node => {
        const icon = {
            'bank_account': 'fa-building',
            'pix_key': 'fa-key',
            'crypto_wallet': 'fa-wallet',
            'entity': 'fa-building'
        }[node.type] || 'fa-circle';
        
        const metadataHtml = Object.entries(node.metadata)
            .map(([key, value]) => `
                <div class="metadata-item">
                    <span class="metadata-label">${key}:</span>
                    <span class="metadata-value">${value}</span>
                </div>
            `).join('');
        
        return `
            <div class="node-card">
                <div class="node-header">
                    <div class="node-icon">
                        <i class="fas ${icon}"></i>
                    </div>
                    <div class="node-title">
                        <h4>${node.name}</h4>
                        <span class="node-type">${node.type}</span>
                    </div>
                </div>
                <div class="node-metadata">
                    ${metadataHtml}
                </div>
            </div>
        `;
    }).join('');
}

// Initialize Application
async function init() {
    showLoading();
    
    try {
        // Initialize navigation
        initNavigation();
        
        // Initialize theme toggle
        initThemeToggle();
        
        // Load dashboard data
        await loadDashboard();
        
        // Initialize forms
        initTraceForm();
        initRiskForm();
        initNodesManagement();
        
    } catch (error) {
        console.error('Initialization error:', error);
    } finally {
        hideLoading();
    }
}

// Start application when DOM is ready
document.addEventListener('DOMContentLoaded', init);
