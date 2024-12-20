import requests
import pandas as pd
import time

def fetch_foursquare_places(query, location, api_key, total_results=5000, limit=50, sleep_time=1):
    """
    Fetch business data from Foursquare Places API and save it to CSV.
    
    :param query: Search query (e.g., "restaurants", "tech companies").
    :param location: Location to search around (e.g., "Mumbai, India").
    :param api_key: Your Foursquare Places API key.
    :param total_results: Total number of results to fetch (default is 5000).
    :param limit: Limit of results per request (default is 50).
    :param sleep_time: Time to sleep between requests (default is 1 second to avoid rate-limiting).
    :return: None
    """
    url = "https://api.foursquare.com/v3/places/search"
    headers = {
        "Accept": "application/json",
        "Authorization": api_key
    }

    params = {
        "query": query,
        "near": location,
        "limit": limit,  # Fetch 50 results per request
    }

    all_results = []
    offset = 0
    
    while len(all_results) < total_results:
        params["offset"] = offset
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            places = data.get("results", [])
            if not places:  # If no more results are returned, break the loop
                break
            for place in places:
                all_results.append({
                    "Name": place.get("name"),
                    "Address": place.get("location", {}).get("address", "N/A"),
                    "City": place.get("location", {}).get("locality", "N/A"),
                    "Category": place.get("categories", [{}])[0].get("name", "N/A")
                })

            offset += limit  # Increase the offset to fetch the next batch of results

            # Sleep for a while to respect the rate limit
            time.sleep(sleep_time)

        else:
            print(f"Error: {response.status_code}, {response.text}")
            break

    # Convert the data to DataFrame and save it to a CSV file
    df = pd.DataFrame(all_results)
    df.to_csv('foursquare_business_data.csv', index=False)
    print(f"Fetched and saved {len(all_results)} records to 'foursquare_business_data.csv'.")

# Example usage
if __name__ == "__main__":
    API_KEY = "fsq3PncDJ+C615QMd8ZlHerhhtlVpGIppd61xQ7/jWgAx3w="  # Replace with your Foursquare Places API key
    QUERY = "restaurants"
    LOCATION = "Mumbai, India"
    
    fetch_foursquare_places(QUERY, LOCATION, API_KEY, total_results=5000)  # Adjust to 5000 results
