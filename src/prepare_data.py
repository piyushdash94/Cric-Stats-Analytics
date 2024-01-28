import json

from pydantic import ValidationError
from models.raw_data_models import RawCommentaryData


def get_raw_data_from_json(file_path: str) -> dict:
    """
    Load raw data from json file as dict
    :param file_path: str path to json file
    :return: dict with raw data
    """
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


def prepare_data(file_path: str) -> RawCommentaryData:
    """
    Prepare raw commentary data in json file to custom RawCommentaryData data-model
    :param file_path: str path to json
    :return: data in RawCommentaryData model
    """
    commentary_data = get_raw_data_from_json(file_path)
    try:
        raw_commentary_data = RawCommentaryData.model_validate(commentary_data)
        return raw_commentary_data
    except ValidationError as e:
        raise ValidationError("Invalid JSON") from e
