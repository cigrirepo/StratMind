# app.py
import os, json, streamlit as st
from prompts import build_prompt
from utils import call_openai

# ── Page setup ─────────────────────────────────────────────────────────────
st.set_page_config(page_title="StratMind AI", layout="wide")
st.title("🧠 StratMind AI – Strategic Reasoning Assistant")
st.caption("Turn messy business challenges into structured, prioritised action plans.")

# ── API key handling ───────────────────────────────────────────────────────
openai_key = os.getenv("OPENAI_API_KEY") or st.sidebar.text_input(
    "🔑 Enter your OpenAI API key", type="password"
)
if openai_key:
    import openai
    openai.api_key = openai_key
else:
    st.warning("Add your OpenAI API key in the sidebar to begin.")

# ── User input ─────────────────────────────────────────────────────────────
problem = st.text_area(
    "Describe the business challenge you want to analyse",
    placeholder="e.g. Increase user retention for our mobile app in LatAm markets …",
    height=180,
)

run_btn = st.button("Generate plan ➜", use_container_width=True)

# ── Run model ──────────────────────────────────────────────────────────────
if run_btn and problem and openai_key:
    with st.spinner("Thinking…"):
        prompt = build_prompt(problem)
        try:
            result = call_openai(prompt)
            st.success("Finished!")
            st.subheader("📋 Structured Output")
            st.json(result, expanded=False)

            # Download button
            st.download_button(
                "💾 Download JSON",
                data=json.dumps(result, indent=2),
                file_name="stratmind_output.json",
                mime="application/json",
            )

        except Exception as e:
            st.error(f"Something went wrong: {e}")
elif run_btn and not problem:
    st.error("Please describe the problem before running.")
