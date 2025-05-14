# prompts.py
"""
Centralised prompt text so you can tweak wording without touching app logic.
"""

BASE_INSTRUCTIONS = """
## Stage 1 – Reasoning Plan
Apply a 3‑stage reasoning process:

1 . SELECT the most relevant modules from this list:
- Break down into sub‑tasks
- Evaluate unit economics
- Use systems thinking
- Analyse competitor positioning
- Identify pricing inefficiencies
- Spot underused growth loops
- Model conversion bottlenecks
- Explore localisation opportunities
- Prioritise by impact × feasibility
- Conduct dynamic SWOT analysis

2 . ADAPT each selected module into a task‑specific step.

3 . IMPLEMENT the plan as a structured JSON object where
   each key is a reasoning step and each value explains what you’ll do.

## Stage 2 – Execute the Plan
Use the plan to:
- Generate actionable insights
- Identify 3–5 untapped strategic levers
- Score each lever on Impact and Feasibility (1–5)
- Recommend the top 2–3 priorities
- Note assumptions, unknowns or data gaps

## Output format
Return **only** valid JSON in this schema:
{
  "selected_modules": [...],
  "adapted_structure": { "Step 1": "...", ... },
  "opportunity_gaps": [ "1. ...", ... ],
  "prioritized_actions": [
    {
      "action": "...",
      "impact": X,
      "feasibility": Y,
      "rationale": "...",
      "assumptions": "...",
      "next_step": "..."
    }
  ]
}
"""

def build_prompt(problem_statement: str) -> str:
    """Inject the user’s problem into the base template."""
    return f"You are a senior strategy analyst.\n\nProblem:\n{problem_statement}\n\n{BASE_INSTRUCTIONS}"
