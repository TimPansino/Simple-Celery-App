import os

# Based on https://github.com/bstiel/celery-filesystem-broker

from celery import Celery


broker_url = os.getenv("CELERY_BROKER_URL", "filesystem://")
broker_dir = os.getenv("CELERY_BROKER_FOLDER", "./broker")

for f in ["out", "processed", "results"]:
    if not os.path.exists(os.path.join(broker_dir, f)):
        os.makedirs(os.path.join(broker_dir, f))


# Initialize Celery
conf = {
    'broker_url': broker_url,
    'broker_transport_options': {
        'data_folder_in': os.path.join(broker_dir, 'out'),
        'data_folder_out': os.path.join(broker_dir, 'out'),
        'data_folder_processed': os.path.join(broker_dir, 'processed')
    },
    'result_backend': "file://%s" % str(os.path.join(broker_dir, 'results')),
    'imports': ('tasks',),
    'result_persistent': False,
    'task_serializer': 'json',
    'result_serializer': 'json',
    'accept_content': ['json']}

app = Celery(__name__, **conf)
