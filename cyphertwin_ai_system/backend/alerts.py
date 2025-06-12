# Alerts generation logic 
import json 

def trigger_alert(msg, severity):
    with open("alerts.json", "r+") as f:
        alerts = json.load(f)
        alerts.append({"msg" : msg, "severity" : severity})
        f.seek(0)
        json.dump(alerts, f)