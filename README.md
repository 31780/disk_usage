# Disk Usage Alert

This Python script is designed to monitor the disk usage of the system and send an email alert when the usage exceeds a predefined threshold.

## Description

In a site reliability engineering (SRE) context, ensuring that disk usage remains within acceptable parameters is crucial to avoid potential system failures and service disruptions. This script is an example of how to implement a simple monitoring and alerting system for disk usage.

**Features:**
- Monitors the disk usage percentage.
- Sends an email alert when disk usage exceeds a predefined threshold.
- Configurable alert threshold and email settings.

## Usage

### Prerequisites
- Python 3.x
- Access to an SMTP server for sending email alerts.

### Configuration

- Set the `DISK_USAGE_THRESHOLD` to the desired disk usage alert threshold (as a percentage).
- Configure the SMTP server, port, email address, and password in the script.

### Running the Script

To run the script manually, use the following command:
```shell
python disk_usage_alert.py

