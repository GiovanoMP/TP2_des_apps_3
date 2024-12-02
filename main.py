from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM  # Correção aqui
import uvicorn

app = FastAPI(title="Tradutor EN-DE")

class TranslationRequest(BaseModel):
    text: str

# Carregando o modelo e tokenizer
try:
    model_name = "Helsinki-NLP/opus-mt-en-de"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)  # Correção aqui
    translator = pipeline("translation", model=model, tokenizer=tokenizer)
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")
    translator = None

@app.post("/translate")
async def translate(request: TranslationRequest):
    if translator is None:
        raise HTTPException(
            status_code=500, 
            detail="Modelo não carregado corretamente"
        )
    
    try:
        result = translator(request.text)
        return {"translated_text": result[0]['translation_text']}
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Erro na tradução: {str(e)}"
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
