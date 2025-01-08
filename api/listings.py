import requests

def fetch_listings(limit=20):
    API_KEY = "ZrQEPSkKa3VzaGtzaGFoM0BnbWFpbC5jb20="
    url = "https://auto.dev/api/listings"
    headers = {"apikey": API_KEY}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        listings = data.get("records", [])
        car_details = []

        for listing in listings[:limit]:
            car = {
                "name": f"{listing.get('make', 'Unknown')} {listing.get('model', 'Unknown')}",
                "price": listing.get("price", "N/A"),
                "type": listing.get("bodyType", "N/A"),
                "mileage": listing.get("mileage", "N/A"),
                "picture":listing.get("primaryPhotoUrl","N/A")
                }
            car_details.append(car)

        return car_details    
    
    except:
        raise Exception("Could not send request")
    