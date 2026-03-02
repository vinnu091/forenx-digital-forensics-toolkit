# seventh
import uuid
from apscheduler.schedulers.background import BackgroundScheduler

from .hash_utils import generate_file_hashes

from .task_store import tasks

scheduler = BackgroundScheduler()
scheduler.start()


def scan_file_task(task_id, file_obj):
    hashes = generate_file_hashes(file_obj)

    tasks[task_id] = {
        "status": "completed",
        "result": hashes
    }


def start_background_scan(file_obj):
    task_id = str(uuid.uuid4())

    tasks[task_id] = {"status": "processing"}

    scheduler.add_job(
        scan_file_task,
        args=[task_id, file_obj],
        id=task_id,
        replace_existing=True
    )

    return task_id