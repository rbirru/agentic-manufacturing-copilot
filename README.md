# agentic-manufacturing-copilot
Multi-agent manufacturing engineering assistant using RAG, Ollama, ChromaDB, and Streamlit.

# Agentic Manufacturing Copilot

AI-powered manufacturing engineering assistant built with Retrieval-Augmented Generation (RAG), multi-agent reasoning, Ollama, ChromaDB, and Streamlit.

The system helps manufacturing engineers diagnose production issues, identify likely root causes, generate investigation plans, assess operational risk, and produce engineering reports.

---

## Overview

Manufacturing engineers often spend significant time searching through work instructions, process specifications, quality procedures, and historical corrective actions.

Agentic Manufacturing Copilot demonstrates how Large Language Models (LLMs) can be combined with Retrieval-Augmented Generation (RAG) and agent-based workflows to support manufacturing decision-making.

The application uses multiple specialized AI agents to:

- Retrieve manufacturing knowledge
- Analyze likely root causes
- Generate investigation plans
- Assess manufacturing risk and impact
- Produce engineering reports

---

## Architecture

```text
                    User
                      |
                      v
            Agentic Manufacturing Copilot
                      |
     ------------------------------------------------
     |            |            |          |         |
     v            v            v          v         v

 Retrieval    Root Cause    Planning     KPI     Report
   Agent        Agent        Agent      Agent     Agent

                      |
                      v

             Manufacturing Knowledge Base
                  (ChromaDB + RAG)
```

---

## Features

### Retrieval Agent

Searches manufacturing knowledge documents using RAG.

Example sources:

- Process specifications
- Manufacturing procedures
- Quality documents
- Corrective action reports
- Work instructions

---

### Root Cause Agent

Identifies likely causes of manufacturing defects.

Example:

- Tool wear
- Fixture misalignment
- Feed rate issues
- Spindle vibration
- Clamp looseness

---

### Planning Agent

Generates practical investigation plans.

Example output:

1. Verify tooling condition
2. Inspect fixture alignment
3. Review NC parameters
4. Measure hole quality
5. Compare with historical defects

---

### KPI Agent

Assesses manufacturing impact.

Outputs:

- Risk Level
- Production Impact
- Quality Impact
- Escalation Recommendation

---

### Report Agent

Creates a structured engineering report including:

- Problem Summary
- Root Cause Analysis
- Investigation Plan
- Corrective Actions
- Management Summary

---

## Technology Stack

### LLM

- Ollama
- Llama 3

### RAG

- ChromaDB
- Ollama Embeddings

### Frameworks

- LangChain
- Streamlit

### Language

- Python

---

## Project Structure

```text
agentic-manufacturing-copilot/

│
├── app.py
├── agents.py
├── rag.py
├── ingest.py
├── requirements.txt
├── README.md
│
├── data/
│   └── manufacturing_knowledge.txt
│
└── chroma_db/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/agentic-manufacturing-copilot.git

cd agentic-manufacturing-copilot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download:

https://ollama.com

Pull required models:

```bash
ollama pull llama3
ollama pull nomic-embed-text
```

Start Ollama:

```bash
ollama serve
```

---

## Build Knowledge Base

Place manufacturing documents inside:

```text
data/
```

Then run:

```bash
python ingest.py
```

---

## Launch Application

```bash
streamlit run app.py
```

---

## Example Query

```text
Station 3 is seeing repeated hole-quality defects on the wing spar.
What should we check first?
```

Example Output:

- Retrieved Manufacturing Context
- Root Cause Analysis
- Investigation Plan
- Manufacturing KPI Assessment
- Engineering Report

---

## Future Enhancements

- LangGraph orchestration
- Historical defect database integration
- PDF ingestion pipeline
- Quality trend analysis
- Manufacturing KPI dashboard
- Multi-user deployment
- Manufacturing knowledge graph
- Real-time factory data integration

---

## Skills Demonstrated

- Agentic AI
- Retrieval-Augmented Generation (RAG)
- Large Language Models
- Multi-Agent Systems
- Vector Databases
- Manufacturing Engineering
- Streamlit Application Development
- AI Workflow Design

---

## Author

Raj Birru
