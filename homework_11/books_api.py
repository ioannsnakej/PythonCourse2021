from books_views import BooksListResource, BooksDetailsResource
from falcon import App
from logging_middleware import LoggingMiddleware
from timing_middleware import TimingMiddleware

middlewares = [
    LoggingMiddleware(),
    TimingMiddleware(),
]

books_list = BooksListResource()
book_details = BooksDetailsResource()

app = App(middleware=middlewares)

app.add_route("/books", books_list)
app.add_route("/books/{book_id}", book_details)