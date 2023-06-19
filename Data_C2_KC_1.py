import pandas as pd
import requests

def fetch_data(api_url):
    try:
        # Make a GET request to the API URL
        response = requests.get(api_url)
        response.raise_for_status()
        # Extract the 'entries' data from the response
        data = response.json()['entries']
        return data
    except (requests.RequestException, ValueError) as e:
        # Handle any exceptions that occur during the request
        print(f"Error occurred while fetching data: {e}")
        return []

def analyze_data(data):
    if not data:
        print("No data to analyze.")
        return
    
    # Create a DataFrame from the fetched data
    df = pd.DataFrame(data=data)
    
    # Print the shape of the DataFrame (number of rows, number of columns)
    print("DataFrame shape:", df.shape)

    # Print the column names
    print("Column names:", df.columns)

    # Print the data types of each column
    print("Data types:")
    print(df.dtypes)

    # Print summary statistics of numerical columns
    print("Summary statistics:")
    print(df.describe())

    # Print the first few rows of the DataFrame
    print("First few rows:")
    print(df.head())

    # Print two descriptive statistics about the data
    print("Descriptive Statistics:")
    # Calculate the percentage of True values in the 'HTTPS' column
    print("1. Percentage of True values in 'HTTPS' column:", df['HTTPS'].mean() * 100)
    # Calculate the number of unique categories in the 'Category' column
    print("2. Number of unique categories in 'Category' column:", df['Category'].nunique())

    # Query to select a subset of data where 'Auth' column is 'apiKey'
    condition_value = 'apiKey'
    subset = df.query('Auth == @condition_value')

    # Print the second and third columns
    print("Selected Columns:")
    print(subset.iloc[:, 1:3])

    # Print the first 4 rows
    print("First 4 Rows:")
    print(subset.head(4))


# Define the API URL
api_url = 'https://api.publicapis.org/entries'

# Fetch data from the API
data = fetch_data(api_url)

# Analyze the data and meet the requirements
analyze_data(data)