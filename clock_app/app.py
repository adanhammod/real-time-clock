from flask import Flask, render_template, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def home():
    # Default timezone: UTC
    tz_name = request.args.get("tz", "UTC")
    return render_template("clock.html", tz=tz_name)

@app.route("/api/time")
def time_api():
    tz_name = request.args.get("tz", "UTC")
    try:
        tz = pytz.timezone(tz_name)
    except:
        tz = pytz.UTC
    now = datetime.now(tz)
    return jsonify({
        "time": now.strftime("%H:%M:%S"),
        "date": now.strftime("%A, %d %B %Y")
    })

if __name__ == "__main__":
    app.run(debug=True)
