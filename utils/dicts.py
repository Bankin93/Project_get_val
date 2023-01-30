def get_val(collection, key, default='git'):
    """Функция возвращает значение из словаря по переданному ключу"""
    if collection == {}:
        return default
    return collection[key]
