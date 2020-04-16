from urllib.request import ssl, socket
import datetime

port = '443'
ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'


class Ssl:
    def __init__(self, domain):
        self.domain = domain

    def check_ssl_time(self):
        context = ssl.create_default_context()
        with socket.create_connection((self.domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=self.domain) as ssock:
                ssl_info = ssock.getpeercert()

        time_left = datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt) - datetime.datetime.utcnow()
        return time_left.days

    def check_ssl(self):
        try:
            return self.check_ssl_time()
        except (ssl.CertificateError, ssl.SSLError):
            return 'cert error'
        except (socket.timeout, socket.gaierror, socket.error):
            return 'cannot connect'

