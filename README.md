## Raspberry Pi Alarm System — Event-Driven Home Security Service

A continuously running Linux service that monitors physical door sensors via Raspberry Pi GPIO, maintains alarm state (armed/disarmed), triggers an audible alarm on breach, and sends email notifications when an intrusion occurs. A Flask web interface provides a small control plane for arming and disarming the system.

I built this system to practice end-to-end service ownership: designing, deploying, and operating a real system that must reliably respond to real-world events.

---

## What the system does
- Monitors door/window sensors using Raspberry Pi GPIO
- Maintains persistent alarm state (armed / disarmed)
- Triggers a siren when a breach occurs while armed
- Sends email alerts on intrusion events
- Provides a Flask web UI to arm/disarm the system
- Runs continuously on a Linux host

---

## Architecture
