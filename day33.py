import requests
import datetime

MY_LAT = 41.630584
MY_LONG = 44.842387

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= latitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now = datetime.datetime.now().hour

    if now >= sunset or now <= sunrise:
        return True


if is_iss_overhead() and is_night():
    print("It's night and iss is overhead")
else:
    print("Nah")



