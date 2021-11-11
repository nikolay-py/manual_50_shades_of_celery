from cwebapp import init_celery

app = init_celery()


# Возможность добавить еще один модуль очередями, который на прописан в конфигураци
# app.conf.imports = app.conf.imports + ("cwebapp.tasks.task1",)

"""
Вызов воркера
Из разных терминалов, или контейнеров
celery -A celery_worker:app worker -n high_priority -Q proverky_bro -c 2 --loglevel=info
celery -A celery_worker:app worker -n low_priority -Q prochee -c 6 --loglevel=info

Можено указывать просто celery -A celery_worker (без двоеточия), тогда слелри будет сама искать
имено похожие на название приложения селери

curl запросы для теста
curl -i -X GET http://127.0.0.1:5000/1
"""

