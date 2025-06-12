# MCP queries, Cypher builders

from gqlalchemy import Memgraph 

def run_query(cypher: str):
    db = Memgraph()
    return list(db.execute_and_fetch(cypher))