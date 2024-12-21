# Stock Trading Plan: Watchlist Manager

## Description
This project implements a **Watchlist Manager** for traders, allowing them to efficiently track stock tickers and add optional notes for each ticker. It is designed to be a foundational tool for building a comprehensive stock trading plan.

The project demonstrates modular Python programming and is structured to allow easy addition of features, such as trade logging and technical analysis. This contribution could form the basis of an open-source project focused on helping traders with essential tools.

---

## Features
- **Add Tickers:** Add a stock ticker to the watchlist with optional notes.
- **View Watchlist:** Display the current watchlist with all tickers and notes.
- **Remove Tickers:** Remove a specific ticker from the watchlist.

---

## Development Setup

### Steps to Set Up the Environment:
1. Clone this repository:
   ```bash
   git clone <repository-link>
   ```
2. Navigate to the project directory:
   ```bash
   cd Stock_Trading_Plan
   ```
3. Create a virtual environment:
   ```bash
   python -m venv env
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the program by executing the `app.py` file:
```bash
python app.py
```

### Menu Options:
1. **Manage Watchlist:**
   - Add stock tickers with optional notes.
   - View the current watchlist.
   - Remove stock tickers.
2. **Exit:** Exit the program.

### Example Usage:

**Adding a Stock:**
1. Choose "1. Manage Watchlist."
2. Select "1. Add to Watchlist."
3. Enter a stock ticker (e.g., `TSLA`) and optional notes (e.g., "Tesla stock - monitor breakout above $200").

**Viewing the Watchlist:**
1. Choose "1. Manage Watchlist."
2. Select "2. View Watchlist."
3. The program will display all added tickers and notes.

**Removing a Stock:**
1. Choose "1. Manage Watchlist."
2. Select "3. Remove from Watchlist."
3. Enter the ticker to remove it from the watchlist.

---

## Contribution Details

### Work Item:
Implemented the **Watchlist Manager**, allowing users to:
- Add stock tickers to the watchlist.
- View the watchlist contents.
- Remove stock tickers from the list.

This feature simplifies stock tracking and aligns with the project's goal of providing tools for traders.

---

## Testing and Validation

### Pre-Checkin Checks:
- Verified functionality for:
  - Adding tickers.
  - Viewing the watchlist.
  - Removing tickers.
- Tested edge cases:
  - Missing `watchlist.csv` file (handled by creating the file automatically).
  - Empty watchlist display.

---

## Use-Cases and Requirements

### Use-Cases:
1. A trader adds a stock (`AAPL`) to track post-earnings movement.
2. A trader views their watchlist to plan trades for the week.
3. A trader removes a stock ticker no longer relevant to their strategy.

### User Story:
- *As a trader, I want to track stocks with notes so I can organize trading opportunities effectively.*

---

## Future Enhancements
1. Add a trade logger to track profits and losses.
2. Implement a risk calculator for position sizing.
3. Integrate technical analysis tools (e.g., RSI, moving averages).

---

## Repository Link
[https://github.com/CodyAC369/Stock_Trading_Plan](https://github.com/CodyAC369/Stock_Trading_Plan)

---

## Author
CodyAC369  
GitHub Profile: [https://github.com/CodyAC369](https://github.com/CodyAC369)


