import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def create_category_pie_chart(df):
    """
    Create a pie chart showing expense distribution by category.
    
    Args:
        df: DataFrame with categorized transactions
    
    Returns:
        Plotly figure object
    """
    # Filter for expenses (negative amounts)
    expenses_df = df[df['Amount'] < 0].copy()
    
    # Group by category and sum amounts
    category_totals = expenses_df.groupby('Category')['Amount'].sum().abs().reset_index()
    category_totals = category_totals.sort_values('Amount', ascending=False)
    
    # Create the pie chart
    fig = px.pie(
        category_totals,
        values='Amount',
        names='Category',
        title='Expense Distribution by Category',
        color_discrete_sequence=px.colors.qualitative.Pastel,
        hole=0.3
    )
    
    # Customize layout
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
        uniformtext_minsize=12,
        uniformtext_mode='hide',
        legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5)
    )
    
    return fig

def create_monthly_bar_chart(df):
    """
    Create a bar chart showing spending by month.
    
    Args:
        df: DataFrame with categorized transactions
    
    Returns:
        Plotly figure object
    """
    # Filter for expenses (negative amounts)
    expenses_df = df[df['Amount'] < 0].copy()
    
    # Group by month and sum amounts
    monthly_totals = expenses_df.groupby('Month')['Amount'].sum().abs().reset_index()
    monthly_totals = monthly_totals.sort_values('Month')
    
    # Create the bar chart
    fig = px.bar(
        monthly_totals,
        x='Month',
        y='Amount',
        title='Monthly Spending',
        labels={'Amount': 'Total Expenses ($)', 'Month': 'Month'},
        color_discrete_sequence=['#36A2EB']
    )
    
    # Customize layout
    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Total Expenses ($)",
        xaxis={'categoryorder': 'category ascending'}
    )
    
    return fig

def create_category_breakdown_table(df):
    """
    Create a table with category breakdown statistics.
    
    Args:
        df: DataFrame with categorized transactions
    
    Returns:
        DataFrame with category breakdown statistics
    """
    # Filter for expenses (negative amounts)
    expenses_df = df[df['Amount'] < 0].copy()
    
    # Create statistics by category
    category_stats = expenses_df.groupby('Category').agg(
        Total_Amount=('Amount', lambda x: abs(sum(x))),
        Average_Transaction=('Amount', lambda x: abs(sum(x)/len(x))),
        Number_of_Transactions=('Amount', 'count')
    ).reset_index()
    
    # Sort by total amount
    category_stats = category_stats.sort_values('Total_Amount', ascending=False)
    
    # Format the columns
    category_stats['Total_Amount'] = category_stats['Total_Amount'].map('${:,.2f}'.format)
    category_stats['Average_Transaction'] = category_stats['Average_Transaction'].map('${:,.2f}'.format)
    
    # Rename columns for display
    category_stats = category_stats.rename(columns={
        'Category': 'Category',
        'Total_Amount': 'Total Amount',
        'Average_Transaction': 'Average Transaction',
        'Number_of_Transactions': 'Number of Transactions'
    })
    
    return category_stats
