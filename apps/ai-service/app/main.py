from fastapi import FastAPI

from app.preprocessing import normalize_text
from app.schemas import ClassifyRequest, ClassifyResponse

app = FastAPI(title="Agentris AI Service", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/classify", response_model=ClassifyResponse)
def classify(req: ClassifyRequest):
    _ = normalize_text(req.text)
    # TODO: ganti dengan prediksi model setelah training selesai
    return ClassifyResponse(intent="di_luar_konteks", confidence=0.0)