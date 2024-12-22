class SumCalculator:
    def calculate_sum(self, numbers):
        if not isinstance(numbers, list):
            raise ValueError("Аргумент должен быть списком чисел.")
        return sum(numbers)
