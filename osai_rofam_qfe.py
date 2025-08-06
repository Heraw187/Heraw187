import json
from datetime import datetime

# 1. ROFAMScore — Symbolic Epistemic Bias Function
def ROFAMScore(text):
    framing = 0.3 if "relocated for peace" in text else 0.8
    epistemic = 0.2 if not any(word in text for word in ["treaty", "consent"]) else 0.9
    voice = 0.5 if any(word in text for word in ["Native", "Indian"]) else 0.1
    sovereignty = 0.6 if any(word in text for word in ["land", "ancestral"]) else 0.0
    return round((framing + epistemic + voice + sovereignty) / 4, 2)

# 2. QuantumFeedbackEngine — Contradiction Detection + Logging
class QuantumFeedbackEngine:
    def __init__(self):
        self.memory = []
        self.inference_log = []

    def load_results(self, results_list):
        self.memory.extend(results_list)

    def detect_contradictions(self):
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
        return [
            f"Why does '{c['prompt']}' now return '{c['new']}' but previously returned '{c['prev']}'?"
            for c in contradictions
        ]

    def log_inference(self, prompt, result, score):
        self.inference_log.append({
            "timestamp": datetime.utcnow().isoformat(),
            "prompt": prompt,
            "result": result,
            "confidence_score": score
        })

    def export_log(self, path="inference_log.json"):
        with open(path, 'w') as f:
            json.dump(self.inference_log, f, indent=2)

# 3. Legal Brief Generator
def generate_brief(json_input):
    brief = "# Legal Brief Draft\n"
    brief += f"**Summary:** {json_input.get('summary')}\n"
    brief += f"**ROFAM Score:** {json_input.get('rofam_score')}\n"
    brief += f"**Contradiction Detected:** {json_input.get('contradiction')}\n"
    brief += "### Generated At:\n"
    brief += f"{json_input.get('timestamp')}\n"
    return brief

# 4. Core Runtime — Runs Symbolic Pipeline
def run_osai_rofam_pipeline(statement):
    qfe = QuantumFeedbackEngine()
    result = "sacred_truth" if "treaty" in statement else "disputed_memory"
    qfe.load_results([{"prompt": statement, "result": result}])
    contradictions = qfe.detect_contradictions()
    rofam_score = ROFAMScore(statement)
    qfe.log_inference(statement, result, rofam_score)

    return generate_brief({
        "summary": statement,
        "rofam_score": rofam_score,
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
