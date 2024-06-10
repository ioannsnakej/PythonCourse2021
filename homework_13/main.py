import logging
from books_api import app

logging.basicConfig(level=logging.INFO)

def main():
    from waitress import serve
    serve(app, host="127.0.0.1", port="8000")

if __name__ == '__main__':
    main()

