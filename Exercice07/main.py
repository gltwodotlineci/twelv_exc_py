
# fonction that will return of a number
def square(parametre):
    try:
        a = int(parametre)
        return a ** 2
    except Exception:
        try:
            b = float(parametre)
            return b ** 2
        except (ValueError, TypeError):
            print("Le paramètre doit être un nombre !")
            return None

square_result = square(5)
if square_result is not None:
    print(f"The square number of your parameter is: {square_result}")
