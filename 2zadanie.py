class MyZeroDiv(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == "__main__":
    from sys import exit

    a = 0
    b = 0
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
    except:
        print("Некоректное число")
        exit(1)

    try:
        if b == 0:
            raise MyZeroDiv("Не делится")
        print(f"Равно {a}/{b} = {a/b}")
    except MyZeroDiv as ex:
        print(ex)

