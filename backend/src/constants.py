from dotenv import load_dotenv
from os import getenv

load_dotenv('../.env')

DB_NAME = getenv('DB_NAME')
DB_USER = getenv('DB_USER')
DB_PASSWORD = getenv('DB_PASSWORD')
DB_HOST = getenv('DB_HOST')

HASH_SALT = getenv('HASH_SALT')

VARCHAR_MIN_LENGTH = getenv('VARCHAR_MIN_LENGTH')
VARCHAR_MAX_LENGTH = getenv('VARCHAR_MAX_LENGTH')
TEXT_MAX_LENGTH = getenv('TEXT_MAX_LENGTH')

char_min = VARCHAR_MIN_LENGTH
char_max = VARCHAR_MAX_LENGTH
text_max = TEXT_MAX_LENGTH