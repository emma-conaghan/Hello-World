"""
Simple hello world function with enhanced logging and input handling.
"""
import logging

logger = logging.getLogger(__name__)

def say_hello(name="World"):
    """
    Return a friendly greeting with input validation/cleaning.
    """
    if not isinstance(name, str):
        logger.error("Invalid type for name: %s", type(name))
        raise TypeError("name must be a string")

    logger.info("Received name input: %r", name)

    stripped = name.strip()
    if stripped == "":
        logger.info("Empty name provided, defaulting to 'World'")
        stripped = "World"

    return f"Hello, {stripped}!"
