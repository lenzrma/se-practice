def analyze_marks(marks, pass_mark=50):
    if not marks:
        raise ValueError("Marks list cannot be empty.")
    
    for m in marks:
        if not isinstance(m, (int, float)):
            raise ValueError("All marks must be numeric.")
        if not (0 <= m <= 100):
            raise ValueError("Marks must be between 0 and 100.")

    total = sum(marks)
    count = len(marks)
    average = total / count
    highest = max(marks)
    lowest = min(marks)
    
    passed_count = sum(1 for m in marks if m >= pass_mark)
    pass_rate = (passed_count / count) * 100.0

    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "pass_rate": pass_rate
    }