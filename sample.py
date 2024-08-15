from dotenv import load_dotenv
import os 

def auth():
    load_dotenv()
    username=os.getenv("USERNAMES")
    password=os.getenv("PASSWORD")
    print(username,password)

auth()