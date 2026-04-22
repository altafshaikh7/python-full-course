def https_status(status_code):
    match status_code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status Code"

# Example usage
print(https_status(200))  # Output: OK
print(https_status(404))  # Output: Not Found
print(https_status(500))  # Output: Internal Server Error
print(https_status(403))  # Output: Unknown Status Code