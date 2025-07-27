fruits = ["apple", "banana", "cherry"]

characteristics = {
    "name": 'Bob',
    "age": 25,
    "city": 'Moscow'
}

set_of_fruits = {"apple", "banana", "cherry"}

def mean(numbers: list[float]) -> float:
    """
    Возвращает среднее значение списка чисел.
    """
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    nums = [1.0, 2.5, 3.5]
    print("Среднее:", mean(nums))