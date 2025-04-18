import os
import pandas as pd
import numpy as np
from datetime import datetime

def generate_ai_insights(df):
    """
    Find interesting and helpful patterns in your spending habits.
    We look at your data locally without sending it anywhere else.
    
    Args:
        df: Your categorized transactions
    
    Returns:
        list: Friendly, easy-to-understand insights about your money
    """
    try:
        # First, let's focus only on money going out (expenses)
        expenses_df = df[df['Amount'] < 0].copy()
        
        # If there's nothing to analyze, let you know gently
        if len(expenses_df) == 0:
            return ["We couldn't find any expenses to analyze in your data."]
        
        # Start with an empty list for our friendly observations
        money_insights = []
        
        # Figure out how much you spend in each category
        category_totals = expenses_df.groupby('Category')['Amount'].sum().abs().reset_index()
        category_totals = category_totals.sort_values('Amount', ascending=False)
        total_expenses = category_totals['Amount'].sum()
        
        # Calculate percentages to make it more relatable
        category_totals['Percentage'] = (category_totals['Amount'] / total_expenses * 100).round(1)
        
        # Tell you about your biggest spending area
        if len(category_totals) > 0:
            top_category = category_totals.iloc[0]
            money_insights.append(
                f"🔍 Looks like {top_category['Category']} is where most of your money goes - about "
                f"{top_category['Percentage']}% of your spending (${top_category['Amount']:.2f})."
            )
        
        # Mention your second biggest expense too
        if len(category_totals) > 1:
            second_category = category_totals.iloc[1]
            money_insights.append(
                f"🥈 Your second biggest expense is {second_category['Category']} at "
                f"{second_category['Percentage']}% of your budget (${second_category['Amount']:.2f})."
            )
        
        # Look at how your spending changes month to month
        if 'Month' in expenses_df.columns and len(expenses_df['Month'].unique()) > 1:
            monthly_totals = expenses_df.groupby('Month')['Amount'].sum().abs().sort_index()
            
            # Find your big spending months and your thrifty months
            highest_month = monthly_totals.idxmax()
            lowest_month = monthly_totals.idxmin()
            
            money_insights.append(
                f"📅 You spent the most in {highest_month} (${monthly_totals[highest_month]:.2f}) and "
                f"the least in {lowest_month} (${monthly_totals[lowest_month]:.2f})."
            )
            
            # See if you're spending more or less lately
            if len(monthly_totals) >= 2:
                last_month = monthly_totals.index[-1]
                prev_month = monthly_totals.index[-2]
                
                change_pct = ((monthly_totals[last_month] - monthly_totals[prev_month]) / 
                              monthly_totals[prev_month] * 100)
                
                if change_pct > 10:
                    money_insights.append(
                        f"📈 Heads up! Your spending jumped up by {abs(change_pct):.1f}% from {prev_month} to {last_month}."
                    )
                elif change_pct < -10:
                    money_insights.append(
                        f"📉 Nice work! You cut your spending by {abs(change_pct):.1f}% from {prev_month} to {last_month}."
                    )
                else:
                    money_insights.append(
                        f"⚖️ Your spending stayed pretty steady between {prev_month} and {last_month} (only changed by {abs(change_pct):.1f}%)."
                    )
                    
        # Look for categories where your spending habits are changing
        if 'Month' in expenses_df.columns and len(expenses_df['Month'].unique()) > 1:
            # Look at each category by month
            cat_month_totals = expenses_df.pivot_table(
                index='Category', 
                columns='Month', 
                values='Amount', 
                aggfunc='sum'
            ).fillna(0).abs()
            
            # Find areas where your spending changed significantly
            for category in cat_month_totals.index:
                if len(cat_month_totals.columns) >= 2:
                    latest_month = cat_month_totals.columns[-1]
                    prev_month = cat_month_totals.columns[-2]
                    
                    if cat_month_totals.loc[category, prev_month] > 0:
                        change_pct = ((cat_month_totals.loc[category, latest_month] - 
                                      cat_month_totals.loc[category, prev_month]) / 
                                      cat_month_totals.loc[category, prev_month] * 100)
                        
                        # Only mention big changes that might matter to you
                        if change_pct > 50:
                            money_insights.append(
                                f"⚠️ Wow! Your {category} spending shot up by {abs(change_pct):.1f}% from "
                                f"{prev_month} to {latest_month}. Might be worth checking what happened there."
                            )
                        elif change_pct < -30:
                            money_insights.append(
                                f"🎯 Great job! You cut your {category} spending by {abs(change_pct):.1f}% from "
                                f"{prev_month} to {latest_month}."
                            )
        
        # Give a helpful money-saving tip
        if len(category_totals) >= 3:
            # Look at smaller spending categories where cuts might be easier
            small_cats = category_totals[category_totals['Percentage'] < 10]
            if len(small_cats) > 0:
                random_cat = small_cats.sample(1).iloc[0]
                money_insights.append(
                    f"💡 Money-saving idea: Take a look at your {random_cat['Category']} expenses (${random_cat['Amount']:.2f}). "
                    f"Even small changes here could add up over time!"
                )
        
        # Make sure we have enough helpful observations
        if len(money_insights) < 3:
            money_insights.append(
                f"💰 Overall, you spent ${total_expenses:.2f} across all categories in this time period."
            )
            
        # Keep it digestible - no more than 5 insights
        return money_insights[:5]
    
    except Exception as e:
        print(f"Oops, something went wrong while analyzing your data: {str(e)}")
        return ["We hit a snag while analyzing your money patterns. Try again or check if your data has the expected format."]
