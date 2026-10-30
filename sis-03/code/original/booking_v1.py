def can_book(start, end, now, blocked, existing):
    # AC1: Validate time range and require start to be after now
    if not all(isinstance(x, int) and not isinstance(x, bool)
               for x in (start, end, now)):
        return False

    if not (0 <= start < end <= 1440):
        return False

    if start <= now:
        return False

    # AC2: Duration must be at most 120 minutes
    if end - start > 120:
        return False

    # AC3: Reject if the requested time is blocked
    if blocked:
        return False

    # AC4: Reject overlapping existing bookings
    # Touching endpoints are allowed
    for existing_start, existing_end in existing:
        if start < existing_end and end > existing_start:
            return False

    # AC5: Return a boolean without modifying existing
    return True