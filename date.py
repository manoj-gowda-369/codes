def format_date(date_tuple):
    year, month, day = date_tuple

    month_names = [
        "", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    if 1 <= month <= 12:
        month_str = month_names[month]
        return f"{month_str} {day}, {year}"
    else:
        return "Invalid month!"

try:
    year = int(input("Enter year (e.g., 2025): "))
    month = int(input("Enter month (1-12): "))
    day = int(input("Enter day (1-31): "))


    date = (year, month, day)


    print("Formatted Date:", format_date(date))

except ValueError:
    print("Invalid input! Please enter numeric values.")