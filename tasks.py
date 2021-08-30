from app import app
from time import sleep


@app.task(bind=True, name="long_running_task")
def long_running_task(self):
    sleep(2)
    return 1

def main():
    task = long_running_task.s().delay()
    while (task.status == 'PENDING'):
        print(task.status)
        sleep(1)
    
    print(task.status)

if __name__ == "__main__":
    main()
