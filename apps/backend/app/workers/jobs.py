from rq import Queue
from redis import Redis
from ..core.config import settings
from weasyprint import HTML
from pathlib import Path

redis = Redis.from_url(settings.redis_url)
queue = Queue(connection=redis)

def generate_pdf(html: str, dest: str):
    HTML(string=html).write_pdf(dest)
    return dest
