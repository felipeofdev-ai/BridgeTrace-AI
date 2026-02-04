from fastapi import FastAPI
from core.pipeline import BridgeTracePipeline

app = FastAPI(title="BridgeTrace AI")

pipeline = BridgeTracePipeline()


@app.post("/analyze")
def analyze(records: list):
    return pipeline.run(records)
