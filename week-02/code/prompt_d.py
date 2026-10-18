def analyze_marks(marks, pass_mark=50):
    """
    Analyze a list of student marks.

    Args:
        marks: List of integers or floats from 0 to 100.
        pass_mark: Minimum mark required to pass. Defaults to 50.

    Returns:
        A dictionary containing average, highest, lowest, and pass_rate.

    Raises:
        ValueError: If marks is empty, contains non-numeric values,
                    or contains a mark outside the 0-100 range.
    """
    if not marks:
        raise ValueError("marks cannot be empty")

    for mark in marks:
        if not isinstance(mark, (int, float)):
            raise ValueError("all marks must be numeric")
        if not 0 <= mark <= 100:
            raise ValueError("marks must be between 0 and 100")

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    passed = sum(mark >= pass_mark for mark in marks)
    pass_rate = round((passed / len(marks)) * 100, 2)

    return {
        "average": float(average),
        "highest": highest,
        "lowest": lowest,
        "pass_rate": pass_rate
    }


# Example
result = analyze_marks([40, 60, 80], 50)
print(result)
# {'average': 60.0, 'highest': 80, 'lowest': 40, 'pass_rate': 66.67}