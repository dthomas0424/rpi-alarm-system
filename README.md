## Raspberry Pi Alarm System — Event-Driven Home Security Service

A continuously running Linux service that monitors physical door sensors via Raspberry Pi GPIO, maintains alarm state (armed/disarmed), triggers an audible alarm on breach, and sends email notifications when an intrusion occurs. A Flask web interface provides a small control plane for arming and disarming the system.

I built this system to practice end-to-end service ownership: designing, deploying, monitoring, and operating a real system that must reliably respond to real-world events.

---

WHAT THE SYSTEM DOES

- Monitors door/window sensors using Raspberry Pi GPIO
- Maintains persistent alarm state (armed / disarmed)
- Triggers a siren when a breach occurs while armed
- Sends email alerts on intrusion events
- Provides a Flask web UI to arm/disarm the system
- Runs continuously on a Linux host

---

ARCHITECTURE

Door Sensor (GPIO)
        ↓
Event Detection
        ↓
Alarm State Manager  ─────→  Web Control Interface (Flask)
        ↓
Breach Detected?
   ├─ Yes → Activate Siren
   └─ Yes → Send Email Notification

The system is event-driven. Hardware input generates events which are processed by the alarm state manager and routed to response handlers.

---

OPERATIONAL CHARACTERISTICS

- Designed to run continuously on a Raspberry Pi (Linux host)
- Recovers automatically after reboot
- Persists alarm state across restarts
- Handles real-world physical inputs (door sensors)
- Provides a remote control interface
- Generates alerts on breach events

---

RELIABILITY CONSIDERATIONS

- Prevent sensor bounce / false triggers
- Ensure predictable reboot recovery behavior
- Persist state to avoid “silent disarm” after restart
- Clear failure behavior: breach while armed always triggers alert + siren

This project mirrors operational concerns found in production monitoring systems: event handling, state management, alerting, and human response.

---

TECHNOLOGIES USED

- Python
- Flask (control interface)
- Raspberry Pi GPIO
- Linux (Raspberry Pi OS)
- SMTP email notifications

---

RUNNING THE SYSTEM

1. Install Python dependencies
2. Configure GPIO pin selection in the code
3. Start the service:

python alarm_web.py

Then open:

http://<raspberry-pi-ip>:5000

---

SECURITY NOTES

This system is intended for local network use only.
Do not expose the web interface directly to the public internet.

Recommended protections:
- LAN-only access
- VPN if remote access is needed
- Reverse proxy authentication if publishing internally

---

WHAT I LEARNED

- Event-driven programming
- Service state management
- Hardware/software interaction
- Alerting and human response workflows
- Operating a continuously running service

---

FUTURE OPERATIONAL IMPROVEMENTS

- Authentication for the web interface
- Health check endpoint
- Structured logging
- systemd service installation (run on boot)
