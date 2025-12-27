#!/usr/bin/env python3
"""
Simple server startup script
"""

import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"

sys.path.insert(0, str(SRC_DIR))

import uvicorn
from src.main import app

if __name__ == "__main__":
    print("🚀 Starting Nginx WAF AI Server...")
    print("📡 API Docs: /docs")
    print("🔍 Health Check: /health")

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        log_level="info"
    )
