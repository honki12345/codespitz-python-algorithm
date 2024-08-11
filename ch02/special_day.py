# ccc15j1 - Special Day
# https://dmoj.ca/problem/ccc15j1
month = input()
if len(month) == 1:
    if not (month in "123456789"):
        exit(f"input({input}) is not valid")
    month = "0" + month[0]
elif len(month) == 2:
    if not (month == "10" or month == "11" or month == "12"):
        exit(f"input({input}) is not valid")
else:  # len(month) != 1 and len(month) != 2
    exit(f"input({input}) is not valid")
days = input()
if not days.isdigit():
    exit("input is not number")
numberDays = int(days)
if not 1 <= numberDays <= 31:
    exit(f"input({input}) is not valid")
if len(days) == 1:
    days = "0" + days[0]
if month < "02":
    print("Before")
elif month > "02":
    print("After")
else:  # month == "02"
    if days < "18":
        print("Before")
    elif days > "18":
        print("After")
    else:  # days == "18"
        print("special")
