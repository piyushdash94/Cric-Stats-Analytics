from __future__ import annotations

from typing import Tuple

import pandas as pd

from models.raw_data_models import RawCommentaryData

EVENT_RUN_MAP = {
    ".": 0,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "6": 6,
}


def parse_event(event: str) -> Tuple[int, int]:
    """Return runs and wicket flag for an event string."""
    e = event.upper().strip()
    wicket = 1 if "W" in e else 0
    e = e.replace("W", "")
    runs = EVENT_RUN_MAP.get(e, 0)
    return runs, wicket


def compute_scorecard(data: RawCommentaryData) -> pd.DataFrame:
    """Return cumulative runs and wickets as a DataFrame."""
    if not data.over_data:
        raise ValueError("over_data missing in commentary")
    runs = 0
    wickets = 0
    records = []
    for item in sorted(data.over_data.commentary, key=lambda i: i.ball):
        r, w = parse_event(item.event)
        runs += r
        wickets += w
        records.append({"ball": item.ball, "runs": runs, "wickets": wickets})
    df = pd.DataFrame(records)
    df["over"] = data.over_data.over_number
    return df


def plot_scorecard(df: pd.DataFrame, save_path: str | None = None):
    """Plot cumulative runs and wickets."""
    import matplotlib.pyplot as plt

    fig, ax1 = plt.subplots()
    ax1.plot(df["ball"], df["runs"], marker="o", label="Runs")
    ax1.set_xlabel("Ball")
    ax1.set_ylabel("Cumulative Runs")

    ax2 = ax1.twinx()
    ax2.step(df["ball"], df["wickets"], where="post", color="red", label="Wickets")
    ax2.set_ylabel("Wickets")

    fig.legend(loc="best")

    if save_path:
        fig.savefig(save_path)
    return fig
