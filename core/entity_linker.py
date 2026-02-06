"""
BridgeTrace AI
Core Module: Entity Linker

This module is responsible for probabilistic correlation between
banking entities and crypto wallets based on behavioral similarity.

No direct identity matching is performed.
"""

from typing import Dict


def calculate_similarity_score(
    bank_entity: Dict,
    crypto_entity: Dict
) -> int:
    """
    Calculates a probabilistic similarity score (0–100) between
    a banking entity and a crypto entity based on behavioral patterns.
    """

    score = 0

    # Geographic correlation
    if bank_entity.get("geo") == crypto_entity.get("geo"):
        score += 30

    # Behavioral risk correlation
    score += min(
        abs(bank_entity.get("behavior_score", 0) -
            crypto_entity.get("behavior_score", 0)),
        20
    )

    # Activity hour overlap
    bank_hours = set(bank_entity.get("active_hours", []))
    crypto_hours = set(crypto_entity.get("active_hours", []))
    if bank_hours & crypto_hours:
        score += 25

    # Transaction value proximity
    if abs(
        bank_entity.get("avg_transaction_value", 0) -
        crypto_entity.get("avg_transaction_value", 0)
    ) < 300:
        score += 25

    return min(score, 100)


def link_entities(
    bank_entities: Dict,
    crypto_entities: Dict,
    threshold: int = 60
) -> Dict:
    """
    Generates probabilistic links between bank entities and crypto wallets
    when similarity exceeds a defined threshold.
    """

    links = {}

    for bank_id, bank_data in bank_entities.items():
        for crypto_id, crypto_data in crypto_entities.items():
            similarity = calculate_similarity_score(bank_data, crypto_data)

            if similarity >= threshold:
                links[(bank_id, crypto_id)] = similarity

    return links
