from task_manager import TaskManager
import uuid

def new_task_program():
    task = { "id" : str(uuid.uuid1())}
    TaskManager.create_new_task("EMAIL",task)

def update_task_program():
    TaskManager.update_task_management_ext(None, "Test-Started", "ENDED", "c0978d27-93de-11ec-a40c-e4a7a032d709")

if __name__ == '__main__':
    #new_task_program()
    update_task_program()