import logging
from waitress import serve
from books_api import app
logging.basicConfig(level=logging.INFO)

def main():
    serve(app, port="8000")

if __name__ == '__main__':
    main()

