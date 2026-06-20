"""
app.py - API Router / Controller for PHES-Web
Handles HTTP routing, parameter normalization,
alert threshold evaluation, and JSON serialization.
All data access is delegated to database.py (NFR2).
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from database import get_dashboard_data

app = Flask(__name__)
CORS(app)

# Alert threshold constant (FR3).
# Defined here as a named constant so it can be
# adjusted in one place without searching logic code.
ALERT_THRESHOLD = 50.0


@app.route('/api/dashboard', methods=['GET'])
def dashboard():
    """
    GET /api/dashboard
    Optional query parameter: ?emotion=<category>
    Case-insensitive. Returns aggregated sentiment
    metrics and any active threshold alerts.

    Response schema:
    {
        "status": "success",
        "data": [
            {
                "date": "YYYY-MM-DD",
                "category": "string",
                "count": int,
                "percentage": float
            }
        ],
        "alerts_triggered": [
            {
                "alert_id": "WARN_SPIKE",
                "category": "string",
                "date": "YYYY-MM-DD",
                "value": float,
                "message": "string"
            }
        ]
    }
    """
    # FR2: case-insensitive normalization in the controller layer
    raw_filter = request.args.get('emotion', None)
    emotion_filter = raw_filter.strip().capitalize() if raw_filter else None

    try:
        metrics = get_dashboard_data(emotion_filter)

        # FR3 + FR4: evaluate alert threshold and build alert objects
        active_alerts = []
        for record in metrics:
            if record["percentage"] >= ALERT_THRESHOLD:
                active_alerts.append({
                    "alert_id": "WARN_SPIKE",
                    "category": record["category"],
                    "date": record["date"],
                    "value": record["percentage"],
                    "message": (
                        f"Alert: High volume of public {record['category']} "
                        f"detected on {record['date']} ({record['percentage']}%)."
                    )
                })

        return jsonify({
            "status": "success",
            "data": metrics,
            "alerts_triggered": active_alerts
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=5000)
