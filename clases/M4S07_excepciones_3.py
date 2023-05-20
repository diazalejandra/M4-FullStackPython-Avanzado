class CustomHttpException(Exception):
    def __init__(self, code=500, message="Internal Server Error"):
        self.code = code
        self.message = message
    
try:
    raise CustomHttpException
except Exception as error:
    print(error.code)
    print(error.message)

try:
    raise CustomHttpException(400, "Bad Request")
except Exception as error:
    print(error.code)
    print(error.message)