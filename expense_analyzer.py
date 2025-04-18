import pandas as pd
import io
from datetime import datetime
from categorization import categorize_transaction

def process_csv(file):
    """
    Process the uploaded CSV file into a pandas DataFrame.
    
    Args:
        file: The uploaded CSV file
    
    Returns:
        DataFrame with processed transactions
    
    Raises:
        ValueError: If required columns are missing or format is invalid
    """
    try:
        # Read CSV into DataFrame
        df = pd.read_csv(file)
        
        # Check for required columns
        required_columns = ['Date', 'Description', 'Amount']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Required column '{col}' is missing from the CSV file.")
        
        # Convert Date to datetime
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Ensure Amount is numeric
        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
        
        # Drop rows with NaN values in important columns
        df = df.dropna(subset=['Date', 'Description', 'Amount'])
        
        # Create additional columns for analysis
        df['Month'] = df['Date'].dt.strftime('%Y-%m')
        df['Year'] = df['Date'].dt.year
        df['Day'] = df['Date'].dt.day
        
        return df
    
    except pd.errors.EmptyDataError:
        raise ValueError("The CSV file is empty.")
    except pd.errors.ParserError:
        raise ValueError("Error parsing the CSV file. Please check the format.")
    except Exception as e:
        raise ValueError(f"Error processing the CSV file: {str(e)}")

def categorize_transactions(df):
    """
    Apply the categorization logic to each transaction in the DataFrame.
    
    Args:
        df: DataFrame containing transaction data
    
    Returns:
        DataFrame with added 'Category' column
    """
    # Create a copy to avoid modifying the original
    categorized_df = df.copy()
    
    # Apply the categorization function to each description
    categorized_df['Category'] = categorized_df['Description'].apply(categorize_transaction)
    
    return categorized_df
