def my_decorator(original_function):
    def my_wrapper():
        original_function()

    return my_wrapper()


def my_name(original_function):
    return original_function() + ' Piffer'


@my_name
def pessoa():
    return 'Lucas'


print(pessoa)
