import streamlit as st
from agents import run_copilot

st.set_page_config(
    page_title="Agentic Manufacturing Copilot",
    layout="wide"
)

st.title("Agentic Manufacturing Copilot")

st.write(
    "AI assistant for manufacturing issue diagnosis, root-cause analysis, "
    "KPI assessment, and corrective action planning."
)

question = st.text_area(
    "Describe the manufacturing issue:",
    placeholder="Example: Station 3 is seeing repeated hole-quality defects on the wing spar. What should we check first?",
    height=120
)

if st.button("Run Copilot"):

    if not question.strip():

        st.warning("Please enter a manufacturing issue.")

    else:

        with st.spinner(
            "Running multi-agent workflow: Retrieval → Root Cause → Planning → KPI → Report"
        ):

            result = run_copilot(question)

        st.success("Retrieval Agent completed")
        with st.expander("Retrieval Agent"):
            st.write(result["context"])

        st.success("Root Cause Agent completed")
        with st.expander("Root Cause Agent"):
            st.write(result["root_causes"])

        st.success("Planning Agent completed")
        with st.expander("Planning Agent"):
            st.write(result["plan"])

        st.success("KPI Agent completed")
        with st.expander("Manufacturing KPI Agent", expanded=True):
            st.write(result["kpis"])

        st.success("Report Agent completed")
        with st.expander("Final Engineering Report", expanded=True):
            st.write(result["report"])
   
