from pathlib import Path

from src.extract_data import extract_data
from src.scorecard_analysis import compute_scorecard

BASE_DIR = Path(__file__).resolve().parent.parent
COMMENTARY_DATA_FILE = BASE_DIR / "data" / "ind_inning4_over96_aus_vs_ind_gabba_test.json"


def test_compute_scorecard_returns_runs_wickets():
    commentary_data = extract_data(file_path=COMMENTARY_DATA_FILE)
    df = compute_scorecard(commentary_data)
    assert df.iloc[-1]['runs'] == 11
    assert df.iloc[-1]['wickets'] == 1
