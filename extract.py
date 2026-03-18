import requests
from config import API_URL

def extract(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        extracted_data = response.text
        if extracted_data:
            print("Data extracted successfully!")
            return extracted_data
        else:
            print("Failed to extract data.")
            print(extracted_data)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return None
        
