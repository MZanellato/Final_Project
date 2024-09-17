# Functions for task 1
def adding(x,y):
    return x + y
def subtracting(x,y):
    return x - y
def dividing(x,y):
    return x / y
def multiplying(x,y):
    return x * y

# Imports function for task 2
from fractions import Fraction

# Dictionaries for task 3
conversion_values_lenght = {
    "inches": 0.0254, 
    "feet": 0.3048, 
    "yards": 0.9144, 
    "miles": 1609.344, 
    "millimeters": 0.001, 
    "centimeters": 0.01, 
    "meters": 1, 
    "kilometers": 1000}
conversion_values_volume = {
    "cups": 0.23658824, 
    "pints": 0.47317647, 
    "quarts": 0.94635295, 
    "gallons": 3.78541178, 
    "milliliters": 0.001, 
    "liters": 1, 
    "kiloliters": 1000}
conversion_values_weight = {
    "ounces": 28.3495231, 
    "pounds": 453.59237, 
    "tons": 907184.74, 
    "milligrams": 0.001, 
    "grams": 1, 
    "kilograms": 1000}

# Functions for task 3
def length_conversion(from_unit, length, to_unit):
    if from_unit in conversion_values_lenght and to_unit in conversion_values_lenght:
        length_meters = length * conversion_values_lenght[from_unit]
        converted_length = length_meters / conversion_values_lenght[to_unit]
        return converted_length
    else:
        return "Invalid units"
def volume_conversion(from_unit, volume, to_unit):
    if from_unit in conversion_values_volume and to_unit in conversion_values_volume:
        volume_liters = volume * conversion_values_volume[from_unit]
        converted_volume = volume_liters / conversion_values_volume[to_unit]
        return converted_volume
    else:
        return "Invalid units"
def weight_conversion(from_unit, weight, to_unit):
    if from_unit in conversion_values_weight and to_unit in conversion_values_weight:
        weight_grams = weight * conversion_values_weight[from_unit]
        converted_weight = weight_grams / conversion_values_weight[to_unit]
        return converted_weight
    else:
        return "Invalid units"

# Starts a user-friendly board 
print                                   (" -------------------------------------------------------------------------------------\n"
                                         "|                                       Welcome!                                      |\n"
                                         "|                                                                                     |\n"
                                         "| This program serves as a tool for performing various mathematical operations and    |\n"
                                         "| unit conversions, and you can choose what to do below...                            |")

# This loop makes operations based on user inputs
while True:
    task = input                        ("|                                                                                     |\n"
                                         "| -> 1 (Basic mathematical operations)                                                |\n"
                                         "| -> 2 (Fraction to decimal conversion or vice-versa, and decimal ordering)           |\n"
                                         "| -> 3 (Length, liquid volume, weight, or temperature conversions in different units) |\n"
                                         "| Choose task: ")
    if task == '1':
        basic_operation = input         ("|                                                                                     |\n"
                                         "| Choose one operation                                                                |\n"
                                         "| -> A (Addition)                                                                     |\n"
                                         "| -> S (Subtraction)                                                                  |\n"
                                         "| -> M (Multiplication)                                                               |\n"
                                         "| -> D (Division)                                                                     |\n"
                                         "| Answer: ")
        if basic_operation.upper() == 'A':
            dFirst = float(input        ("|                                                                                     |\n"
                                         "| First number: "))
            dSecond = float(input       ("| Second number: "))
            print                       ("| The result is:", adding(dFirst,dSecond))
        elif basic_operation.upper() == 'S':
            dFirst = float(input        ("|                                                                                     |\n"
                                         "| First number: "))
            dSecond = float(input       ("| Second number: "))
            print                       ("| The result is:", subtracting(dFirst,dSecond))
        elif basic_operation.upper() == 'M':
            dFirst = float(input        ("|                                                                                     |\n"
                                         "| First number: "))
            dSecond = float(input       ("| Second number: "))
            print                       ("| The result is:", round(multiplying(dFirst,dSecond),4))
        elif basic_operation.upper() == 'D':
            dFirst = float(input        ("|                                                                                     |\n"
                                         "| First number: "))
            dSecond = float(input       ("| Second number: "))
            precision = int(input       ("| How many decimals to round? "))
            print                       ("| The result is:", round(dividing(dFirst,dSecond),precision))
        else:
            print                       ("|                                                                                     |\n"
                                         "|        **INVALID**                  **INVALID**                  **INVALID**        |")
    elif task == '2':
        number_conversion = input       ("|                                                                                     |\n"
                                         "| Choose the conversion                                                               |\n"
                                         "| -> D (Convert decimal to fraction)                                                  |\n"
                                         "| -> F (Convert fraction to decimal)                                                  |\n"
                                         "| -> S (Sort decimals)                                                               |\n"
                                         "| Answer: ")
        if number_conversion.upper() == 'D':
            decimal = float(input       ("|                                                                                     |\n"
                                         "| Enter the decimal: "))
            fraction = Fraction(decimal)
            print                       ("|",decimal,"in fraction is", round(fraction,3))
        elif number_conversion.upper() == 'F':
            numerator = float(input     ("|                                                                                     |\n"
                                         "| Enter the numerator: "))
            denominator = float(input   ("| Enter the denominator: "))
            precision = int(input       ("| How many decimals to round? "))
            decimal = numerator / denominator
            print                       ("|",numerator,"/",denominator,"in decimal is",round(decimal, precision))
        elif number_conversion.upper() == 'S':
            decimals_amount = int(input ("|                                                                                     |\n"
                                         "| How many decimals to sort? "))
            decimals_list = []
            for i in range(decimals_amount):
                decimals = float(input  ("| Enter decimal: "))
                decimals_list.append(decimals)
            sorted_decimals = sorted(decimals_list)
            print                       ("| Sorted decimals:", sorted_decimals)
        else:
            print                       ("|                                                                                     |\n"
                                         "|        **INVALID**                  **INVALID**                  **INVALID**        |")
    elif task == '3':
        type_conversion = input         ("|                                                                                     |\n"
                                         "| Choose type of unit conversion                                                      |\n"
                                         "| -> L (Length)                                                                       |\n"
                                         "| -> V (Liquid volume)                                                                |\n"
                                         "| -> W (Weight)                                                                       |\n"
                                         "| -> T (Temperature)                                                                  |\n"
                                         "| Answer: ")
        if type_conversion.upper() == 'L':
            from_unit = input           ("|                                                                                     |\n"
                                         "| The avaible units are:                                                              |\n"
                                         "| -> Inches                                                                           |\n"
                                         "| -> Feet                                                                             |\n"
                                         "| -> Yards                                                                            |\n"
                                         "| -> Miles                                                                            |\n"
                                         "| -> Millimeters                                                                      |\n"
                                         "| -> Centimeters                                                                      |\n"
                                         "| -> Meters                                                                           |\n"
                                         "| -> Kilometers                                                                       |\n"
                                         "|                                                                                     |\n"
                                         "| Convert from: ")
            from_unit = from_unit.lower()
            length = float(input        ("| How many? "))
            to_unit = input             ("| Convert to: ")
            to_unit = to_unit.lower()
            precision = int(input       ("| How many decimals to round? "))
            converted_length = length_conversion(from_unit, length, to_unit)
            if converted_length == "Invalid units":
                print                   ("|                                                                                     |\n"
                                         "|        **INVALID**                  **INVALID**                  **INVALID**        |")
            else:
                print                   ("|",length, from_unit, "is equal to", round(converted_length, precision), to_unit)            
        elif type_conversion.upper() == 'V':
            from_unit = input           ("|                                                                                     |\n"
                                         "| The avaible units are:                                                              |\n"
                                         "| -> Cups                                                                             |\n"
                                         "| -> Pints                                                                            |\n"
                                         "| -> Quarts                                                                           |\n"
                                         "| -> Gallons                                                                          |\n"
                                         "| -> Milliliters                                                                      |\n"
                                         "| -> Liters                                                                           |\n"
                                         "| -> Kiloliters                                                                       |\n"
                                         "|                                                                                     |\n"
                                         "| Convert from: ")
            from_unit = from_unit.lower()
            volume = float(input        ("| How many? "))
            to_unit = input             ("| Convert to: ")
            to_unit = to_unit.lower()
            precision = int(input       ("| How many decimals to round? "))
            converted_volume = volume_conversion(from_unit, volume, to_unit)
            if converted_volume == "Invalid units":
                print                   ("|                                                                                     |\n"
                                         "|        **INVALID**                  **INVALID**                  **INVALID**        |")
            else:
                print                   ("|",volume, from_unit, "is equal to", round(converted_volume, precision), to_unit)
        elif type_conversion.upper() == 'W':
            from_unit = input           ("|                                                                                     |\n"
                                         "| The avaible units are:                                                              |\n"
                                         "| -> Ounces                                                                           |\n"
                                         "| -> Pounds                                                                           |\n"
                                         "| -> Tons                                                                             |\n"
                                         "| -> Milligrams                                                                       |\n"
                                         "| -> Grams                                                                            |\n"
                                         "| -> Kilograms                                                                        |\n"
                                         "|                                                                                     |\n"
                                         "| Convert from: ")
            from_unit = from_unit.lower()
            weight = float(input        ("| How many? "))
            to_unit = input             ("| Convert to: ")
            to_unit = to_unit.lower()
            precision = int(input       ("| How many decimals to round? "))
            converted_weight = weight_conversion(from_unit, weight, to_unit)
            if converted_weight == "Invalid units":
                print                   ("|                                                                                     |\n"
                                         "|        **INVALID**                  **INVALID**                  **INVALID**        |")
            else:
                print                   ("|",weight, from_unit, "is equal to", round(converted_weight, precision), to_unit)
        elif type_conversion.upper() == 'T':
            answer_3 = input            ("|                                                                                     |\n"
                                         "| Here are some key temperatures:                                                     |\n"
                                         "| Freezing point of water: 32°F / 0°C                                                 |\n"
                                         "| Boiling point of water: 212°F / 100°C                                               |\n"
                                         "| Average human body temperature: 98°F / 37°C                                         |\n"
                                         "|                                                                                     |\n"
                                         "| Choose the conversion                                                               |\n"
                                         "| -> F (Fahrenheit to celsius)                                                        |\n"
                                         "| -> C (Celsius to fahrenheit)                                                        |\n"
                                         "| Answer: ")
            if answer_3.upper() == 'F':
                fahrenheit = float(input("|                                                                                     |\n"
                                         "| Temperature in fahrenheit: "))
                celsius = (fahrenheit - 32) / 1.8
                print                   ("| " + str(fahrenheit) + "°F is equal to " + str(round(celsius,2)) + "°C")
            elif answer_3.upper() == 'C':
                celsius = float(input   ("|                                                                                     |\n"
                                         "| Temperature in celsius: "))
                fahrenheit = (celsius * 1.8) + 32
                print                   ("| " + str(celsius) + "°C is equal to " + str(round(fahrenheit, 2)) + "°F")
# Invalid inputs from user
            else:
                print                   ("|                                                                                     |\n"
                                         "|        **INVALID**                  **INVALID**                  **INVALID**        |")
        else:
            print                       ("|                                                                                     |\n"
                                         "|        **INVALID**                  **INVALID**                  **INVALID**        |")
    else:
        print                           ("|                                                                                     |\n"
                                         "|        **INVALID**                  **INVALID**                  **INVALID**        |")
# User repeats or stops loop            
    continue_or_stop = input            ("|                                                                                     |\n"
                                         "| Press S to stop or any other key to continue: ")
    if continue_or_stop.upper() == 'S':
        break

# Ends user-friendly board
print                                   ("|                                                                                     |\n"
                                         "|                                   Have a good day!                                  |\n"
                                         " -------------------------------------------------------------------------------------") 