Raspberry Pi Alarm System — Event-Driven Home Security Service

This project is a continuously running Linux service that monitors physical door sensors via GPIO, maintains alarm state, triggers an audible alarm on breach, and sends email notifications when an intrusion occurs. A Flask web interface provides a control plane for arming and disarming the system.

I built this system to practice end-to-end service ownership: designing, deploying, monitoring, and operating a real system that must reliably respond to real-world events.

What the System Does

Monitors door/window sensors using Raspberry Pi GPIO

Maintains persistent alarm state (armed / disarmed)

Triggers a siren when a breach occurs while armed

Sends email alerts on intrusion events

Provides a Flask web UI to arm/disarm the system

Runs continuously on a Linux host

Architecture
Door Sensor (GPIO)
        ↓
Event Detection
        ↓
Alarm State Manager ────→ Web Control Interface (Flask)
        ↓
Breach Detected?
   ├─ Yes → Activate Siren
   └─ Yes → Send Email Notification

The system is event-driven. Hardware input generates events which are processed by the alarm state manager and routed to appropriate response handlers.

Operational Characteristics

This system is designed to behave like a real service rather than a simple script.

Runs continuously on a Raspberry Pi (Linux host)

Recovers automatically after reboot

Persists alarm state across restarts

Handles real-world physical inputs (door sensors)

Provides a remote control interface

Generates alerts on failure events (breach)

Reliability Considerations

While building this system I focused on reliability behavior:

Preventing false triggers from sensor bounce

Handling reboot recovery

Persisting state so the system does not silently disarm

Ensuring alerts are sent before siren timeout

Designing clear failure behavior (breach always produces a notification)

This project mirrors operational concerns found in production monitoring systems: event handling, state management, alerting, and human response.

Technologies Used

Python

Flask (control interface)

Raspberry Pi GPIO

Linux (Raspberry Pi OS)

SMTP email notification

Running the System

Install Python dependencies

Configure GPIO pins

Start the service:

python alarm_web.py

Then open:

http://<raspberry-pi-ip>:5000
Security Notes

This system is intended for local network use only.
The web interface should not be exposed directly to the public internet.

Recommended protections:

local network only

reverse proxy authentication

VPN access if remote control is needed

What I Learned

This project taught me practical reliability concepts:

Event-driven programming

Service state management

Hardware/software interaction

Alerting and human response workflows

Operating a continuously running service

Future Improvements

Authentication for web interface

Health check endpoint

Structured logging

systemd service installation
