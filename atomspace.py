import requests

def fetch_iss_location():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        data = response.json()
        if response.status_code == 200:
            return data.get("iss_position", {}).get("latitude"), data.get("iss_position", {}).get("longitude")
    except Exception as e:
        print("An error occurred:", e)
    return None, None

def display_iss_location(latitude, longitude):
    if latitude is not None and longitude is not None:
        print("Current International Space Station Location:")
        print("Lat: {:.2f}°".format(float(latitude)))
        print("Long: {:.2f}°".format(float(longitude)))
    else:
        print("Unable to retrieve ISS location.")

if __name__ == "__main__":
    iss_latitude, iss_longitude = fetch_iss_location()
    display_iss_location(iss_latitude, iss_longitude)
