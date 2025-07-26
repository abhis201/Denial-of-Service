# Denial-of-Service

This repository contains resources, scripts, and documentation related to Denial-of-Service (DoS) attacks. **For educational and research purposes only.**

## Overview

A Denial-of-Service (DoS) attack aims to make a machine or network resource unavailable to its intended users. This repository provides example scripts, detection methods, and mitigation strategies to help security researchers and students learn about DoS attacks and defenses.

## Features

- Example DoS attack scripts (for research/educational use)
- Documentation on DoS types, prevention, and impact
- Tools for analyzing network traffic related to DoS

## Installation

Clone the repository:

```bash
git clone https://github.com/abhis201/Denial-of-Service.git
cd Denial-of-Service
```

## Requirements

- Python 3.x
- `figlet` (for ASCII art banner, optional)

Install dependencies (if needed):

```bash
sudo apt-get install figlet   # On Ubuntu/Debian
brew install figlet           # On macOS
```

## Usage

**Warning:** Only use this script in a controlled, legal environment (e.g., your own test server). Unauthorized use against third-party systems is illegal.

Run the attack script:

```bash
python3 ddos-attack.py --ip <target_ip> --port <target_port> --duration <seconds>
```

Arguments:
- `--ip`      : Target IP address (required)
- `--port`    : Target port (default: 80)
- `--duration`: Attack duration in seconds (default: 30)

If arguments are not provided, the script will prompt for them interactively.

Example:
```bash
python3 ddos-attack.py --ip 192.168.1.100 --port 8080 --duration 60
```

## How It Works

The script sends UDP packets to the target IP and port for the specified duration. Progress is displayed in the terminal. This is a simple demonstration and not a sophisticated attack tool.

## Disclaimer

This repository is for educational purposes only. Do not use these scripts to attack any system without explicit permission. The author is not responsible for any misuse.
