import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def say_hello(name="World"):
    """
    Return a friendly greeting.

    - If name is not provided, defaults to 'World'
    - If name is a string with leading/trailing spaces, they are stripped
    - If name is an empty string (after stripping), defaults to 'World'
    - If name is not a string, raises TypeError
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string")

    stripped = name.strip()

    if stripped == "":
        stripped = "World"

    return f"Hello, {stripped}!"


# Allow interactive input ONLY when running this file directly
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(say_hello(user_name))
