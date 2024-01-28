from src.prepare_data import prepare_data
from models.raw_data_models import RawCommentaryData

COMMENTARY_DATA_FILE = "../data/ind_inning4_over96_aus_vs_ind_gabba_test.json"


def test_prepare_data_parses_raw_data():
    commentary_data = prepare_data(file_path=COMMENTARY_DATA_FILE)
    assert commentary_data is not None
    assert isinstance(commentary_data, RawCommentaryData)
    assert len(commentary_data.over_data.commentary) > 0
