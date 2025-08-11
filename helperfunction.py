
import json
import logging
class Response():
    @staticmethod
    def response(remote,data):
        logging.basicConfig(filename="log.log",filemode='w',level=logging.info)
        logging.info('the message revered')
        try:

            remote.send_response(200)
            remote.send_header('Content-type','application/json')
            remote.end_headers()
            remote.wfile.write((data).encode())

        except Exception as e:
            remote.send_response(500)
            remote.end_headers()
            remote.wfile.write(json.dumps("the exception is {e}".encode()))    
