def can_book(start, end, now, blocked, existing):
    """
    Check room availability based on AC1-AC5 contract.
    AC1: 0 <= start < end <= 1440; start > now
    AC2: duration <= 120
    AC3: reject if blocked
    AC4: reject overlap (touching endpoints are allowed)
    AC5: return bool, do not mutate existing
    """
    if blocked:
        return False

    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(now, int):
        return False

    if start < 0 or end > 1440 or start >= end:
        return False

    if start <= now:
        return False

    if (end - start) > 120:
        return False

    for b_start, b_end in existing:
        # Overlap check: intervals overlap if max(start1, start2) < min(end1, end2)
        if max(start, b_start) < min(end, b_end):
            return False

    return True