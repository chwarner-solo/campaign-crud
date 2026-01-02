from fastapi import FastAPI
from pygments.lexer import include

from campaign_crud.adapters.http.npc_controller import router as npc_router

app = FastAPI(
    title="Campaign CRUD",
    description="Narrative infrastructure for tabletop RPGs",
    version="0.0.1",
)

app.include_router(npc_router)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)