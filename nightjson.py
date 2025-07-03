import json
import os
from datetime import datetime

def add_to_json(file_path, new_data):
    """
        file_path (str): Путь к JSON-файлу
        new_data (dict): Словарь с данными для добавления

        add_to_json("data.json", {"key": "value"})
        add_to_json("data.json", {"number": 5, "name": "John"})
    """
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = {}
    else:
        data = {}
    
    data.update(new_data)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def remove_from_json(file_path, keys_to_remove):
    """
        file_path (str): Путь к JSON-файлу
        keys_to_remove (str/list): Ключ или список ключей для удаления

        remove_from_json("test.json", "nick")
        remove_from_json("test.json", ["nick", "numbers"])
    """
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            return
    else:
        return
    
    if isinstance(keys_to_remove, str):
        keys_to_remove = [keys_to_remove]
    
    for key in keys_to_remove:
        if key in data:
            del data[key]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def read_json(file_path, keys=None):
    """
    Читает JSON-файл и возвращает данные по ключам (включая вложенные).
    
    Args:
        file_path (str): Путь к JSON-файлу.
        keys (str|list|None): Ключ или список ключей. Поддерживает вложенность через точку ("mail.first") или списком ["mail", "first"].
                             Если None — возвращает весь JSON.
    
    Returns:
        dict|list|str|int|None: Данные по ключу или None, если ключ не найден или файл невалиден.
    """
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return None
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None
    
    if keys is None:
        return data
    
    # Если ключ передан как строка (например, "mail.first")
    if isinstance(keys, str):
        keys = keys.split('.')
    
    result = data
    for key in keys:
        if isinstance(result, dict) and key in result:
            result = result[key]
        else:
            return None  # Если ключ не найден
    
    return result