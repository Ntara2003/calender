import calendar

# Function to display the calendar for a given month and year
def show_calendar(year, month):
    # Create a text calendar instance
    cal = calendar.TextCalendar(calendar.SUNDAY)
    month_calendar = cal.formatmonth(year, month)
    
    print(month_calendar)

# Function to display the full calendar for a given year
def show_year_calendar(year):
    # Create a text calendar for the entire year
    year_calendar = calendar.TextCalendar(calendar.SUNDAY)
    print(calendar.calendar(year))

# Main program
print("Calendar Program")
choice = input("Enter 'M' for monthly calendar or 'Y' for full year calendar: ").upper()

if choice == 'M':
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    show_calendar(year, month)
elif choice == 'Y':
    year = int(input("Enter year: "))
    show_year_calendar(year)
else:
    print("Invalid choice!")
