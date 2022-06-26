from dotenv import load_dotenv
import os

load_dotenv()
PAPER_END_POINT= 'https://paper-api.alpaca.markets'
PAPER_API_KEY=os.getenv('PAPER_API_KEY')
PAPER_SECRET_KEY=os.getenv('PAPER_SECRET_KEY')

END_POINT = r'https://api.alpaca.markets'
REAL_MONEY_API_KEY = os.getenv('REAL_MONEY_API_KEY')
REAL_MONEY_SECRET_KEY = os.getenv('REAL_MONEY_SECRET_KEY')