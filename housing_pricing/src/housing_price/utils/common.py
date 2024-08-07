import os 
import yaml
from box.exceptions import BoxValueError
from housing_price.logging import logger
from box import ConfigBox
from typing import Any

from pathlib import Path
import pickle 



def read_yaml(path_to_yaml:Path)-> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:

            content =yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} laoded sucessfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e



def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at :{path} ")


            
def get_size(path:Path)->str:
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"



def save_tuple_to_file(tuple_data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(tuple_data, file)



def load_tuple_from_file(filename):
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    return data   
        