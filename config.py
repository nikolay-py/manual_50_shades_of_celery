"""Application initialization."""
import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    """Base initialization config."""

    DEBUG = False
    SECRET_KEY = None

    """Celery settings."""
    CELERY = {
        "broker_url": os.environ.get("CELERY_BROKER_URL"),
        "result_backend": os.environ.get("CELERY_RESULT_BACKEND_URL"),
        "task_routes": {
            'uuu.*': {'queue': 'proverky_bro'},
            'wweb.*': {'queue': 'prochee'},            
        },
        "include": [
            'cwebapp.tasks.task1',
        ],        
    }
    
    """
    broker_url - адрес брокера очередей
    result_backend - адрес базы, где храним состояния задач
    task_routes - таски с какими именами в какую очередь будем направлять, см. чек лист и task1.py

    include = imports - в каком моуделе храниться список тасков. Иначе селери их найдет.
    Но найдет если задача испортирована в модуль с приложением, в т.ч. через блюпринт, или 
    зарегестированное в приложении апи.
    Также можно передать список через оперативную (app.conf.) настройку конфигурации
    app.conf.imports = app.conf.imports + ("cwebapp.tasks.task1",)
    см. celery_worker.py
    
    """


class ProductionConfig(Config):
    """Production config."""


class DevelopmentConfig(Config):
    """Development config."""
    ENV = "development"
    DEBUG = ENV == "development"
