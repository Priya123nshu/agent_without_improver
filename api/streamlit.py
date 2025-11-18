import subprocess
import sys
import time
import urllib.request

def handler(request, response):

    # Start Streamlit server (only once)
    if "streamlit_process" not in globals():
        globals()["streamlit_process"] = subprocess.Popen(
            [
                sys.executable,
                "-m", "streamlit",
                "run", "app.py",
                "--server.headless", "true",
                "--server.port", "8000",
                "--server.address", "0.0.0.0",
                "--server.enableCORS", "false",
                "--server.enableXsrfProtection", "false",
                "--global.developmentMode", "false",
                "--browser.gatherUsageStats", "false"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Wait for Streamlit to actually start
        time.sleep(3)

    # Forward response from Streamlit server
    try:
        html = urllib.request.urlopen("http://127.0.0.1:8000").read()
    except Exception as e:
        html = f"Streamlit failed to start: {e}".encode()

    response.status_code = 200
    response.headers["Content-Type"] = "text/html"
    response.body = html
