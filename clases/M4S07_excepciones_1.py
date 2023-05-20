try:
    raise Exception("Rut", "11.111.111-1", "Invalidate rut format")
except Exception as error:
    print(type(error))
    print(error.args)
    print(error)

    key, value, message = error.args

    print(f'key --> {key}')
    print(f'value --> {value}')
    print(f'message --> {message}')