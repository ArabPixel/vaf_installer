#!/usr/bin/env python3
"""
VAF Installer HTTP Server

Serves the deploy/ folder statically.
Files are already patched by deploy.sh, so no runtime patching needed.

Usage: python3 server.py [port]
"""

import http.server
import os
import socket
import sys


PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 9090
SERVE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "deploy")


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SERVE_DIR, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()


if __name__ == "__main__":
    local_ip = get_local_ip()
    print(f"Serving: {SERVE_DIR}")
    print(f"URL: http://{local_ip}:{PORT}")
    print()

    httpd = http.server.HTTPServer(("0.0.0.0", PORT), CORSHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        httpd.shutdown()
