import os
from openai import OpenAI

def test_openai_api():
    """
    Test the OpenAI API connection.
    """
    try:
        # Get OpenAI API key from environment
        api_key = os.getenv("OPENAI_API_KEY")
        
        if not api_key:
            print("❌ No API key found in environment variables.")
            return False
        
        print(f"✓ API key found (first 4 chars): {api_key[:4]}***")
        
        # Initialize OpenAI client
        client = OpenAI(api_key=api_key)
        print("✓ OpenAI client initialized successfully")
        
        # Make a simple API call
        print("Making test API call to OpenAI...")
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say 'Hello, the OpenAI API is working!'"}
            ],
            max_tokens=20
        )
        
        # Check the response
        content = response.choices[0].message.content
        print(f"✓ Received response: {content}")
        
        return True
    
    except Exception as e:
        print(f"❌ Error testing OpenAI API: {str(e)}")
        return False

if __name__ == "__main__":
    print("\n==== OpenAI API Test ====\n")
    success = test_openai_api()
    print("\n=========================\n")
    
    if success:
        print("✅ OpenAI API test completed successfully!")
    else:
        print("❌ OpenAI API test failed. Please check the errors above.")