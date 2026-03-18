import json
from database import query_duplicates

def transform(data):
    try:
        products = json.loads(data)
        duplicates = []
        uniques = []
        
        for product in products:
            is_duplicate, rows = query_duplicates(product["title"])
            if is_duplicate:               
                duplicates.append(product)
            else:
                uniques.append(product)
                     
        return clean_data(uniques)

    
    except json.JSONDecodeError as e:
        print(f"An error occurred while parsing JSON data: {e}")
        return None


def clean_data(products):
    cleaned_products = []
    for product in products:
        cleaned_product = {
            "title": product.get("title", ""),
            "price": product.get("price", 0.0),
            "description": product.get("description", ""),
            "category": product.get("category", ""),
            "image": product.get("image", ""),
            "rating": product.get("rating") or {},
            "rate": product.get("rating", {}).get("rate", 0.0),
            "count": product.get("rating", {}).get("count", 0)
        }
        cleaned_products.append(cleaned_product)
    return cleaned_products


def remove_duplicates(duplicates, existing_titles):
    unique_products = []
    print("duplicates: ", duplicates)
    for product in duplicates:
        if product['title'] not in existing_titles:
            unique_products.append(product)
        else:
            pass
    print(f"Unique products after removing duplicates: {unique_products}")

    return unique_products
    