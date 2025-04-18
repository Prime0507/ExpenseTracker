import streamlit as st
import pandas as pd
import io
from expense_analyzer import process_csv, categorize_transactions
from visualization import create_category_pie_chart, create_monthly_bar_chart, create_category_breakdown_table
from ai_insights import generate_ai_insights
import utils

# Make our app look nice and friendly
st.set_page_config(
    page_title="Where's My Money Going?",
    page_icon="💰",
    layout="wide"
)

# Set up our memory to remember what you've uploaded
if 'df' not in st.session_state:
    st.session_state.df = None
if 'categorized_df' not in st.session_state:
    st.session_state.categorized_df = None
if 'insights' not in st.session_state:
    st.session_state.insights = None

# Welcome to the app!
st.title("💰 Where's My Money Going?")
st.write("Upload your bank statement and we'll help you see where your money is actually going.")

# Let's get your bank statement
with st.container():
    st.subheader("Step 1: Upload Your Bank Statement")
    
    uploaded_file = st.file_uploader("Drop your bank statement CSV file here", type="csv")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("Here's what your data should look like:")
        example_df = pd.DataFrame({
            'Date': ['2023-01-15', '2023-01-20', '2023-01-25'],
            'Description': ['GROCERY MART PURCHASE', 'NETFLIX SUBSCRIPTION', 'SHELL GAS STATION'],
            'Amount': [45.67, 12.99, 38.50]
        })
        st.dataframe(example_df)
    
    with col2:
        st.info("""
        **Quick Tips:**
        1. Look for a "Download Transactions" option in your online banking
        2. Make sure your file has these three things: when you spent it, where you spent it, and how much
        3. Expenses are usually shown as negative numbers (like -45.67)
        4. Not sure? Try our sample files first to see how it works!
        """)

# Making sense of your bank statement
if uploaded_file is not None:
    try:
        # Working behind the scenes to organize your data
        df = process_csv(uploaded_file)
        categorized_df = categorize_transactions(df)
        
        # Remembering your data so we don't lose it
        st.session_state.df = df
        st.session_state.categorized_df = categorized_df
        
        # Let you know we got it!
        st.success("Got it! We've organized your transactions.")
        
    except Exception as e:
        st.error(f"Hmm, something went wrong: {str(e)}. Try checking your file format.")

# Show the fun stuff once we have your data
if st.session_state.categorized_df is not None:
    # You can peek at the raw data if you want
    with st.expander("See your original transactions"):
        st.dataframe(st.session_state.df)
    
    # Show how we've organized things
    st.subheader("Step 2: We've Sorted Your Spending")
    st.write("We've automatically put each purchase into a category that makes sense:")
    st.dataframe(st.session_state.categorized_df)
    
    # The fun visual part!
    st.subheader("Step 3: Your Money, Visualized")
    st.write("Here's where your money actually went:")
    
    # Easy-to-navigate tabs for different views
    tab1, tab2, tab3 = st.tabs(["Where'd It Go?", "Monthly Patterns", "Category Details"])
    
    with tab1:
        st.write("This pie chart shows the percentage of your spending in each category:")
        fig = create_category_pie_chart(st.session_state.categorized_df)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.write("See how your spending changes month to month:")
        fig = create_monthly_bar_chart(st.session_state.categorized_df)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.write("A detailed breakdown of each spending category:")
        breakdown_table = create_category_breakdown_table(st.session_state.categorized_df)
        st.table(breakdown_table)
    
    # The big money picture
    st.subheader("Step 4: The Bottom Line")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_expenses = utils.get_total_expenses(st.session_state.categorized_df)
        st.metric("Total Spending", f"${abs(total_expenses):.2f}")
    
    with col2:
        top_category = utils.get_top_spending_category(st.session_state.categorized_df)
        st.metric("Biggest Money Drain", top_category["category"], 
                  f"${abs(top_category['amount']):.2f}")
    
    with col3:
        avg_transaction = utils.get_average_transaction(st.session_state.categorized_df)
        st.metric("Average Purchase", f"${abs(avg_transaction):.2f}")
    
    # Personal insights section
    st.subheader("Step 5: What Does It All Mean?")
    
    with st.container():
        if st.button("Get Personalized Money Insights"):
            with st.spinner("Looking for patterns in your spending..."):
                try:
                    insights = generate_ai_insights(st.session_state.categorized_df)
                    st.session_state.insights = insights
                except Exception as e:
                    st.error(f"Oops, we couldn't generate insights: {str(e)}")
        
        # Show the helpful insights
        if st.session_state.insights:
            st.write("Here are some interesting patterns we noticed:")
            for insight in st.session_state.insights:
                st.info(insight)
else:
    # Friendly welcome message when you first arrive
    st.info("👋 Welcome! Upload your bank statement (CSV file) to see where your money is really going.")
