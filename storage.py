import json  

def save_data(filename, data):
    """
    Save data to a JSON file.
    Args:
        filename (str): The name of the JSON file to save the data.
        data (list or dict): The data to be saved to the file.
    """
    with open(filename, 'w') as f:  
        json.dump(data, f)  

def load_data(filename):
    """
    Load data from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the data from.

    Returns:
        list or dict: The data loaded from the file.
    """
    try:
        with open(filename, 'r') as f:  
            return json.load(f)  
    except FileNotFoundError: 
        return [] 
