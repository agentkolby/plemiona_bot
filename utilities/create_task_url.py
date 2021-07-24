from dotenv import load_dotenv 

import os

load_dotenv()

TASK_URL = os.environ.get("TASK_URL")

def create_task_url(**kwargs):

    final_url = TASK_URL

    for key, value in kwargs.items():

        add_url = "&"
        add_url += key
        add_url += "="
        add_url += value

        final_url += add_url

    return final_url