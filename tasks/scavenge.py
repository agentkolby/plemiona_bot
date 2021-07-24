from dotenv import load_dotenv 

import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from ..utilities.create_task_url import create_task_url

load_dotenv()

TASK_URL = os.environ.get("TASK_URL")

task_option = {"&screen=place&mode=scavenge"}

task_url = create_task_url(screen = 'place', mode = 'scavenge')

print(task_url)