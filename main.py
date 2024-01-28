from src.extract_data import extract_data

COMMENTARY_DATA_FILE = "data/ind_inning4_over96_aus_vs_ind_gabba_test.json"

if __name__ == "__main__":
    commentary_data = extract_data(file_path=COMMENTARY_DATA_FILE)

