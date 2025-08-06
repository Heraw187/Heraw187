import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from osai_rofam_qfe import ROFAMScore, QuantumFeedbackEngine, run_osai_rofam_pipeline


def test_rofam_score_keywords():
    text = "treaty land Native"
    score = ROFAMScore(text)
    assert 0 <= score <= 1


def test_qfe_contradictions():
    qfe = QuantumFeedbackEngine()
    qfe.load_results([
        {"prompt": "A", "result": "x"},
        {"prompt": "A", "result": "y"},
    ])
    cons = qfe.detect_contradictions()
    assert len(cons) == 1
    assert cons[0]['prev'] == 'x'
    assert cons[0]['new'] == 'y'


def test_run_pipeline_generates_brief():
    brief = run_osai_rofam_pipeline("test treaty")
    assert "Legal Brief Draft" in brief
    assert "ROFAM Score" in brief
