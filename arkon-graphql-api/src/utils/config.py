import os
from dotenv import load_dotenv

load_dotenv()

HOST_MONGODB = os.getenv('HOST_MONGODB')
DATABASE_MONGODB = os.getenv('DATABASE_MONGODB')