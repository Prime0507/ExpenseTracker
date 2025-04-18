"""
Demo script for the Expense Analyzer application.
This script demonstrates how to use the core functionality programmatically.
"""

import pandas as pd
from expense_analyzer import process_csv, categorize_transactions
from ai_insights import generate_ai_insights
import utils

def run_demo(csv_file_path):
    """
    Run a demonstration of the Expense Analyzer functionality.
    
    Args:
        csv_file_path: Path to the CSV file with transaction data
    """
    print("\n===== EXPENSE ANALYZER DEMO =====\n")
    
    # Step 1: Process the CSV file
    print("Step 1: Processing CSV data...")
    df = process_csv(csv_file_path)
    print(f"Processed {len(df)} transactions.")
    
    # Step 2: Categorize transactions
    print("\nStep 2: Categorizing transactions...")
    categorized_df = categorize_transactions(df)
    print("Categories found:")
    categories = categorized_df['Category'].value_counts()
    for category, count in categories.items():
        print(f"  - {category}: {count} transactions")
    
    # Step 3: Calculate key metrics
    print("\nStep 3: Calculating key metrics...")
    total_expenses = utils.get_total_expenses(categorized_df)
    top_category = utils.get_top_spending_category(categorized_df)
    avg_transaction = utils.get_average_transaction(categorized_df)
    
    print(f"  - Total Expenses: ${abs(total_expenses):.2f}")
    print(f"  - Top Spending Category: {top_category['category']} (${abs(top_category['amount']):.2f})")
    print(f"  - Average Transaction: ${abs(avg_transaction):.2f}")
    
    # Step 4: Generate insights
    print("\nStep 4: Generating smart insights...")
    insights = generate_ai_insights(categorized_df)
    print("Insights found:")
    for i, insight in enumerate(insights, 1):
        print(f"  {i}. {insight}")
    
    print("\n===== DEMO COMPLETE =====\n")
    return categorized_df

if __name__ == "__main__":
    # Run the demo with the sample transactions
    print("Running demo with sample transactions...")
    processed_data = run_demo("sample_transactions.csv")
    
    # Save some sample output
    print("Saving sample categorized data to categorized_transactions.csv")
    processed_data.to_csv("categorized_transactions.csv", index=False)
    
    print("\nDemo complete! You can now run the full application with:")
    print("  streamlit run app.py")