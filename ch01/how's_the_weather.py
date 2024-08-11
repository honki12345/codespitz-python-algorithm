# (wc17c1j2) How's the Weather?
# https://dmoj.ca/problem/wc17c1j2
celsius = input()
celsius = int(celsius)
if not -40 <= celsius <= 40:
    exit("input is not in range: -40 <= C <= 40")

# formula Fahrenheit from Celsius
fahrenheit = (celsius * 9 / 5) + 32
fahrenheit = int(fahrenheit)
print(fahrenheit)
