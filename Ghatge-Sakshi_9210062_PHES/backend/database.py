def fetch_aggregated_metrics(emotion_filter=None):
    """
    Simulates PostgreSQL data layer retrieval. 
    Returns structured public health sentiment trends.
    """
    mock_db_data = [
        {"date": "2026-05-12", "category": "Confusion", "count": 120, "percentage": 30.0},
        {"date": "2026-05-13", "category": "Anxiety", "count": 180, "percentage": 45.0},
        {"date": "2026-05-14", "category": "Anger", "count": 220, "percentage": 55.0}, 
        {"date": "2026-05-15", "category": "Trust", "count": 80, "percentage": 20.0}
    ]
    
    if emotion_filter:
        return [row for row in mock_db_data if row["category"].lower() == emotion_filter.lower()]
    return mock_db_data