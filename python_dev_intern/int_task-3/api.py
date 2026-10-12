import requests

try:
    city = input("Enter a City: ")
    r = requests.get(f"https://wttr.in/{city}?format=j1",timeout=10)
    r.raise_for_status()
    d = r.json()["current_condition"][0]
    print("Temperature is:", d["temp_C"], "°C")
    print("Weather is:", d["weatherDesc"][0]["value"])
except (requests.RequestException, ValueError, KeyError, IndexError) as e:
    print("Error:", e)