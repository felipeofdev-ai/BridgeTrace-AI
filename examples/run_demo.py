from core.pipeline import BridgeTracePipeline


if __name__ == "__main__":
    sample_records = [
        {"entity": "user_123", "type": "pix", "amount": 12000, "to": "wallet_abc"},
        {"entity": "wallet_abc", "type": "crypto", "amount": 0.8, "to": "exchange_xyz"},
        {"entity": "exchange_xyz", "type": "bank", "amount": 45000, "to": "account_999"}
    ]

    pipeline = BridgeTracePipeline()
    result = pipeline.run(sample_records)

    print("Risk Score:", result["risk_score"])
    print("Explanation:", result["explanation"])
