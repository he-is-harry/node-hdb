from random import randint

def divide_by_power_of_10(num_str, frac):

    # Check if the number is negative
    is_negative = num_str.startswith("-")
    
    # Remove the negative sign for calculation
    num_str = num_str.lstrip("-")
    
    num_len = len(num_str)

    # Place the decimal point
    if frac >= num_len:
        # Pad with zeros if the shift is greater than or equal to the length of the number
        result = "0." + "0" * (frac - num_len) + num_str
    else:
        # Insert the decimal point at the correct position
        result = num_str[:-frac] + "." + num_str[-frac:]
    
    # Remove any trailing decimal point (if the result is a whole number)
    result = result.rstrip(".")
    
    # Re-add the negative sign if the number was negative
    if is_negative:
        result = "-" + result

    return result

MAX_VAL = 65504
SIZE_REDUCTION = 0.000000001
MAX_FRAC = 15

with open("trial.js") as f:
    print(f.read())

print("var assert = require('assert');")
print("var buffer = Buffer.alloc(2);")

for testNum in range(10000):
    frac = randint(0, MAX_FRAC)
    val = randint(int(-MAX_VAL * (10 ** frac) * SIZE_REDUCTION), int(MAX_VAL * (10 ** frac) * SIZE_REDUCTION))

    print("write(buffer, {}, 0, true, 10, 2);".format(divide_by_power_of_10(str(val), frac)))
    print("assert(generalRead(buffer, 0, true, 10, 2) == readDec16(buffer, 0));")