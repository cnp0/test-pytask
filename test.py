from task_runner import TestTask, run_task

class MyTask(TestTask):

    def standard_fn_1(data):
        pass

    def standard_fn_2(data):
        pass

    def standard_fn_3(data):
        pass

    def standard_fn_4(data):
        pass


if __name__ == "__main__":
    data = ""
    run_task(data, task=MyTask)