import os

from groq import Groq


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def investigate_with_llm(history, decision):

    workflow_history = ""

    for i, run in enumerate(history):

        workflow_history += (
            f"Run {i+1}: {run['status']}\n"
        )

    prompt = f"""
You are a Senior Site Reliability Engineer.

You are investigating whether a CI/CD failure
is caused by a flaky test.

Repository:
flaky-test-lab

Workflow History:

{workflow_history}

Deterministic Analysis:

Instability Score:
{decision["instability_score"]}

Verdict:
{decision["verdict"]}

Your task is NOT to change the verdict.

Instead, generate a structured investigation.

Return Markdown using EXACTLY these headings.

## Reasoning

Explain why the workflow history supports
(or does not support) the verdict.

## Evidence

List the important observations.

## Possible Root Causes

Provide 3–5 possible causes.

## Recommended Next Action

Suggest the best engineering action.

## Confidence

Give one confidence percentage.
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        temperature=0.2,

        messages=[
            {
                "role": "system",
                "content":
                "You are an expert DevOps engineer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    return response.choices[0].message.content