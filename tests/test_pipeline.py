from core.pipeline import BridgeTracePipeline


def test_pipeline_runs():
    pipeline = BridgeTracePipeline()
    data = [{"entity": "test", "type": "pix", "amount": 100, "to": "x"}]

    result = pipeline.run(data)

    assert "risk_score" in result
    assert "explanation" in result
