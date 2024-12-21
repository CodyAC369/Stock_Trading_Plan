from watchlist_manager import add_to_watchlist, view_watchlist, remove_from_watchlist

def main():
    while True:
        print("\nStock Trading Plan Menu")
        print("1. Manage Watchlist")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nWatchlist Menu")
            print("1. Add to Watchlist")
            print("2. View Watchlist")
            print("3. Remove from Watchlist")
            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                ticker = input("Enter ticker: ")
                notes = input("Enter notes: ")
                add_to_watchlist(ticker, notes)
            elif sub_choice == "2":
                view_watchlist()
            elif sub_choice == "3":
                ticker = input("Enter ticker to remove: ")
                remove_from_watchlist(ticker)
        elif choice == "2":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
