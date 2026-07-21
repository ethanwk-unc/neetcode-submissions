def divide_numbers(a: str, b: str) -> None:
    try:
        numa = int(a)
        numb = int(b)
        result = numa / numb
        print(result)
    except ValueError:
        print("Error: Invalid value!")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception as error:
        print("An error occurred:", error)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
