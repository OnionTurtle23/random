def transform_exp_to_log (base, exponent, y_value):
    base = str(base)
    exponent = str(exponent)
    y_value = str(y_value)
    print("Log " + base + " " + y_value + " = " + exponent)

print("I can help you transform an exponential expression into a logarithmic one")    
base = input("Please enter the base coefficient: ")
exponent = input ("Please enter its exponent: ")
y_value = input ("Please enter the value for Y, located on the other side of the equals sign:")

transform_exp_to_log(base, exponent, y_value)