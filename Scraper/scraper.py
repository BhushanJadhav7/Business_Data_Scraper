import requests
import pandas as pd

def fetch_foursquare_places(query, location, api_key):
    """
    Fetch business data using the Foursquare Places API and save it to a CSV.

    :param query: Search query (e.g., "restaurants", "tech companies").
    :param location: Location to search around (e.g., "Mumbai, India").
    :param api_key: Your Foursquare Places API key.
    :return: None
    """
    url = "https://api.foursquare.com/v3/places/search"
    headers = {
        "Accept": "application/json",
        "Authorization": 'fsq3PncDJ+C615QMd8ZlHerhhtlVpGIppd61xQ7/jWgAx3w='  # Your API key
    }
    params = {
        "query": query,
        "near": location,
        "limit": 1000 # Number of results to fetch
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        places = data.get("results", [])
        business_data = []
        
        for place in places:
            business_data.append({
                "Name": place.get("name"),
                "Address": place.get("location", {}).get("address"),
                "City": place.get("location", {}).get("locality"),
                "Category": place.get("categories", [{}])[0].get("name", "N/A")
            })
        
        # Save the data to a CSV file
        df = pd.DataFrame(business_data)
        df.to_csv('foursquare_business_data.csv', index=False)
        print("Data saved to 'foursquare_business_data.csv'.")
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Example usage
if __name__ == "__main__":
    API_KEY = "fsq3PncDJ+C615QMd8ZlHerhhtlVpGIppd61xQ7/jWgAx3w="  # Replace with your Foursquare Places API key
    QUERY = "restaurants"
    LOCATION = "Mumbai, India"
    
    fetch_foursquare_places(QUERY, LOCATION, API_KEY)

