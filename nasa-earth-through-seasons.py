import requests
from getpass import getpass

BASE_URL = "https://api.nasa.gov/EPIC/api/natural/date/"

def get_photos(date, api_key):
    url = BASE_URL + date

    try:
        response = requests.get(
            url,
            params={"api_key": api_key},
            timeout=20
        )

        if response.status_code != 200:
            print(f"Error retrieving photos for {date}.")
            print(f"Status code: {response.status_code}")
            return []

        photos = response.json()

        if not isinstance(photos, list):
            print("The API did not return a photo list.")
            return []

        if len(photos) == 0:
            print(f"No photos available for {date}.")
            return []

        return photos

    except requests.exceptions.RequestException as error:
        print(f"Connection error: {error}")
        return []

    except ValueError:
        print("Unable to read the API response.")
        return []

def get_latitude(photos):

    if not photos:
        return None

    latitudes = []

    for photo in photos:

        coordinates = photo.get("centroid_coordinates", {})
        latitude = coordinates.get("lat")

        if latitude is not None:
            try:
                latitudes.append(float(latitude))
            except (ValueError, TypeError):
                continue

    if not latitudes:
        return None

    average_latitude = sum(latitudes) / len(latitudes)

    return average_latitude

def compare_seasons(june_latitude, december_latitude):

    if june_latitude is None or december_latitude is None:
        return "Unable to compare seasons because latitude data is missing."

    difference = abs(december_latitude - june_latitude)

    if december_latitude > june_latitude:
        direction = "farther north"
    elif december_latitude < june_latitude:
        direction = "farther south"
    else:
        direction = "at the same latitude"

    result = (
        f"December's average latitude is {direction} "
        f"compared to June's.\n"
        f"The difference between the two averages is "
        f"{difference:.2f} degrees."
    )

    return result


def main():

    print("================================")
    print("       CHASING THE SEASONS")
    print("       NASA EPIC PROJECT")
    print("================================")

    api_key = getpass("Enter your NASA API key: ").strip()

    if not api_key:
        print("An API key is required to continue.")
        return
    
    june_date = "2025-06-21"
    december_date = "2025-12-21"

    print("\nRetrieving June Earth photos...")
    june_photos = get_photos(june_date, api_key)

    print("\nRetrieving December Earth photos...")
    december_photos = get_photos(december_date, api_key)

    june_latitude = get_latitude(june_photos)
    december_latitude = get_latitude(december_photos)

    print("\n========== RESULTS ==========")

    if june_latitude is not None:
        print(f"June average latitude: {june_latitude:.2f}")
    else:
        print("June latitude: Unavailable")

    if december_latitude is not None:
        print(f"December average latitude: {december_latitude:.2f}")
    else:
        print("December latitude: Unavailable")

    print("\n========== COMPARISON ==========")

    comparison = compare_seasons(
        june_latitude,
        december_latitude
    )

    print(comparison)

    print("\nThank you for exploring Earth's seasons!")


if __name__ == "__main__":
    main()
