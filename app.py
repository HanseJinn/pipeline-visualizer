import streamlit as st
from pipeline.loader import load_pipeline_config
from pipeline.visualizer import draw_pipeline
from pipeline.simulator import run_pipeline

st.set_page_config(page_title="Data Pipeline Visualizer", layout="wide")
st.title("🧩 Data Pipeline Visualizer & Simulator")

uploaded_file = st.file_uploader("Upload pipeline config (YAML)", type="yaml")

if uploaded_file:
    with open("configs/uploaded.yaml", "wb") as f:
        f.write(uploaded_file.getvalue())
    config_path = "configs/uploaded.yaml"
else:
    st.sidebar.info("Using example config")
    config_path = "configs/example_pipeline.yaml"

pipeline = load_pipeline_config(config_path)

if pipeline:
    st.subheader("📊 Pipeline Graph")
    draw_pipeline(pipeline)

    if st.button("▶️ Run Pipeline Simulation"):
        run_pipeline(pipeline)