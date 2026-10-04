class InvalidError(Exception):
    pass

def process_input(value):
    if value<0:
        raise InvalidError("Input must be non negative")
    return value**0.5
try:
    print(process_input(-5))
except InvalidError as e:
    print(f"Error {e}")