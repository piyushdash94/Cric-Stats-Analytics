from pathlib import Path

from src.extract_data import extract_data
from models.raw_data_models import RawCommentaryData

BASE_DIR = Path(__file__).resolve().parent.parent
COMMENTARY_DATA_FILE = BASE_DIR / "data" / "ind_inning4_over96_aus_vs_ind_gabba_test.json"


def test_extract_data_parses_raw_data():
    commentary_data = extract_data(file_path=COMMENTARY_DATA_FILE)
    assert commentary_data is not None
    assert isinstance(commentary_data, RawCommentaryData)
    assert len(commentary_data.over_data.commentary) > 0
