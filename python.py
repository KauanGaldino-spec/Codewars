def derive(coefficient, exponent):
    
    new_coefficient = coefficient * exponent

    new_exponent = exponent - 1

    return f"{new_coefficient}x^{new_exponent}"


print(derive(7, 8))  
print(derive(5, 9))  