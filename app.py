import os
import socket
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

CAMPUS = os.getenv("CAMPUS_NAME", "KGiSL Institute of Technology")
BANNER = os.getenv("BANNER_MESSAGE", "Welcome to the Smart Campus Event Board")
VERSION = os.getenv("APP_VERSION", "1.0")

events = [
    {
        "title": "AI & Cloud Computing Workshop",
        "date": "15 October 2026",
        "venue": "Seminar Hall"
    },
    {
        "title": "Hackathon 2026",
        "date": "20 October 2026",
        "venue": "Innovation Lab"
    },
    {
        "title": "Guest Lecture on DevOps",
        "date": "25 October 2026",
        "venue": "Auditorium"
    },
    {
        "title": "Cyber Security Awareness Program",
        "date": "30 October 2026",
        "venue": "Block A"
    }
]


@app.route("/")
def home():
    return render_template_string("""
    <html>
    <head>
        <title>Smart Campus Event Board</title>
    </head>
    <body>
        <h1>{{ campus }}</h1>
        <h2>{{ banner }}</h2>

        <h3>Upcoming Events</h3>

        {% for event in events %}
            <p>
                <b>{{ event.title }}</b><br>
                Date: {{ event.date }}<br>
                Venue: {{ event.venue }}
            </p>
        {% endfor %}

        <hr>
        <p>Version: {{ version }}</p>
        <p>Pod Name: {{ pod }}</p>
    </body>
    </html>
    """,
    campus=CAMPUS,
    banner=BANNER,
    events=events,
    version=VERSION,
    pod=socket.gethostname())


@app.route("/api/events")
def api_events():
    return jsonify(events)


@app.route("/info")
def info():
    return jsonify({
        "campus": CAMPUS,
        "version": VERSION,
        "pod": socket.gethostname()
    })


@app.route("/health")
def health():
    return "Healthy"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)