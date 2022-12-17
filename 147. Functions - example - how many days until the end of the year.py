def DaysToEndOfTheYear():
    #print how much days left to end of the current year

    from datetime import date

    dateToday = date.today()

    currentYear  = dateToday.year

    dateEndYear  = date(currentYear,12,31)

    delta  = dateEndYear - dateToday


    print(delta.days)

DaysToEndOfTheYear()
