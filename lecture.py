# def template(old_function):
#     """простой декоратор"""
#
#     def new_function(*args, **kwargs):
#         ...  # код до вызова исходной функции
#         result = old_function(*args, **kwargs)
#         ...  # код после вызова исходной функции
#         return result
#
#     return new_function
#
#
# @template
# def hello_world():
#     return 'Hello World'

# def template(param):
#     """параметризованный декоратор"""
#
#     def _template(old_function):
#
#         def new_function(*args, **kwargs):
#             ...  # код до вызова исходной функции
#             print(param)  # можем использовать параметр
#
#             result = old_function(*args, **kwargs)
#             ...  # код после вызова исходной функции
#             return result
#
#         return new_function
#
#     return _template
#
#
# @template(param=42)
# def hello_world():
#     return 'Hello World'

# from functools import wraps
#
#
# def trace_decorator(some_function):
#     @wraps(some_function)  # wraps подменяет метаданные функции
#     def new_function(*args, **kwargs):
#         print(f'Вызываем {some_function.__name__} c аргументами {args} и {kwargs}')
#         result = some_function(*args, **kwargs)
#         print(f'Вернули результат {result}')
#         return result
#
#     return new_function
#
#
# @trace_decorator
# def hello_world():
#     return 'Hello World'

# import requests
#
#
# def cached(cache_size):
#     def _cached(old_function):
#
#         CACHE = {}
#
#         def new_function(*args, **kwargs):
#
#             key = f'{args}_{kwargs}'
#             if key in CACHE:
#                 return CACHE[key]
#             result = old_function(*args, **kwargs)
#             if len(CACHE) >= cache_size:
#                 CACHE.popitem()
#             CACHE[key] = result
#             return result
#
#         return new_function
#     return _cached
#
#
# @cached(cache_size=10)
# def get_people(people_id):
#
#     return requests.get(f'https://swapi.dev/api/people/{people_id}').json()