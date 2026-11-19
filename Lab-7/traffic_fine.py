def parse_ticket_id(ticket_id):
    """
    Parses a traffic ticket ID in the format 'PREFIX-YEAR-SERIAL'.
    Returns (prefix.upper(), year, serial) or None if input is invalid.
    Hardened against fuzzing / malformed inputs.
    """
    if ticket_id is None or not isinstance(ticket_id, str):
        return None
    ticket_id = ticket_id.strip()
    parts = ticket_id.split('-')
    if len(parts) != 3:
        return None
    prefix, year_str, serial_str = parts
    prefix = prefix.strip()
    if not prefix:
        return None
    try:
        year = int(year_str.strip())
        serial = int(serial_str.strip())
        return prefix.upper(), year, serial
    except (ValueError, TypeError, OverflowError):
        return None


def total_fines(amounts_csv):
    """
    Calculates total fine amount from comma-separated numbers.
    Caps total fine at 10,000. Returns 0 if input is invalid or empty.
    Hardened against fuzzing / malformed inputs.
    """
    if amounts_csv is None or not isinstance(amounts_csv, str):
        return 0
    amounts_csv = amounts_csv.strip()
    if not amounts_csv:
        return 0
    total = 0
    for a in amounts_csv.split(','):
        item = a.strip()
        if not item:
            continue
        try:
            val = int(item)
            if val > 0:
                total += val
        except (ValueError, TypeError, OverflowError):
            continue
    if total > 10000:
        total = 10000
    return total


def speed_excess(reading):
    """
    Calculates percentage speed excess from a 'speed/limit' string.
    Returns percentage as integer, or 0 if within limit or invalid.
    Hardened against fuzzing / malformed inputs and ZeroDivisionError.
    """
    if reading is None or not isinstance(reading, str):
        return 0
    reading = reading.strip()
    parts = reading.split('/')
    if len(parts) != 2:
        return 0
    try:
        speed = int(parts[0].strip())
        limit = int(parts[1].strip())
        if limit <= 0:
            return 0
        if speed <= limit:
            return 0
        return (speed - limit) * 100 // limit
    except (ValueError, TypeError, ZeroDivisionError, OverflowError):
        return 0


def main():
    print("==== Running parse_ticket_id ====")
    user_input = input("Enter a ticket ID (e.g. TF-2024-0456): ")
    result = parse_ticket_id(user_input)
    print("Ticket Prefix, Year and Serial:", result)

    print("\n==== Running total_fines ====")
    user_input = input("Enter fine amounts as CSV (e.g. 500,1200,300): ")
    result = total_fines(user_input)
    print("Total Fines:", result)

    print("\n==== Running speed_excess ====")
    user_input = input("Enter speed/limit (e.g. 72/60): ")
    result = speed_excess(user_input)
    print("Percent Over Limit:", result)


if __name__ == "__main__":
    main()
