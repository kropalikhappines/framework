class GetRequest:
    @staticmethod
    def get_request_pars(data):
        result = {}
        if data:
            params = data.split('&')
            for el in params:
                key, value = el.split('=')
                result[key] = value
        return result


class PostRequest:
    @staticmethod
    def get_wsgi_inpt_data(data):
        content_length_data = data.get('CONTENT_LENGTH')

        content_length = int(content_length_data) if content_length_data else 0
        inf = data['wsgi.input'].read(content_length) if content_length > 0 else b''
        return inf

    def pars_wsgi_input_data(self, data):
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = GetRequest.get_request_pars(data_str)
        return result

    def get_requests(self, environ):
        data = self.get_wsgi_inpt_data(environ)
        data = self.pars_wsgi_input_data(data)
        return data