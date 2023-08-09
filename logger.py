from datetime import datetime


def logger(old_function):
    def wrapper(*args, **kwargs):
        date = datetime.now().strftime('%H:%M:%S %d.%m.%Y')
        result = old_function(*args, **kwargs)
        func_name = old_function.__name__
        log = f'date = {date}; func_name = {func_name}; args = {args}; kwargs = {kwargs}; result = {result}\n'
        with open('main.log', '+a', encoding='utf-8') as file:
            file.write(log)
        return result

    return wrapper


def logger_with_path(path):  
    def __logger(old_function):
        def wrapper(*args, **kwargs):
            date = datetime.now().strftime('%H:%M:%S %d.%m.%Y')
            result = old_function(*args, **kwargs)
            func_name = old_function.__name__
            log = f'date = {date}; func_name = {func_name}; args = {args}; kwargs = {kwargs}; result = {result}\n'
            with open(path, '+a', encoding='utf-8') as file:
                file.write(log)
            return result
        return wrapper

    return __logger