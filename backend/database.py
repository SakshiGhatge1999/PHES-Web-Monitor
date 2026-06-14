"""
database.py - Data Engine Module for PHES-Web
Simulates PostgreSQL data layer retrieval.
Returns structured public health sentiment trends.
All raw data and aggregation logic is isolated here
to satisfy NFR2 (architectural modularity).
"""


def get_dashboard_data(emotion_filter=None):
    """
    Simulates PostgreSQL data layer retrieval.
    Returns structured public health sentiment trends
    for a 30-day monitoring window (2026-05-01 to 2026-05-30).

    Categories: Anxiety, Confusion, Distrust, Fear, Acceptance
    At least 3 records intentionally exceed ALERT_THRESHOLD (50.0)
    to demonstrate the alert engine under realistic conditions.

    Args:
        emotion_filter (str or None): Optional category name.
            If provided, only records matching that category are returned.
            Matching is case-insensitive (normalization applied in app.py).

    Returns:
        list[dict]: List of records with keys:
            date (str): YYYY-MM-DD
            category (str): emotional classification label
            count (int): occurrence frequency
            percentage (float): relative volume for that date
    """
    mock_db_data = [
        # --- May 01 ---
        {"date": "2026-05-01", "category": "Anxiety",    "count": 140, "percentage": 35.0},
        {"date": "2026-05-01", "category": "Confusion",  "count": 100, "percentage": 25.0},
        {"date": "2026-05-01", "category": "Distrust",   "count":  60, "percentage": 15.0},
        {"date": "2026-05-01", "category": "Fear",       "count":  80, "percentage": 20.0},
        {"date": "2026-05-01", "category": "Acceptance", "count":  20, "percentage":  5.0},
        # --- May 02 ---
        {"date": "2026-05-02", "category": "Anxiety",    "count": 130, "percentage": 32.5},
        {"date": "2026-05-02", "category": "Confusion",  "count": 110, "percentage": 27.5},
        {"date": "2026-05-02", "category": "Distrust",   "count":  70, "percentage": 17.5},
        {"date": "2026-05-02", "category": "Fear",       "count":  70, "percentage": 17.5},
        {"date": "2026-05-02", "category": "Acceptance", "count":  20, "percentage":  5.0},
        # --- May 05 (Confusion spike — threshold breach 1) ---
        {"date": "2026-05-05", "category": "Anxiety",    "count":  80, "percentage": 20.0},
        {"date": "2026-05-05", "category": "Confusion",  "count": 210, "percentage": 52.5},
        {"date": "2026-05-05", "category": "Distrust",   "count":  50, "percentage": 12.5},
        {"date": "2026-05-05", "category": "Fear",       "count":  40, "percentage": 10.0},
        {"date": "2026-05-05", "category": "Acceptance", "count":  20, "percentage":  5.0},
        # --- May 10 ---
        {"date": "2026-05-10", "category": "Anxiety",    "count": 150, "percentage": 37.5},
        {"date": "2026-05-10", "category": "Confusion",  "count":  90, "percentage": 22.5},
        {"date": "2026-05-10", "category": "Distrust",   "count":  80, "percentage": 20.0},
        {"date": "2026-05-10", "category": "Fear",       "count":  60, "percentage": 15.0},
        {"date": "2026-05-10", "category": "Acceptance", "count":  20, "percentage":  5.0},
        # --- May 14 (Fear spike — threshold breach 2) ---
        {"date": "2026-05-14", "category": "Anxiety",    "count":  70, "percentage": 17.5},
        {"date": "2026-05-14", "category": "Confusion",  "count":  60, "percentage": 15.0},
        {"date": "2026-05-14", "category": "Distrust",   "count":  40, "percentage": 10.0},
        {"date": "2026-05-14", "category": "Fear",       "count": 204, "percentage": 51.0},
        {"date": "2026-05-14", "category": "Acceptance", "count":  26, "percentage":  6.5},
        # --- May 18 ---
        {"date": "2026-05-18", "category": "Anxiety",    "count": 160, "percentage": 40.0},
        {"date": "2026-05-18", "category": "Confusion",  "count":  80, "percentage": 20.0},
        {"date": "2026-05-18", "category": "Distrust",   "count":  60, "percentage": 15.0},
        {"date": "2026-05-18", "category": "Fear",       "count":  60, "percentage": 15.0},
        {"date": "2026-05-18", "category": "Acceptance", "count":  40, "percentage": 10.0},
        # --- May 22 (Confusion spike — threshold breach 3) ---
        {"date": "2026-05-22", "category": "Anxiety",    "count":  60, "percentage": 15.0},
        {"date": "2026-05-22", "category": "Confusion",  "count": 212, "percentage": 53.0},
        {"date": "2026-05-22", "category": "Distrust",   "count":  48, "percentage": 12.0},
        {"date": "2026-05-22", "category": "Fear",       "count":  60, "percentage": 15.0},
        {"date": "2026-05-22", "category": "Acceptance", "count":  20, "percentage":  5.0},
        # --- May 26 ---
        {"date": "2026-05-26", "category": "Anxiety",    "count": 120, "percentage": 30.0},
        {"date": "2026-05-26", "category": "Confusion",  "count":  80, "percentage": 20.0},
        {"date": "2026-05-26", "category": "Distrust",   "count":  80, "percentage": 20.0},
        {"date": "2026-05-26", "category": "Fear",       "count":  80, "percentage": 20.0},
        {"date": "2026-05-26", "category": "Acceptance", "count":  40, "percentage": 10.0},
        # --- May 30 ---
        {"date": "2026-05-30", "category": "Anxiety",    "count": 100, "percentage": 25.0},
        {"date": "2026-05-30", "category": "Confusion",  "count":  80, "percentage": 20.0},
        {"date": "2026-05-30", "category": "Distrust",   "count":  80, "percentage": 20.0},
        {"date": "2026-05-30", "category": "Fear",       "count":  80, "percentage": 20.0},
        {"date": "2026-05-30", "category": "Acceptance", "count":  60, "percentage": 15.0},
    ]

    if emotion_filter:
        return [
            row for row in mock_db_data
            if row["category"].lower() == emotion_filter.lower()
        ]
    return mock_db_data
