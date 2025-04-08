import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

def draw_pipeline(pipeline_steps):
    G = nx.DiGraph()

    for i, step in enumerate(pipeline_steps):
        G.add_node(step["id"], label=step["type"])
        if i > 0:
            G.add_edge(pipeline_steps[i - 1]["id"], step["id"])

    net = Network(height="500px", directed=True)
    net.from_nx(G)
    net.show("graph.html")
    HtmlFile = open("graph.html", "r", encoding="utf-8")
    components.html(HtmlFile.read(), height=550)