class Error(Exception):
    pass


class FormulaError(Error):
    print("Formula Error Caught")


formula = input("Enter formula...")
expressions = [char for char in formula]
print("Expressions are...", expressions)
try:
    if len(expressions) < 3:
        raise FormulaError
    float_value1 = float(expressions[0])
    float_value2 = float(expressions[2])
    if expressions[1] != '+' and expressions[1] != '-':
        print("About to raise Formula Error")
        raise FormulaError
    print(formula, " = ", end=" ")
    print(eval(formula))

except FormulaError as fe:
    print("Something wrong with the formula...")

except ValueError as ve:
    raise FormulaError
