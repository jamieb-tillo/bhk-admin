import os

import pymongo
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(os.getenv('CONNECTION_STRING'))
