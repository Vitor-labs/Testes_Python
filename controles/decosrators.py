import functools as ft


def repeat(num_times):
    def decorator_repeat(func):
        @ft.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat


def debug(func):
    @ft.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Executando {func.__name__}')
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'{func.__name__}({signature})')
        value = func(*args, **kwargs)
        print(f'Retornando {value!r}')
        return value
    return wrapper


def apresentacao(func):
    @ft.wraps(func)
    def wrapper(*args, **kwargs):
        print('Olá, ')
        retorno = func(*args, **kwargs)
        return retorno
    return wrapper


@debug
@apresentacao
@repeat(num_times=3)
def greet(name):
    presentation = 'bem vindo {}'.format(name)
    print(presentation)
    return presentation


greet('World')


# def apresentacao(func):
#     @ft.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Olá')
#         retorno = func(*args, **kwargs)
#         return retorno
#     return wrapper

# @apresentacao
# def faz_algo(nome):
#     return "bom dia " + nome

# #faz_algo = apresentacao(faz_algo)
# print(faz_algo('vitor'))
# print(faz_algo.__name__)
