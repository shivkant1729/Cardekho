def process_query(data, query):
    if query.lower() in data.columns:
        return data[query.lower()].describe().to_string()
    return "Query not found in data."
