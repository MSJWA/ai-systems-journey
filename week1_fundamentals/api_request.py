import requests

try: 
    response = requests.get("https://api.github.com/users/torvalds")

    if response.status_code == 200:
        data = response.json()
        print(data["name"])

    else: 
        print("Couldn't find that user.")

except requests.exceptions.ConnectionError:
    print("No internet connection.")