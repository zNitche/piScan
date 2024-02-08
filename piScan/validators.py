# Custom models validators goes here

def validate_resolutions(resolutions_list):
    return True if (isinstance(resolutions_list, list) and
                    all(isinstance(res, int) for res in resolutions_list)) else False
