import json
from converter import datetime_converter
from status import Status

class Task:
    def __init__(self, task_name, task_id, message, conditions):
        self.task_name = task_name
        self.task_id = task_id
        self.conditions = conditions
        self.message = message

    def __iter__(self):
        yield from {
            "task_name": self.task_name,
            "task_id": self.task_id,
            "conditions": self.conditions,
            "message":  self.message
        }.items()

    def __str__(self):
        return json.dumps(self.to_json(), ensure_ascii=False, default = datetime_converter)
    
    def __repr__(self):
        return self.__str__()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def to_json(self):
        to_return = {"task_name": self.task_name, "task_id": self.task_id, "message": self.message, "conditions":self.conditions}
        statuses = []
        for status in self.conditions:
            print("checking status type ->",type(status)) 
            # print(" to_json status type", )
            if isinstance(status, dict):
                from collections import namedtuple
                x = namedtuple("ObjectName", status.keys())(*status.values())
                conditions = []
                print("printing x data",x)
                s = Status(x.id, x.status_name, x.status_datetime, x.message)
                statuses.append(s.to_json())
            if isinstance(status,Status):    
                #x = namedtuple("ObjectName", status.keys())(*status.values())
                #s = Status(status.id, status.status_name, status.status_datetime, status.message)
                statuses.append(status.to_json())  

        # # statuses = []
        # # for status in self.conditions:
        # #     statuses.append(status.__dict__)        


        # #statuses = {}
        # #for key, status in self.conditions.items():
        # #     single_status = []
        # #     for status_set in status:
        # #         single_status.append(status_set.__dict__)
        # #         statuses[key] = single_status

        to_return["conditions"] = statuses
        return to_return
        
# import json
# from task_store.converter import datetime_converter

# class Task:
#     def __init__(self, task_name, task_id, message, conditions):
#         self.task_name = task_name
#         self.task_id = task_id
#         self.conditions = conditions
#         self.message = message

#     def __iter__(self):
#         yield from {
#             "task_name": self.task_name,
#             "task_id": self.task_id,
#             "conditions": self.conditions,
#             "message":  self.message
#         }.items()

#     def __str__(self):
#         return json.dumps(self.to_json(), ensure_ascii=False, default = datetime_converter)
    
#     def __repr__(self):
#         return self.__str__()

#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__, 
#             sort_keys=True, indent=4)

#     def to_json(self):
#         to_return = {"task_name": self.task_name, "task_id": self.task_id, "message": self.message}
#         statuses = []
#         for status in self.conditions:
#             statuses.append(status.__dict__)        
#         #statuses = {}
#         #for key, status in self.conditions.items():
#         #     single_status = []
#         #     for status_set in status:
#         #         single_status.append(status_set.__dict__)
#         #         statuses[key] = single_status

#         to_return["conditions"] = statuses
#         return to_return