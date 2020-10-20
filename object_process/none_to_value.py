def none_to_value(obj, value):
    if type(obj) is dict:
        for key, obj_value in obj.items():
            if obj_value is None:
                obj[key] = value
            else:
                none_to_value(obj_value, value)

    if type(obj) is list:
        for index in range(len(obj)):
            if obj[index] is None:
                obj[index] = value
            else:
                none_to_value(obj[index], value)