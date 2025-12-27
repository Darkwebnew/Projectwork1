#!/usr/bin/env python3
"""
Simple server startup script
"""

import os
import sys
import subprocess
from pathlib import Path

# Set project root
BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"

# Make sure src is in the path
sys.path.insert(0, str(SRC_DIR))

# Get port from environment or default to 8000
PORT = int(os.environ.get("PORT", 8000))

if __name__ == "__main__":
    print("🚀 Starting Nginx WAF AI Server...")
    print(f"📡 API Docs: http://localhost:{PORT}/docs")
    print(f"🔍 Health Check: http://localhost:{PORT}/health")

    # Run uvicorn as a module to handle relative imports properly
    cmd = [
        sys.executable, "-m", "uvicorn",
        "src.main:app",
        "--host", "0.0.0.0",
        "--port", str(PORT),
        "--log-level", "info"
    ]

    # Optional: enable auto-reload in development
    if os.environ.get("DEV_MODE", "0") == "1":
        cmd.append("--reload")

    # Run the server
    subprocess.run(cmd)
