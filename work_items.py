# initial import
from RPA.Robocorp.WorkItems import WorkItems

# class workitems


class WorkItems:
    # initial workitems
    def __init__(self) -> None:
        self.WorkItems = WorkItems()

    def set_work_item(self, name, value):
        self.WorkItems.set_workitem_variable(name, value)
        return self.WorkItems
