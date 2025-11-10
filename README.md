# Network-scanning-Tool

    A multithreaded port scanner written in Python to discover open TCP ports, identify services, and perform simple banner grabbing.
    For educational and authorized security testing only. Do not scan systems you do not own or do not have explicit permission to test.

# 📌 Project Overview

This tool scans a target IPv4 address or domain name using a thread pool for speed. It supports two scan modes:

basic — ports '1–1024'
aggressive — ports '1–65535'

For each open port it attempts simple banner grabbing (sends an HTTP 'HEAD' request) and maps ports to common service names (if available).

# ✅ Features

* Resolves domain names to IPv4 addresses.
* Multithreaded scanning using 'concurrent.futures.ThreadPoolExecutor'.
* Two scan modes: 'basic' and 'aggressive'.
* Simple banner grabbing for basic service fingerprinting.
* Attempts to map ports to service names using 'socket.getservbyport'.
* Nicely formatted output: table of port / service / banner.


# 🧾 Files

* 'main.py' — Main scanner script (entry point)


# ⚙️ Requirements

 Python 3.10+ (script was tested with Python 3.12)
 No external libraries — uses Python standard library only


# 🚀 Installation

1. Clone the repo (replace <vikram> with your GitHub username):

bash
git clone https://github.com/vikram-hack/Network-scanning-Tool.git
cd Network-scanning-Tool


2. Run the scanner:

bash
python main.py


# ▶️ Usage (interactive)

When you run the script it will prompt for the target and scan type:

Enter IP address or domain name to scan: 192.168.52.1
Scan type ('basic' 1-1024 or 'aggressive' 1-65535): basic
Scanning 192.168.52.1 ports from 1 to 1024 ...

Scan completed in 6.15 seconds.

No open ports found.

If open ports are found, output will look like:

Port   Service         Banner
------------------------------------------------------------
22     ssh             SSH-2.0-OpenSSH_8.4
80     http            HTTP/1.1 200 OK
443    https           -


## 🧩 How it works (brief)

1. Resolve the input (domain or IP) to an IPv4 address.
2. Create a thread pool (default 'max_workers=200') and attempt a TCP connect to each port in the chosen range.
3. If the connection succeeds, try a simple banner grab (sends 'HEAD / HTTP/1.0\r\n\r\n') and read up to 1024 bytes.
4. Use 'socket.getservbyport' to map common port numbers to service names (fallback: 'unknown').
5. Print a sorted table of discovered open ports with service name and banner (if available).

# 🔧 Configurable items / notes

* 'max_workers' in the 'ThreadPoolExecutor' is currently set to '200'. You can reduce it for lower system/network load or increase it if your environment can handle more concurrency.
* Banner grabbing uses a basic HTTP 'HEAD' request. Some services won't respond to this; banners may be empty.
* Timeout for socket connect is set to '1' second — adjust if your network is slow or you need more reliable detection.

# ⚠️ Ethical & Legal Notice

Network scanning can be intrusive and is regulated in many contexts. Only run this tool against:

* systems you own, or
* systems for which you have explicit written permission.

Misuse may be illegal and could cause service disruption.

# 🛠️ Possible improvements / TODO

* Add CLI arguments (e.g., using 'argparse') for non-interactive runs.
* Add UDP scanning (careful: requires root/privileged access and different approach).
* Better banner grabbing per-protocol (SMTP, FTP, SSH specific probes).
* Rate limiting and backoff to avoid triggering IDS/IPS.
* Output formats: CSV, JSON, or an HTML report.
* Graceful handling/logging of exceptions and improved user feedback.

# 🤝 Contributing

Contributions are welcome. Open an issue for bugs or feature requests, and send pull requests for improvements. Please follow good ethical rules: don't add capabilities meant to facilitate unauthorized access.

# 📜 License

Include your preferred license here (e.g., MIT). Example:

MIT License

# Example 'main.py' (for reference)

python
# (Your script content - keep the approved copy in repo)

