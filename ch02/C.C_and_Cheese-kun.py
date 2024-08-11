# dmopc16c1p0 - C.C and Cheese-kun
# https://dmoj.ca/problem/dmopc16c1p0
widthOfPizza = input()
if not widthOfPizza.isdigit():
    exit("input is not number")
widthOfPizza = int(widthOfPizza)
if not 1 <= widthOfPizza <= 3:
    exit(f"input is not in range: 1 <= input <= 3")
percentageCheese = input()
if not percentageCheese.isdigit():
    exit("input is not number")
percentageCheese = int(percentageCheese)
if not 0 <= percentageCheese <= 100:
    exit(f"input is not in range: 0 <= input <= 100")
if widthOfPizza == 3 and percentageCheese >= 95:
    satisfaction = "absolutely"
elif widthOfPizza == 1 and percentageCheese <= 50:
    satisfaction = "fairly"
else:
    satisfaction = "very"
print(f"C.C. is {satisfaction} satisfied with her pizza.")

