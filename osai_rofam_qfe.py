import json
from datetime import datetime

# 1. rofam_score — Symbolic Epistemic Bias Function
def rofam_score(text):
    """Compute a symbolic ROFAM score for the provided text.

    The score is an average of four heuristic factors describing how a
    statement frames historical narratives.
    """
    framing = 0.3 if "relocated for peace" in text else 0.8
    epistemic = 0.2 if not any(word in text for word in ["treaty", "consent"]) else 0.9
    voice = 0.5 if any(word in text for word in ["Native", "Indian"]) else 0.1
    sovereignty = 0.6 if any(word in text for word in ["land", "ancestral"]) else 0.0
    return round((framing + epistemic + voice + sovereignty) / 4, 2)

# 2. QuantumFeedbackEngine — Contradiction Detection + Logging
class QuantumFeedbackEngine:
    """Store inferences and surface contradictions across runs."""

    def __init__(self):
        """Initialize empty memory and an inference log."""
        self.memory = []
        self.inference_log = []

    def load_results(self, results_list):
        """Append previous inference results to the memory."""
        self.memory.extend(results_list)

    def detect_contradictions(self):
        """Return a list of contradictory results detected in memory."""
        contradictions = []
        seen = {}
        for entry in self.memory:
            prompt = entry['prompt']
            if prompt in seen and seen[prompt] != entry['result']:
                contradictions.append({
                    "prompt": prompt,
                    "prev": seen[prompt],
                    "new": entry['result']
                })
            seen[prompt] = entry['result']
        return contradictions

    def generate_entropy_prompts(self, contradictions):
        """Formulate follow-up prompts that question changing outputs."""
        return [
            f"Why does '{c['prompt']}' now return '{c['new']}' but previously returned '{c['prev']}'?"
            for c in contradictions
        ]

    def log_inference(self, prompt, result, score):
        """Record a model inference and its ROFAM score."""
        self.inference_log.append({
            "timestamp": datetime.utcnow().isoformat(),
            "prompt": prompt,
            "result": result,
            "confidence_score": score
        })

    def export_log(self, path="inference_log.json"):
        """Export the internal inference log as JSON."""
        with open(path, 'w') as f:
            json.dump(self.inference_log, f, indent=2)

# 3. Legal Brief Generator
def generate_brief(json_input):
    """Format results of an inference run into a markdown brief."""
    brief = "# Legal Brief Draft\n"
    brief += f"**Summary:** {json_input.get('summary')}\n"
    brief += f"**ROFAM Score:** {json_input.get('rofam_score')}\n"
    brief += f"**Contradiction Detected:** {json_input.get('contradiction')}\n"
    brief += "### Generated At:\n"
    brief += f"{json_input.get('timestamp')}\n"
    return brief

# 4. Core Runtime — Runs Symbolic Pipeline
def run_osai_rofam_pipeline(statement):
    """Run the symbolic pipeline and return a formatted legal brief."""
    qfe = QuantumFeedbackEngine()
    result = "sacred_truth" if "treaty" in statement else "disputed_memory"
    qfe.load_results([{"prompt": statement, "result": result}])
    contradictions = qfe.detect_contradictions()
    score = rofam_score(statement)
    qfe.log_inference(statement, result, score)

    return generate_brief({
        "summary": statement,
        "rofam_score": score,
        "contradiction": contradictions,
        "timestamp": datetime.utcnow().isoformat()
    })

# 5. Command Line or Agentic Entry Point
if __name__ == "__main__":
    print("🔎 O.S.A.I.–ROFAM Justice Interface")
    statement = input("Enter a historical or legal statement:\n> ")
    brief_output = run_osai_rofam_pipeline(statement)
    print("\n===== 📜 Legal Brief Output =====\n")
    print(brief_output)
