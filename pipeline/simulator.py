import time
import streamlit as st

def run_pipeline(pipeline_steps):
    st.markdown("### 🚀 Running Pipeline...")
    for step in pipeline_steps:
        st.write(f"➡️ **{step['type'].upper()}** `{step['id']}`")
        time.sleep(0.7)
        st.success(f"✅ Finished `{step['id']}`")