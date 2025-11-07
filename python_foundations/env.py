# import os

# value = os.environ.get("FAV_COLOR")
# print("Your favorite is:", value)


from dotenv import load_dotenv  # Loads environment variables from a .env file. It's a library that makes it easy to manage environment variables in a project.
load_dotenv(override=True)

