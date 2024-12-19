# Business Data Scraper

## Overview

The **Business Data Scraper** is a Python-based project that retrieves business information from the **Foursquare Places API**. This scraper allows users to search for businesses by category (e.g., "restaurants") and location (e.g., "Mumbai, India"). The scraper can collect up to 5000 records and save them into a CSV file. Additionally, the project includes data cleaning functionalities to handle missing, duplicate, or inconsistent values in the fetched data, making it ready for analysis or machine learning tasks.

## Features

- Fetches business data from the Foursquare Places API.
- Supports querying different business categories (e.g., "restaurants", "tech companies").
- Handles pagination to fetch large amounts of data.
- Data cleaning functions for handling missing values, removing duplicates, and handling inconsistent formats.
- Saves the cleaned data to a CSV file for further analysis.

## Requirements

To run this project, you will need:

- Python 3.x
- pandas
- requests

Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

`requirements.txt` content:

```
pandas==2.1.0
requests==2.31.0
```

## Setup and Configuration

### 1. Get Your Foursquare API Key

You need a **Foursquare API key** to interact with their Places API. To obtain one:

1. Go to [Foursquare Developers](https://foursquare.com/developers/) and sign up.
2. Once signed in, create a new application to get your API key.

### 2. Update the API Key in the Code

In the `scraper.py` file, replace the API key placeholder with your Foursquare API key:

```python
headers = {
    "Accept": "application/json",
    "Authorization": "fsq3PncDJ+C615QMd8ZlHerhhtlVpGIppd61xQ7/jWgAx3w="  # Replace with your API key
}
```

### 3. Set Query Parameters

In `scraper.py`, update the following configuration variables to suit your needs:

- **QUERY**: The business category or keyword to search for (e.g., "restaurants").
- **LOCATION**: The location to search around (e.g., "Mumbai, India").
- **total_results**: The total number of records to fetch (default is 5000).

## Running the Scraper

### 1. Fetch Business Data

Run the `scraper.py` file to start scraping:

```bash
python scraper.py
```

This will fetch business data from the Foursquare API, storing it in the `foursquare_business_data.csv` file.

### 2. Clean the Fetched Data

Run the `clean_data.ipynb` file to clean the raw data fetched by the scraper:

```bash
python clean_data.ipynb
```

This script will:
- Handle missing or inconsistent values.
- Remove duplicate records.
- Save the cleaned data in a new CSV file: `cleaned_foursquare_business_data.csv`.

## File Structure

- **scraper.py**: Contains the code for fetching data from the Foursquare API.
- **clean_data.py**: Contains the code for cleaning the fetched data.
- **foursquare_business_data.csv**: The raw CSV file containing the scraped business data.
- **cleaned_foursquare_business_data.csv**: The cleaned CSV file after data processing.

## Testing the Scraper

1. **Test Fetching:**
   - Ensure that the API key is correctly set.
   - Test the scraper to confirm it fetches data correctly and handles pagination.
   - Verify that the CSV file contains the expected number of records.

2. **Test Data Cleaning:**
   - Run `clean_data.ipynb` on the raw CSV.
   - Ensure missing values, duplicates, and inconsistent formats are properly handled.
   - Verify that the cleaned data is saved in a new CSV file.

## Troubleshooting

- **API Rate Limits:**
  - If you encounter issues due to rate-limiting, add delays between requests using `time.sleep()` or adjust the number of requests per minute.
  
- **Empty CSV or No Data:**
  - Make sure the query and location are correct.
  - Check for any API response errors or empty results.

- **Invalid API Key:**
  - Ensure you have a valid API key and that it is correctly set in the script.

## License

This project is open-source and available under the MIT License.

---

Feel free to modify or add more details based on your project’s specific needs!
