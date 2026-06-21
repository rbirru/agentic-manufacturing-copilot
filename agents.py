from langchain_ollama import ChatOllama
from rag import retrieve_context

llm = ChatOllama(model="llama3", temperature=0.2)

def retrieval_agent(question):
    context, sources = retrieve_context(question)
    return context, sources

def root_cause_agent(question, context):
    prompt = f"""
You are a Manufacturing Root Cause Agent.

Problem:
{question}

Relevant manufacturing context:
{context}

Identify the most likely root causes.
Rank them from most likely to least likely.
Explain briefly.
"""

    return llm.invoke(prompt).content

def planning_agent(question, root_causes):
    prompt = f"""
You are a Manufacturing Action Planning Agent.

Problem:
{question}

Root causes:
{root_causes}

Create a practical investigation plan for a manufacturing engineer.
Use numbered steps.
"""

    return llm.invoke(prompt).content

def report_agent(question, context, root_causes, plan):
    prompt = f"""
You are a Manufacturing Engineering Copilot.

Create a concise engineering report.

Issue:
{question}

Retrieved knowledge:
{context}

Root cause analysis:
{root_causes}

Investigation plan:
{plan}

Format:
1. Problem Summary
2. Likely Root Causes
3. Recommended Checks
4. Corrective Actions
5. Management Summary
"""

    return llm.invoke(prompt).content

def kpi_agent(question, root_causes, plan):
    prompt = f"""
You are a Manufacturing KPI Agent.

Manufacturing issue:
{question}

Root cause analysis:
{root_causes}

Investigation plan:
{plan}

Estimate the manufacturing impact using this format:

1. Risk Level: Low / Medium / High
2. Production Impact: Low / Medium / High
3. Quality Impact: Low / Medium / High
4. Recommended Escalation Level: Mechanic / Manufacturing Engineer / Lead Engineer / Manager
5. Reasoning: Brief explanation
"""

    return llm.invoke(prompt).content

def run_copilot(question):
    context, sources = retrieval_agent(question)

    root_causes = root_cause_agent(question, context)

    plan = planning_agent(question, root_causes)

    kpis = kpi_agent(question, root_causes, plan)

    report = report_agent(question, context, root_causes, plan)

    return {
        "context": context,
        "sources": sources,
        "root_causes": root_causes,
        "plan": plan,
        "kpis": kpis,
        "report": report
    }