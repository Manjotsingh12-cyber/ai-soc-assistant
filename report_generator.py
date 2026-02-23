import json
from datetime import datetime

def generate_report(alert, analysis, mitre):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"report_{timestamp}.json"

    report = {
        "alert": alert,
        "analysis": analysis,
        "mitre_mapping": mitre,
        "generated_at": timestamp
    }

    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    return filename
