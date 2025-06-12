# Secure API with GPT to Memgraph Querying

from fastapi import FastAPI, Depends
from backend.auth import verify_tokens
from backend.memgraph_interface import run_query 
from backend.logger import log_access 

app = FastAPI()

@app.post('/ask')
def ask(question: str, user=Depends(verify_tokens)):
    cypher = "MATCH (a:Asset) WHERE a.patchLevel = 'low' RETURN a"
    result = run_query(cypher)
    log_access(user['username'], question)
    return result 
