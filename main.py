from extract import extract
from transform import transform
from database import load
from config import API_URL

extracted_data = extract(API_URL)
transformed_data = transform(extracted_data)

if transformed_data:
    ingestion = load(transformed_data)
    
    if ingestion:
        print("Data loaded successfully into the database.")
    else:
        print("Failed to load data into the database.")
else:
    print("No data to load into the database.")



