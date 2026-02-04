"""
BridgeTrace AI
Core Module: Graph Builder

This module is responsible for constructing the Unified Financial Trace Graph,
combining banking, PIX and crypto transactions into a single directed graph.

All data consumed by this module is strictly synthetic.
"""

import networkx as nx


def build_financial_graph(
    bank_accounts: list,
    pix_transactions: list,
    crypto_wallets: list,
    crypto_transactions: list
) -> nx.DiGraph:
    """
    Builds a unified directed graph representing hybrid financial flows.

    Nodes:
        - Bank accounts
        - Crypto wallets

    Edges:
        - PIX transfers
        - On-chain crypto transactions

    Each edge carries contextual metadata used for tracing and risk analysis.
    """

    graph = nx.DiGraph()

    # --- Add bank account nodes ---
    for account in bank_accounts:
        graph.add_node(
            account["account_id"],
            node_type="bank_account",
            entity_id=account["entity_id"],
            avg_transaction_value=account["avg_transaction_value"],
            active_hours=account["active_hours"],
            risk_flags=account["risk_flags"]
        )

    # --- Add crypto wallet nodes ---
    for wallet in crypto_wallets:
        graph.add_node(
            wallet["wallet_id"],
            node_type="crypto_wallet",
            entity_id=wallet["entity_id"],
            blockchain=wallet["blockchain"],
            avg_transaction_value=wallet["avg_transaction_value"],
            active_hours=wallet["active_hours"]
        )

    # --- Add PIX transaction edges ---
    for tx in pix_transactions:
        graph.add_edge(
            tx["from_account"],
            tx["to_account"],
            transaction_id=tx["transaction_id"],
            channel="PIX",
            amount=tx["amount"],
            timestamp=tx["timestamp"],
            pix_key=tx["pix_key"]
        )

    # --- Add crypto transaction edges ---
    for tx in crypto_transactions:
        graph.add_edge(
            tx["from_wallet"],
            tx["to_wallet"],
            transaction_id=tx["tx_id"],
            channel="CRYPTO",
            amount=tx["amount"],
            timestamp=tx["timestamp"],
            blockchain=tx["blockchain"]
        )

    return graph
