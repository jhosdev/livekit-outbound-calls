from livekit.agents.llm import function_tool


@function_tool()
async def authenticate_user(username: str, password: str) -> str:
    """
    Authenticate a user with the provided username and password.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        str: A message indicating whether the authentication was successful or not.
    """
    # Placeholder for actual authentication logic
    if username == "admin" and password == "password":
        return "Authentication successful"
    else:
        return "Authentication failed"
