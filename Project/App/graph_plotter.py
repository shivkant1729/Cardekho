import matplotlib.pyplot as plt

def generate_graph(data, query):
    if query.lower() in data.columns:
        fig, ax = plt.subplots()
        data[query.lower()].hist(ax=ax)
        return fig
    return None
