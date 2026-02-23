from flask import Flask, request, jsonify
import json
from ai_engine import analyze_alert
from report_generator import generate_report
from mitre_mapper import map_to_mitre

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    print("[+] Alert received from Splunk")

    # AI Analysis
    analysis = analyze_alert(data)

    # MITRE Mapping
    mitre = map_to_mitre(data)

    # Generate Report
    report_path = generate_report(data, analysis, mitre)

    response = {
        "status": "processed",
        "analysis": analysis,
        "mitre": mitre,
        "report": report_path
    }

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
