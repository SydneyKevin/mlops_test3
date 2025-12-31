def format_trip_count(count: int) -> str:
    """Return a human-friendly string for trip counts."""
    if count < 0:
        raise ValueError("count cannot be negative")
    return f"{count} trips" if count != 1 else "1 trip"
