
print("\n Initializing Time... \n")
time = 0
day = 1
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
current_month = 0
month = months[current_month]
year = 1997

def Advance_Time():
    global time, day, current_month, month, year  # Declare global variables
    time += int(input("\n How much do you want to advance time (In hours)? \n"))
#   print(f"Time: {time}, Day: {day}, Current Month { current_month} and {month}, Year: {year}") If needed for debugging
    while time > 23:
        day += 1
        time -= 24
        while day > 30:
            day -= 30
            current_month += 1
            while current_month > 11:
                current_month -= 12
                year += 1
            month = months[current_month]
        
def report_date():
    if time < 10:
        print(f"It is currently 0{time}:00 on {day} of {month} of the year {year}")
    else:
        print(f"It is currently {time}:00 on {day} of {month} of the year {year}")

report_date()
while True: 
    Advance_Time()
    report_date()