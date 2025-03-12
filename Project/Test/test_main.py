import pytest
import pandas as pd
from app.csv_handler import handle_csv_upload
from app.query_processor import process_query
from app.graph_plotter import generate_graph

def test_csv_upload():
    data = handle_csv_upload("data/Housing.csv")
    assert isinstance(data, pd.DataFrame)

def test_valid_query():
    data = handle_csv_upload("data/Housing.csv")
    query = data.columns[0] 
    response = process_query(data, query)
    assert isinstance(response, str)
    assert "count" in response.lower()

def test_invalid_query():
    data = handle_csv_upload("data/Housing.csv")
    response = process_query(data, "non_existent_column")
    assert response == "Query not found in data."

def test_graph_generation():
    data = handle_csv_upload("data/Housing.csv")
    query = data.columns[0]
    graph = generate_graph(data, query)
    assert graph is not None
