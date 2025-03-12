import gradio as gr
import pandas as pd
import os
from app.csv_handler import handle_csv_upload
from app.query_processor import process_query
from app.graph_plotter import generate_graph

def query_interface(file, query):
    if file is None:
        file_path = "data/Housing.csv"
    else:
        file_path = file.name
    
    data = handle_csv_upload(file_path)
    if isinstance(data, str):
        return data, None
    answer = process_query(data, query)
    graph = generate_graph(data, query)
    return answer, graph

demo = gr.Interface(
    fn=query_interface,
    inputs=[gr.File(optional=True), gr.Textbox(label='Ask a question')],
    outputs=[gr.Textbox(label='Answer'), gr.Plot()],
)

if __name__ == "__main__":
    demo.launch()