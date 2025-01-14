
# fonction that will return of a number
def square():
    paramter = input("Please give a number: ")
    
    try:
        a = int(paramter)
        return a ** 2
    except Exception:
        try:
            b = float(paramter)
            return b ** 2
        except Exception:
            print("Le paramètre doit être un nombre !")
            return None

square_result = square()
if square_result is not None:
    print(f"The square number of your parameter is: {square_result}")
