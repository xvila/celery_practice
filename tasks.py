from celery import Celery

app = Celery("tasks", 
             backend="redis://127.0.0.1:6379",
             broker="redis://127.0.0.1:6379"
             )

# setting a task result expire allows me to actually get the results
# without these result.get() just times out.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

@app.task
def add(x, y):
    return x + y

if __name__ == "__main__":
    app.start()
