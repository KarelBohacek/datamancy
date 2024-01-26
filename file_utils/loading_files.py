import json

def load_json(filepath):
    """Load a JSON file from a filepath."""
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def load_jsonl(filepath):
    """Load a JSONL file from a filepath."""
    with open(jsonl_file_path, 'r') as jsonl_file:
        data = [json.loads(line) for line in jsonl_file]
    return data

def load_pickle(filepath: str):
    """Load a pickle file from a filepath."""
    with open(pickle_file_path, 'rb') as pickle_file:
        data = pickle.load(pickle_file)
    return data