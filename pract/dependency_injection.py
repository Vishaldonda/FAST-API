
def get_query_param(q: str = None):
    return q

@app.get("/items/")
def read_items(query: str = Depends(get_query_param)):
    return {"query_value": query}

@app.get("/users/")
def read_users(query: str = Depends(get_query_param)):
    return {"query_value": query}
  
