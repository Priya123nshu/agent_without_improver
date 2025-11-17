import subprocess
import sys
import urllib.request

# This handler runs inside Vercel’s serverless function
def handler(request, response):
    # Launch Streamlit server only once
    if "streamlit_process" not in globals():
        globals()["streamlit_process"] = subprocess.Popen(
            [
                sys.executable,
                "-m",
                "streamlit",
                "run",
                "app.py",
                "--server.port",
                "8000",
                "--server.address",
                "0.0.0.0",
                "--browser.gatherUsageStats",
                "false"
            ]
        )

    # Try reading the Streamlit output on port 8000
    try:
        html = urllib.request.urlopen("http://127.0.0.1:8000").read()
    except Exception as e:
        html = f"Streamlit startup error: {e}".encode()

    response.status_code = 200
    response.headers["Content-Type"] = "text/html"
    response.body = html
