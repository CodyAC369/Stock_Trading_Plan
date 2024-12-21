import pandas as pd 

WATCHLIST_FILE = "data/watchlist.csv"  # Ensure the path matches folder structure

def add_to_watchlist(ticker, notes=""):
    """Add a stock to the watchlist."""
    try:
        # Attempt to read the file
        df = pd.read_csv(WATCHLIST_FILE)
    except FileNotFoundError:
        # If the file doesn't exist, create it with a header
        print(f"{WATCHLIST_FILE} not found. Creating a new file.")
        df = pd.DataFrame(columns=["Ticker", "Notes"])  # Empty DataFrame with required columns
    
    # Add the new entry
    new_entry = pd.DataFrame({"Ticker": [ticker], "Notes": [notes]})
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(WATCHLIST_FILE, index=False)
    print(f"Added {ticker} to watchlist.")

def view_watchlist():
    """View the current watchlist."""
    try:
        # Attempt to read the file
        df = pd.read_csv(WATCHLIST_FILE)
        print(df)
    except FileNotFoundError:
        # If no file exists
        print("No watchlist found.")

def remove_from_watchlist(ticker):
    """Remove a stock from the watchlist."""
    try:
        # Attempt to read the file
        df = pd.read_csv(WATCHLIST_FILE)
        # Filter out the specified ticker
        df = df[df["Ticker"] != ticker]
        df.to_csv(WATCHLIST_FILE, index=False)
        print(f"Removed {ticker} from watchlist.")
    except FileNotFoundError:
        # If no file exists
        print("No watchlist found.")
