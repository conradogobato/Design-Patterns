class Response:
    def response():
        print('Response!!')

class Proxy:
    def __init__(self, conn : Response):
        self.conn = conn

    def response(self):
        return self.conn.response()

class Request:
    def __init__(self, conn: Proxy):
        self.conn = conn

    def get_response(self):
        self.conn.response()


