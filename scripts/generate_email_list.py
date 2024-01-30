def generate_email_list(file_path: str, count: int) -> None:
    """Generate a sample email list for testing purposes.

    Args:
        file_path (str): The path to the file to save the email list.
        count (int): The number of sample email addresses to generate.
    """
    with open(file_path, 'w') as file:
        for i in range(count):
            file.write(f"user{i}@example.com\n")
    print(f"Generated {count} sample email addresses in {file_path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python generate_email_list.py <file_path> <count>")
    else:
        file_path = sys.argv[1]
        count = int(sys.argv[2])

        generate_email_list(file_path, count)
