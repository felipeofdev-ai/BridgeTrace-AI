# Data Layer – Synthetic Financial Datasets

This directory contains **fully synthetic datasets** used by BridgeTrace AI to simulate
financial flows across banking systems (including PIX) and blockchain environments.

No real data is used or referenced.

---

## 🎯 Purpose of the Data Layer

The datasets in this folder are designed to:

- Simulate realistic financial behaviors
- Enable graph-based traceability experiments
- Support risk analysis and explainability
- Demonstrate architectural feasibility for hybrid financial systems

All data is intentionally anonymized and artificial.

---

## 📂 Dataset Overview

### `bank_accounts.json`
Synthetic bank account profiles, including:
- Account identifiers
- Entity metadata (anonymized)
- Behavioral patterns (average transaction value, activity hours)
- Risk-related attributes (historical flags, synthetic chargebacks)

---

### `pix_transactions.json`
Simulated PIX transactions representing:
- Instant transfers between bank accounts
- Multi-hop transaction chains
- Temporal patterns used for tracing and risk scoring

Each transaction includes:
- Source and destination accounts
- Amount
- Timestamp
- Synthetic PIX key reference

---

### `crypto_wallets.json`
Synthetic blockchain wallet profiles, including:
- Wallet identifiers
- Activity metadata
- Simulated geographic and temporal behavior
- Abstracted wallet characteristics

---

### `crypto_transactions.json`
Simulated on-chain transactions representing:
- Wallet-to-wallet transfers
- Transaction value patterns
- Multi-hop blockchain paths

No real blockchain data is used.

---

### `entity_metadata.json`
Abstract entity layer used for probabilistic linking, including:
- Synthetic entity IDs
- Behavioral fingerprints
- Cross-domain attributes (banking ↔ crypto)

This dataset enables **probabilistic correlation experiments** without identity exposure.

---

## 🔒 Compliance & Ethics Notice

> - All datasets are **synthetically generated**
> - No personal, financial, or identifiable real-world data is included
> - No connection to Banco Central, PIX infrastructure, or live blockchains
> - Intended strictly for research, education, and architectural demonstration

---

## 🔬 Research Notes

The separation between:
- Transaction data
- Entity metadata
- Behavioral patterns

is intentional and reflects real-world compliance-oriented data architectures.

---

## 🧪 Extending the Data

New datasets can be added to simulate:
- Exchange bridges
- International payment rails
- Layer-2 crypto solutions
- Fraud and anomaly scenarios

Ensure all extensions remain synthetic and documented.
