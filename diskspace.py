import subprocess
from datetime import datetime

from tools import run_request, read_config

config = read_config()
chat_id = config["chat_id"]
bot_token = config["bot_token"]
available_gb_alert = int(config["available_gb_alert"])

output = subprocess.check_output('echo $(($(stat -f --format="%a*%S" .)))', shell=True, universal_newlines=True)
diskspace = round(float(output) / 1000000000, 2)

try:
    file = open("last-sent-diskspace.txt", "r")
    last_sent = int(file.readline())
    file.close()
except:
    last_sent = datetime.now().hour - 1

if diskspace < available_gb_alert and last_sent != datetime.now().hour:
    run_request("GET",
                f"https://api.telegram.org/bot{bot_token}/sendMessage?"
                f"chat_id={chat_id}&text=The available disk space is only {diskspace} GB!")
    file = open("last-sent-diskspace.txt", "w")
    file.write(str(datetime.now().hour))
    file.close()
