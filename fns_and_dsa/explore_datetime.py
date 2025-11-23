from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()
    # Format as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    # Prompt user for number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Save the current date
    current_date = datetime.now()
    # Calculate future date
    future_date = current_date + timedelta(days=days_to_add)
    # Format as YYYY-MM-DD
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
