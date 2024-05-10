# ---------------------------------------------------------------------------------------------
# Description: Build a simple Internet Performance and Network Speed Test Routine
# Author: Made with ❤️ in Python 3 by Alvison Hunter - September 26th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# ---------------------------------------------------------------------------------------------

import speedtest
from time import sleep
from tqdm import tqdm
from colorama import Fore, init

init(autoreset=True)

print(Fore.GREEN + "GETTING BEST AVAILABLE SERVERS, UPLOADING & DOWNLOADING SPEED.....")
# Initializing the SpeedTest instance
st = speedtest.Speedtest()

st.get_best_server()  # Get the most optimal server available
for i in tqdm(range(10), colour="green", desc="Finding Optimal Server "):
    sleep(0.15)

st.download()   # Get downloading speed
for i in tqdm(range(10), colour="cyan", desc="Getting Download Speed "):
    sleep(0.15)

st.upload()     # Get uploading speed
for i in tqdm(range(10), colour="red", desc="Getting Upload Speed   "):
    sleep(0.15)

# Save all these elements in a dictionary
res_dict = st.results.dict()

# Assign to variables with an specific format
dwnl = str(res_dict['download'])[:2] + "." + str(res_dict['download'])[2:4]

upl = str(res_dict['upload'])[:2] + "." + str(res_dict['upload'])[2:4]

# Display results in a nice looking table using colorama features
print("")

# divider - a line in the screen with a fixed width
print(Fore.MAGENTA + "="*80)
print(Fore.GREEN + "INTERNET SPEED TEST RESULTS:".center(80))
print(Fore.MAGENTA + "="*80)
print(Fore.YELLOW + f"Download: {dwnl}mbps ({float(dwnl)*0.125:.2f}MBs) | Upload:{upl}mbps ({float(upl)*0.125:.2f}MBs) | Ping:{res_dict['ping']:.2f}ms".center(80))
print(Fore.MAGENTA + "-"*80)
print(Fore.CYAN + f"HOST:{res_dict['server']['host']} | SPONSOR:{res_dict['server']['sponsor']} | LATENCY:{res_dict['server']['latency']:.2f}".center(80))
print(Fore.MAGENTA + "-"*80)
