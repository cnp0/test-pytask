class TestTask:

    @classmethod
    def run(self, data):

        self.standard_fn_1(data)
        self.standard_fn_2(data)
        self.standard_fn_3(data)
        self.standard_fn_4(data)

        print("Success!")


def run_task(data: any, task: TestTask):
    task.run(data)