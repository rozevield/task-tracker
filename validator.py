def validate_id(idx, target):
    if not idx <= len(target) or idx < 1:
        raise ValueError('ID not found')
    

def idx_and_desc_converter(idx, desc):
    try:
        idx = int(idx)
    except:
        raise ValueError('>> update __ << must be an interger <id>')

    try:
        description = str(desc)
    except:
        raise ValueError('>> update <id> __ << must be a string <description>')
    
    return idx, description


def idx_converter(idx, error_massage: str):
    try:
        idx = int(idx)

    except:
        raise ValueError(error_massage)
    
    return idx


def is_2_items(target, error_massage: str):
    if len(target) < 2:
        raise ValueError(error_massage)
    
    
def is_3_items(target, error_massage:str):
    if len(target) < 3:
        raise ValueError(error_massage)
