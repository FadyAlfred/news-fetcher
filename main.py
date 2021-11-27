from celery import Celery
from celery.schedules import crontab

from config import CELERY_BROKER
from utils import NewsFetcher

app = Celery('news_fetcher', broker=CELERY_BROKER)
app.autodiscover_tasks()

news_fetcher = NewsFetcher()


@app.task
def print_articles():
    articles = news_fetcher.fetch_articles()
    for article in articles:
        print(article)


app.conf.beat_schedule = {
    # Executes every 5 minutes.
    'run-every-5-minutes': {
        'task': 'main.print_articles',
        'schedule': crontab(minute="*/5"),
        'args': (),
    },
}
