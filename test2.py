def shorten_deci(num, precision=3):
    num = float(num)
    num_str = str(num)
    decimal_part = num_str.split('.')[1]
    if len(set(decimal_part)) == 1:
        num_str = num_str.rstrip('0').rstrip('.')  # Remove zeros after decimal
        if decimal_part == '0':  # Check if the decimal part is zero
            return str(int(num))  # Return the integer part if the decimal part is zero
        else:
            return str("{:.{}f}".format(float(num_str), precision))
    else:
        return str(num)

# Test cases
print(shorten_deci("1.244231230000"))  # Output: 1.24423123
print(shorten_deci("1.333333300000"))  # Output: 1.333
print(shorten_deci("3.0"))           # Output: 3







