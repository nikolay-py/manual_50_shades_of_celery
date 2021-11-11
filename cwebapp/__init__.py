from flask import Flask
from cwebapp.extensions import celery_app
from config import DevelopmentConfig
from cwebapp.tasks.task1 import dummy_task, uuuuuu


def create_app() -> Flask:
    """Create and configure Flask app."""
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)
    """
    Инициализируем celery во время создания приложения, 
    т.к. нам нужно чтобы celery запустился раньше, чем к нам начнут поступать задачи
    """
    init_celery(app)

    return app


"""
Фабрика создания приложения celery
Создаем для того, чтобы запускаемые задачи выполнялись в котексте Flask приложения

Не можем никуда вынести, т.к. присутвсует app или create_app.
Т.е. если мы его вынесенм, и при этом импортируем функцию init_celery,
то пойдут ошибка циклического импорта.
Одному нужны полные данные о другом, но они так не могут, т.к. оба
пока друг без друга не сформированы...
"""
def init_celery(app=None):
    app = app or create_app()
    celery_app.conf.update(app.config.get("CELERY", {}))

    class ContextTask(celery_app.Task):
        """Make celery tasks work with Flask app context"""

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app.Task = ContextTask
    return celery_app

app = create_app()


@app.route("/1")
def hello_world():
    uuuuuu.delay()
    return "<p>Hello, World!</p>"

@app.route("/2")
def hello_world2():
    dummy_task.delay()
    return "<p>TTTUI, World!</p>"

"""
curl - запросы
curl -i -X GET http://rest-api.io/items
curl -i -X GET http://rest-api.io/items/5069b47aa892630aae059584
curl -i -X DELETE http://rest-api.io/items/5069b47aa892630aae059584
curl -i -X POST -H 'Content-Type: application/json' -d '{"name": "New item", "year": "2009"}' http://rest-api.io/items
curl -i -X PUT -H 'Content-Type: application/json' -d '{"name": "Updated item", "year": "2010"}' http://rest-api.io/items/5069b47aa892630aae059584
"""