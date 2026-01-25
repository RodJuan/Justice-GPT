from fastapi import FastAPI
# Importamos la lógica que creaste en la otra carpeta
from ocr_models.benchmarks import calculate_innocence_score

app = FastAPI(title="Justice-GPT Sentinel API")

@app.get("/")
def home():
    return {
        "status": "Sentinel System Active",
        "version": "1.0.1",
        "collaboration": "Human Architect + Gemini 3 Flash + Grok"
    }

@app.post("/analyze-case")
def analyze_case(case_data: dict):
    """
    Endpoint para que abogados o devs envíen datos de un caso 
    y reciban el puntaje de inocencia inicial.
    """
    score = calculate_innocence_score(case_data)
    return {
        "innocence_score": score,
        "priority_level": "High" if score > 70 else "Standard",
        "next_steps": "Check for procedural anomalies or coerced confession patterns."
    }
