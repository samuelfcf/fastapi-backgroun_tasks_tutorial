import time
from fastapi import FastAPI, BackgroundTasks


app = FastAPI()


def heavy_query_in_db():
    print('start query...')
    time.sleep(4)
    print('end query!')


def heavy_calculation():
    print('start heavy calculation...')
    time.sleep(6)
    print('end calculataion!')


def heavy_process():
    heavy_query_in_db()
    heavy_calculation()


@app.get("/with-bg-task")
def heavy_process_route(backgroun_tasks: BackgroundTasks):
    start = time.time()

    backgroun_tasks.add_task(
        heavy_process
    )

    end = time.time()
    return {"Execution time": f"{end - start}"}


@app.get("/without-bg-task")
def heavy_process_route_with_background_tasks():
    start = time.time()

    heavy_process()

    end = time.time()
    return {"Execution time": f"{end - start}"}