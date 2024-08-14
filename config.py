import os

####################################
# Load .env file
####################################

try:
    from dotenv import load_dotenv, find_dotenv

    load_dotenv(find_dotenv("./.env"))
except ImportError:
    print("dotenv not installed, skipping...")

API_KEY = os.getenv("PIPELINES_API_KEY", "")
PIPELINES_DIR = os.getenv("PIPELINES_DIR", "./pipelines")
