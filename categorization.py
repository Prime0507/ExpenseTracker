import json
import os
import re

# Load the category mapping from JSON file
def load_category_mapping():
    """
    Load the category mapping from the JSON file.
    
    Returns:
        dict: Mapping of keywords to categories
    """
    try:
        with open('category_mapping.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # If file doesn't exist yet, return default mapping
        return {
            "groceries": ["grocery", "supermarket", "food", "market", "walmart", "trader", "whole foods", "safeway", "kroger", "aldi", "costco"],
            "dining": ["restaurant", "cafe", "coffee", "starbucks", "mcdonald", "burger", "pizza", "dining", "chipotle", "subway", "taco", "doordash", "uber eats", "grubhub"],
            "transportation": ["gas", "fuel", "uber", "lyft", "taxi", "bus", "train", "transit", "transport", "parking", "toll", "car", "auto", "vehicle"],
            "utilities": ["electric", "water", "gas bill", "internet", "wifi", "phone", "utility", "bill", "service"],
            "housing": ["rent", "mortgage", "apartment", "housing", "maintenance", "repair", "home", "property"],
            "entertainment": ["movie", "theatre", "concert", "event", "ticket", "netflix", "hulu", "spotify", "disney", "amazon prime", "entertainment", "game"],
            "shopping": ["amazon", "ebay", "etsy", "target", "purchase", "store", "mall", "shop", "retail", "clothing", "apparel", "shoe"],
            "health": ["doctor", "medical", "pharmacy", "healthcare", "hospital", "clinic", "dental", "medication", "fitness", "gym", "health"],
            "education": ["tuition", "school", "college", "university", "course", "class", "education", "book", "learning", "student"],
            "travel": ["hotel", "flight", "airline", "airbnb", "booking", "vacation", "travel", "trip", "cruise"],
            "subscription": ["subscription", "membership", "recurring", "monthly"],
            "income": ["salary", "deposit", "income", "payment received", "refund", "tax return", "dividend", "interest"],
            "insurance": ["insurance", "premium", "coverage", "policy"],
            "investment": ["investment", "stock", "bond", "mutual fund", "etf", "brokerage", "wealth", "retirement"],
            "other": []
        }

def categorize_transaction(description):
    """
    Categorize a transaction based on its description.
    
    Args:
        description (str): Transaction description
    
    Returns:
        str: Category name
    """
    if not isinstance(description, str):
        return "Uncategorized"
    
    # Convert to lowercase for case-insensitive matching
    desc_lower = description.lower()
    
    # Load category mapping
    category_mapping = load_category_mapping()
    
    # Try to match the description to a category
    for category, keywords in category_mapping.items():
        for keyword in keywords:
            if keyword.lower() in desc_lower:
                return category
    
    # If no match found, return "Other"
    return "Other"

def add_keyword_to_category(keyword, category):
    """
    Add a new keyword to a specific category in the mapping.
    
    Args:
        keyword (str): New keyword to add
        category (str): Category to add the keyword to
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        category_mapping = load_category_mapping()
        
        # Check if the category exists
        if category not in category_mapping:
            category_mapping[category] = []
        
        # Add keyword if it doesn't already exist
        if keyword not in category_mapping[category]:
            category_mapping[category].append(keyword)
        
        # Save updated mapping
        with open('category_mapping.json', 'w') as f:
            json.dump(category_mapping, f, indent=4)
        
        return True
    except Exception:
        return False
