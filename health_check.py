import urllib.request
import datetime


URL_TO_CHECK = "https://devops-midterm-project.vercel.app/api/health"
LOG_FILE = "uptime_status.log"

def check_health():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        response = urllib.request.urlopen(URL_TO_CHECK)
        if response.getcode() == 200:
            log_message = f"[{timestamp}] SUCCESS: App is online and healthy.\n"
        else:
            log_message = f"[{timestamp}] WARNING: App returned status code {response.getcode()}.\n"
    except Exception as e:
        log_message = f"[{timestamp}] ERROR: App is unreachable. Details: {str(e)}\n"

    print(log_message)
    with open(LOG_FILE, "a") as f:
        f.write(log_message)

if __name__ == "__main__":
    check_health()