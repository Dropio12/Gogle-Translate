def remove_number(text: str) -> str:
    output = ''.join(c for c in text if not c.isdigit())
    return output
