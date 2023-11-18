import json

from typing import Dict, List, Optional, Union

def load_json(filepath: str, 'r') -> Union[Dict, List]:
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def load_jsonl(filepath: str) -> List:
    data = []
    with open(file_path, 'r') as json_file:
        for line in json_file:
            raw_object = json.loads(line)
            data.append(raw_object)
    return data
