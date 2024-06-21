import config
from books_views import BooksListResource, BooksDetailsResource
from falcon import App
from kombu import Connection
from logging_middleware import LoggingMiddleware
from timing_middleware import TimingMiddleware
from stat_middleware import StatMiddleware

connection = Connection(config.AMQP_CONNECTION_URL)
stats_middleware = StatMiddleware(
    connection=connection,
    queue_name=config.STAT_QUEUE_NAME,
)

middlewares = [
    stats_middleware,
    LoggingMiddleware(),
    TimingMiddleware(),
]

books_list = BooksListResource()
book_details = BooksDetailsResource()

app = App(middleware=middlewares)

app.add_route("/books", books_list)
app.add_route("/books/{book_id}", book_details)