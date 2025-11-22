def perform_operation(num1: float, num2: float, operation: str):
    if operation =="add":
        return(num1 + num2)
    if operation =="subtraction":
        return (num1 - num2)
    if operation =="multiplication":
        return (num1 * num2)
    if operation =="division":
        if num2 == 0:
            return "you cannot divide by zero"
        else:
            return(num1 / num2)

    
    

