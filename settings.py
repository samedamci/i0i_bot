#!/usr/bin/env python3

import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), "environment")
load_dotenv(dotenv_path)
TOKEN = os.getenv("TOKEN")
