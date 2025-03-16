def check_pin(pin):
    if len(pin) != 4 or not pin.isdigit():
        return "ERROR"
    if len(set(pin)) != 4:
        return "ERROR"
    pin_number = int(pin)
    if 1900 <= pin_number <= 2050:
        return "ERROR"
    return "OK"
pin = input()

result = check_pin(pin)
print(result)