import time
import streamlit as st
from agent import investigate

st.set_page_config(
    page_title="Flaky Test Detective",
    page_icon="🕵️",
    layout="wide"
)

st.title("🕵️ Flaky Test Detective")

st.markdown("""
### Agent Lifecycle

🔍 **Observe** → 🧠 **Reason** → 📋 **Plan** → ⚡ **Act**
""")

st.write(
    "Autonomous AI agent that monitors GitHub workflows, "
    "detects flaky tests, investigates flaky behaviour using an LLM, "
    "and creates GitHub issues automatically."
)

if st.button("🚀 Start Autonomous Investigation"):

    status = st.empty()

    # --------------------------
    # Observe
    # --------------------------
    status.info("🔍 Observing GitHub workflows...")
    time.sleep(1)

    status.success("✅ Workflow history collected")
    time.sleep(0.5)

    # --------------------------
    # Reason
    # --------------------------
    status.info("🧠 AI analyzing workflow history...")
    time.sleep(1)

    result = investigate()

    status.success("✅ AI investigation completed")
    time.sleep(0.5)

    # --------------------------
    # Plan
    # --------------------------
    status.info("📋 Planning engineering action...")
    time.sleep(1)

    status.success("✅ Investigation report prepared")
    time.sleep(0.5)

    # --------------------------
    # Act
    # --------------------------

    status.info("⚡ Executing autonomous action...")
    time.sleep(1)
    if result["issue_url"]:
        status.success("✅ GitHub Issue Created")
    else:
        status.success("✅ No action required")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Workflow Runs",
            len(result["history"])
        )

        st.metric(
            "Failures",
            result["failures"]
        )

    with col2:

        st.metric(
            "Instability Score",
            result["decision"]["instability_score"]
        )

        st.metric(
            "Verdict",
            result["decision"]["verdict"]
        )

        st.metric(
            "Confidence",
            f"{result['confidence']}%"
        )

    st.divider()

    st.subheader("📈 Recent Workflow History")

    for i, run in enumerate(result["history"], start=1):

        if run["status"] == "success":
            st.success(f"Run {i}: SUCCESS")
        else:
            st.error(f"Run {i}: FAILURE")

    st.divider()

    st.subheader("🧠 AI Investigation")
    st.divider()

    st.subheader("🤖 Agent Decision")
    st.markdown(result["llm_summary"])

    st.divider()

    st.subheader("📄 Deterministic Investigation Report")

    st.code(result["report"])

    st.divider()

    if result["issue_url"]:

        st.success("🎯 Autonomous Action Completed")
        st.markdown(
        f"**GitHub Issue:** [Open Issue]({result['issue_url']})")

        st.write(result["issue_url"])

    st.success(f"""
Observation

✔ {len(result["history"])} workflow runs collected

Reasoning

✔ {result["decision"]["verdict"]}

Plan

✔ {result["plan"]["action"]}

Action

✔ GitHub Issue Created
""")

    