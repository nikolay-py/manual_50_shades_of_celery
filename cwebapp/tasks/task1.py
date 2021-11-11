import time
from cwebapp.extensions import celery_app

@celery_app.task
def add(x, y):
    return x + y

@celery_app.task(name='wweb.ok')
def dummy_task():
    return "OK"

@celery_app.task(name='uuu.PRverka')
def uuuuuu():
    time.sleep(10)
    print("ПРоверка связи 2")
    return "OK"


"""
В конфигурации укажем, что задачи, 
чьи имена начинаются с uuu.* направляем в очередь uuu_proverky_bro
...

"task_routes": {
    'uuu.*': {'queue': 'uuu_proverky_bro'},
    'wweb.*': {'queue': 'wweb_prochee'},
}
"""