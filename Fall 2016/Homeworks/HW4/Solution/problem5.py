month = int(input("Enter month: "))
year = int(input("Enter year: "))

if month == 1:
    monthName = "January"
    numberOfDaysInMonth = 31
elif month == 2:
    monthName = "February"
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        numberOfDaysInMonth = 29
    else:
        numberOfDaysInMonth = 28
elif month == 3:
    monthName = "March"
    numberOfDaysInMonth = 31
elif month == 4:
    monthName = "April"
    numberOfDaysInMonth = 30
elif month == 5:
    monthName = "May"
    numberOfDaysInMonth = 31
elif month == 6:
    monthName = "June"
    numberOfDaysInMonth = 30
elif month == 7:
    monthName = "July"
    numberOfDaysInMonth = 31
elif month == 8:
    monthName = "August"
    numberOfDaysInMonth = 31
elif month == 9:
    monthName = "September"
    numberOfDaysInMonth = 30
elif month == 10:
    monthName = "October"
    numberOfDaysInMonth = 31
elif month == 11:
    monthName = "November"
    numberOfDaysInMonth = 30
else:
    monthName = "December"
    numberOfDaysInMonth = 31
    
print(monthName, year, "has", numberOfDaysInMonth, "days")
