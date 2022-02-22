import json
from converter import datetime_converter

class Status:
    def __init__(self, id, status_name, datetime, message):
        self.id = id
        self.status_name = status_name
        self.datetime = datetime
        self.message = message
    
    def __iter__(self):
        yield from {
            "id": self.id,
            "status_name": self.status_name,
            "datetime": self.datetime,
            "message": self.message
        }.items()
    
    def __str__(self):
        return json.dumps(self.to_json(), ensure_ascii=False, default = datetime_converter)
   
    def __repr__(self):
        return self.__str__()
    
    def to_json(self):
        to_return = {"id": self.id, "status_name": self.status_name, "status_datetime": self.datetime, "message":self.message}
        return to_return
    
    @staticmethod
    def from_json(json_dct):        
      return Status(json_dct['id'],
                    json_dct['status_name'],
                    json_dct['datetime'],
                    json_dct['message'])