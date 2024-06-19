import os
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
from CNNClassifier import logger
import json
import joblib 
import base64
import yaml

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    # read the content ofyaml file and reture it 
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    
@ensure_annotations
def create_dir(path_dir:list,verbose=True):
    # create list of dir
    for path in path_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"dir is created at {path}")

@ensure_annotations
def save_json(path:Path,data:dict):
    # save the json data
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
    logger.info(f"Json file saved at: {path}")

@ensure_annotations
def load_json(path:Path)->ConfigBox:
    # load json file data
    with open(path) as f:
        content=json.load(f)
    logger.info("Json file loaded ")
    return ConfigBox(content)

@ensure_annotations
def save_bin(path:Path,data:Any):
    joblib.dump(value=data,filename=path)
    logger.info("Bineary file saved")

@ensure_annotations
def load_bin(path:Path)->Any:
    data=joblib.load(path)
    logger.info("bineary file loaded")
    return data

@ensure_annotations
def get_size(path:Path)->str:
    size_in_kb=round(os.path.getsize(path)/1024)
    return size_in_kb

@ensure_annotations
def decodeImage(imgstring,filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename,'wb') as f:
        f.write(imgdata)
        f.close()
@ensure_annotations
def encodeImage_IntoBased64(cropimagepath):
    with open(cropimagepath,'rb') as f:
        return base64.b64encode(f.read())