from flask import Flask, jsonify, request
from flask_cors import CORS
from database import fetch_aggregated_metrics

app = Flask(__name__)
CORS(app)  

ALERT_THRESHOLD = 50.0

@app.route('/api/dashboard', methods=['GET'])
def get_dashboard_data():
    emotion_filter = request.args.get('emotion', None)
    try:
        metrics = fetch_aggregated_metrics(emotion_filter)
        active_alerts = []
        for log in metrics:
            if log["percentage"] >= ALERT_THRESHOLD:
                active_alerts.append({
                    "alert_id": "WARN_SPIKE",
                    "message": f"Alert: High volume of public {log['category']} detected on {log['date']} ({log['percentage']}%)."
                })
                
        return jsonify({
            "status": "success",
            "data": metrics,
            "alerts_triggered": active_alerts
        }), 200
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)