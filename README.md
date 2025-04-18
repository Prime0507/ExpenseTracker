# 💰 A Friendly Expense Analyzer

Ever wondered where all your money disappears to each month? This app helps you make sense of your spending without the headache. Just upload your bank statement, and watch as your expenses come to life with colorful charts and helpful insights!

## Getting Started (The Easy Way)

### What we'll Need

- Python installed on your computer (any version 3.7 or newer)
- A few minutes of your time
- A CSV file of your transactions (I will explain what this is below)

### Step 1: Getting the App on Your Computer

Download the app in one of these ways:
- If you're comfortable with GitHub: `git clone https://github.com/yourusername/expense-analyzer.git`
- Or simply download and unzip the `expense_analyzer.zip` file

### Step 2: Setting Up (Don't Worry, It's Simple!)

Open your command prompt or terminal and follow these friendly steps:

```
# Go to the folder where you downloaded the app
cd expense-analyzer

# Create a safe space for the app (optional but helpful)
# For Windows:
python -m venv venv
venv\Scripts\activate

# For Mac/Linux:
python3 -m venv venv
source venv/bin/activate

# Install the necessary pieces
pip install streamlit pandas plotly numpy
```

### Step 3: Start the App

Still in your command prompt, type:
```
streamlit run app.py
```

A new browser window should open automatically. If not, you can visit http://localhost:8501 in your browser.

### Not Working? Try These Quick Fixes:

- **Nothing happened after running the app?** Check your browser or manually go to http://localhost:8501
- **Error messages about missing packages?** Make sure you ran the installation step correctly
- **Problems with your CSV file?** Make sure it has columns for Date, Description, and Amount

### Try Without Your Real Data First!

I have included some example files so you can test drive the app:
- `sample_transactions.csv` - A simple 3-month example
- `complex_transactions.csv` - A more detailed 6-month example

Just upload either file through the app's upload button to see how it works!

## What Does This App Actually Do?

### It Makes Sense of Your Money

1. **Organizes Your Spending**: Automatically sorts your purchases into categories like "Groceries," "Dining," and "Entertainment"
2. **Shows Where Your Money Goes**: Creates colorful charts that make patterns jump out at you
3. **Spots Trends**: Notices if you're spending more in certain categories or months
4. **Gives Helpful Insights**: Provides friendly observations about your spending habits

### The Helpful Bits You'll See

- **Pie Charts**: Show what percentage of your money goes to each category
- **Monthly Trends**: See if your spending is increasing or decreasing over time
- **Spending Breakdowns**: Find your biggest expenses at a glance
- **Smart Insights**: Get personalized observations about your spending patterns

## How I Built It

I created this app with real people in mind. Instead of complicated financial jargon, I focused on making something that:

- **Respects Your Privacy**: All your financial data stays on your computer
- **Speaks Human**: Uses plain language instead of confusing financial terms
- **Shows, Not Tells**: Uses visual charts that make patterns obvious
- **Keeps It Simple**: No overwhelming features or complicated steps

## What I Assumed About You

- You want to understand your spending without becoming a financial expert
- You have access to your transactions in a downloadable format from your bank
- You prefer seeing visual patterns rather than just numbers in a spreadsheet
- You want insights that are actually helpful, not just technical statistics

## The Parts That Make It Work

The app consists of several friendly pieces working together:
- The main screen that you interact with
- A smart categorizing system that sorts your purchases
- Pretty charts and visualizations that make patterns clear
- A helper that generates insights about your spending
- Sample data so you can try it without your real information

## Customizing to Your Life

Want to adjust how transactions are categorized? The app comes with common categories already set up, but you can customize them:

1. Find the `category_mapping.json` file
2. Open it in any text editor
3. Add keywords that match your shopping habits to the appropriate categories

## Thank You!