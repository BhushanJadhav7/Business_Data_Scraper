# scraper/config.py

# HTTP Headers for requests
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/91.0.4472.124 Safari/537.36"
    )
}

# Base URL for scraping (if applicable)
BASE_URL = "https://example.com"

# Retry configuration
MAX_RETRIES = 3
RETRY_DELAY = 2  # in seconds
