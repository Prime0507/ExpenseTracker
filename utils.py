import pandas as pd

def get_total_expenses(df):
    """
    Calculate the total expenses from the dataframe.
    
    Args:
        df: DataFrame with transaction data
    
    Returns:
        float: Total expense amount
    """
    # Sum all negative amounts (expenses)
    expenses = df[df['Amount'] < 0]['Amount'].sum()
    return expenses

def get_top_spending_category(df):
    """
    Find the category with the highest spending.
    
    Args:
        df: DataFrame with categorized transactions
    
    Returns:
        dict: Category name and amount
    """
    # Filter for expenses (negative amounts)
    expenses_df = df[df['Amount'] < 0].copy()
    
    # Group by category and find the one with the highest (absolute) total
    if len(expenses_df) > 0:
        category_totals = expenses_df.groupby('Category')['Amount'].sum()
        top_category = category_totals.abs().idxmax()
        top_amount = category_totals[top_category]
        
        return {
            "category": top_category,
            "amount": top_amount
        }
    else:
        return {
            "category": "None",
            "amount": 0
        }

def get_average_transaction(df):
    """
    Calculate the average transaction amount for expenses.
    
    Args:
        df: DataFrame with transaction data
    
    Returns:
        float: Average expense amount
    """
    # Filter for expenses (negative amounts)
    expenses_df = df[df['Amount'] < 0]
    
    if len(expenses_df) > 0:
        return expenses_df['Amount'].abs().mean()
    else:
        return 0

def get_month_over_month_change(df):
    """
    Calculate the percentage change in spending compared to the previous month.
    
    Args:
        df: DataFrame with transactions
    
    Returns:
        float: Percentage change
    """
    # Filter for expenses (negative amounts)
    expenses_df = df[df['Amount'] < 0].copy()
    
    # Group by month and calculate totals
    monthly_totals = expenses_df.groupby('Month')['Amount'].sum().abs()
    
    if len(monthly_totals) >= 2:
        # Sort by month
        monthly_totals = monthly_totals.sort_index()
        
        # Get last two months
        last_month = monthly_totals.iloc[-1]
        previous_month = monthly_totals.iloc[-2]
        
        # Calculate percentage change
        percent_change = ((last_month - previous_month) / previous_month) * 100
        return percent_change
    else:
        return 0
