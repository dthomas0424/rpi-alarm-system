from flask import Flask, render_template, redirect, url_for
import threading
import time
import RPi.GPIO as GPIO
from datetime import datetime

app = Flask(__name__)
alarm_active = False
door_state = "Unknown"
last_door_state = None  # Track the previous door state to avoid sending multiple emails

DOOR_SENSOR_PIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Monitor the door state continuously
def monitor_door():
    global door_state, last_door_state
    prev_state = GPIO.input(DOOR_SENSOR_PIN)

    while True:
        current_state = GPIO.input(DOOR_SENSOR_PIN)
        if current_state != prev_state:
            # Get current time
            d = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            door_state = "OPEN" if current_state == GPIO.HIGH else "CLOSED"
            print(f"Door {door_state} at {d}")

            # Only send email and text if the alarm is active and the door has been opened
            if door_state == "OPEN" and alarm_active and last_door_state != "OPEN":
                exec(open('door_txt.py').read())  # Your email and text sending script
                #exec(open('door_txtmsg.py').read()) # Text Message Script
                exec(open('siren.py').read()) # Script for siren

            # Update last_door_state to avoid multiple emails
            last_door_state = door_state

            prev_state = current_state
        time.sleep(1)

# Flask route for the home page
@app.route("/")
def home():
    return render_template("index.html", status="ON" if alarm_active else "OFF", door_state=door_state)

# Flask route to start the alarm
@app.route("/start")
def start_alarm():
    global alarm_active
    alarm_active = True
    return redirect(url_for('home'))

# Flask route to stop the alarm
@app.route("/stop")
def stop_alarm():
    global alarm_active
    alarm_active = False
    return redirect(url_for('home'))

# New route to return the door state as JSON (for AJAX)
@app.route("/door_state")
def get_door_state():
    return {"door_state": door_state}

if __name__ == '__main__':
    # Start the door monitoring in a separate thread
    threading.Thread(target=monitor_door, daemon=True).start()
    
    # Start the Flask app
    app.run(host='0.0.0.0', port=5000)
