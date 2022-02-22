import json

def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            print("is __dict__ type",obj)
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    print('k == key')
                    arr.append(v)
        elif isinstance(obj, list):
            print("is __list__ type",obj)
            for item in obj:
                extract(item, arr, key)
        elif isinstance(obj, str):
            print(obj)
        return arr

    values = extract(obj, arr, key)
    return values

def check_update_list(ele, prefix, new_status):
    for i in range(len(ele)):
        if (isinstance(ele[i], list)):
            print("---->check_update_list--->list")            
            check_update_list(ele[i], prefix+"["+str(i)+"]")
        elif (isinstance(ele[i], str)):
            print("---->check_update_list--->str")            
            _existing_task = json.loads(ele[i].replace("\'", "\""))            
            if _existing_task['task_id'] == new_status.id:
                # get task status list
                current_task_conditions = _existing_task['conditions']
                current_task_conditions.append(new_status)
            ele[i] = _existing_task
            printField(ele[i], prefix+"["+str(i)+"]")
        else:
            print("---->check_update_list--->dict")
            check_dict(ele[i], prefix+"["+str(i)+"]", new_status)

def check_dict(jsonObject, prefix, status):
    for ele in jsonObject:
        if (isinstance(jsonObject[ele], dict)):
            print("---->check_dict--->dict")
            check_dict(jsonObject[ele], prefix+"."+ele, status)
        elif (isinstance(jsonObject[ele], list)):
            print("---->check_dict--->list")
            check_update_list(jsonObject[ele], prefix+"."+ele, status)
        elif (isinstance(jsonObject[ele], str)):
            print("---->check_dict--->str")
            printField(jsonObject[ele],  prefix+"."+ele)

def printField(ele, prefix):
    print (prefix, ":" , ele)


def test_function_usage():
    tasks_obj_as_dict = {} #TaskManager.get_task_management()    
    #Iterating all the fields of the JSON
    for element in tasks_obj_as_dict:
        #If Json Field value is a Nested Json
        if (isinstance(tasks_obj_as_dict[element], dict)):
            print(" main _dict")
            check_dict(tasks_obj_as_dict[element], element)
        #If Json Field value is a list
        elif (isinstance(tasks_obj_as_dict[element], list)):
            print("main list")
            check_update_list(tasks_obj_as_dict[element], element)
        #If Json Field value is a string
        elif (isinstance(tasks_obj_as_dict[element], str)):
            print("main str")
            printField(tasks_obj_as_dict[element], element)
