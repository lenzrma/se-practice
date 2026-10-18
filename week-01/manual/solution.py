def process_marks(marks_input):
    valid_marks = []
    raw_items = [item.strip() for item in marks_input.split(',')]
    
    for item in raw_items:
        if item == '':
            continue
        try:
            val = float(item)
            if 0 <= val <= 100:
                if val.is_integer():
                    val = int(val)
                valid_marks.append(val)
        except ValueError:
            continue

    if not valid_marks:
        print("No valid marks")
        return

    count = len(valid_marks)
    avg = sum(valid_marks) / count
    highest = max(valid_marks)
    lowest = min(valid_marks)
    
    passing = sum(1 for m in valid_marks if m >= 50)
    pass_rate = (passing / count) * 100

    print(f"Valid marks: {count}")
    print(f"Average: {avg:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Pass rate: {pass_rate:.1f}%")

if __name__ == "__main__":
    print("--- Case A ---")
    process_marks("85, 23, 45, 90, 92")
    
    print("\n--- Case B ---")
    process_marks("88, 47, -5, 101, abc, 73, 50, , 100")
    
    print("\n--- Case C ---")
    process_marks("10, 20, 30")
    
    print("\n--- Case D ---")
    process_marks("abc, , xyz")