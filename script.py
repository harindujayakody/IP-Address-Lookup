import os
import requests

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_ip_info():
    url = "http://ipinfo.io/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def print_dracula(text):
    # Dracula color codes
    dracula_fg = "\033[38;2;255;121;198m"
    dracula_reset = "\033[0m"
    print(f"{dracula_fg}{text}{dracula_reset}")

clear_terminal()  # Clear the terminal screen
ip_info = get_ip_info()

if ip_info:
    print_dracula("IP Information:")
    print_dracula("==============")
    print_dracula(f"IP Address   : {ip_info.get('ip', 'N/A')}")
    print_dracula(f"Hostname     : {ip_info.get('hostname', 'N/A')}")
    print_dracula(f"City         : {ip_info.get('city', 'N/A')}")
    print_dracula(f"Region       : {ip_info.get('region', 'N/A')}")
    print_dracula(f"Country      : {ip_info.get('country', 'N/A')}")
    print_dracula(f"Location     : {ip_info.get('loc', 'N/A')}")
    print_dracula(f"Organization : {ip_info.get('org', 'N/A')}")
else:
    print_dracula("Unable to fetch IP information.")
