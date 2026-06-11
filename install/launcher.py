import subprocess
import webbrowser
import time

def launch():
    subprocess.Popen(["python", "installer/setup.py"])

    time.sleep(5)
    webbrowser.open("http://localhost:8501")

if __name__ == "__main__":
    launch()

