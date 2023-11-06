import json
import httpx

def check_email_exists(email):
    """Checks if an email address exists in all social media."""
    # Get the list of all social media platforms.
    social_media_platforms = [
        "facebook",
        "twitter",
        "instagram",
        "linkedin",
        "github",
    ]
    # Check if the email address exists in each social media platform.
    for social_media_platform in social_media_platforms:
        url = f"https://api.{social_media_platform}.com/v1/users?q={email}"
        response = requests.get(url)
        # If the response is successful, check if the email address exists.
        if response.status_code == 200:
            data = json.loads(response.content)
            if data["results"]:
                return True

    # If the email address does not exist in any social media platform, return False.
    return False

# Get the email address from the user.
email = input("Enter the email address: ")
# Check if the email address exists in all social media platforms.
if check_email_exists(email):
        print("The email address exists in all social media platforms.")
else:
        print("The email address does not exist in any social media platforms.")