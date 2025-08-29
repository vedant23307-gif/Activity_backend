
import json
import logging
import os


def http_response(remote,data):
    try:
        log_path = os.path.join(os.path.dirname(__file__), "log.log")
        logging.basicConfig(filename=log_path,filemode='a',level=logging.INFO)
        remote.send_response(200)
        remote.send_header('Content-type','application/json')
        remote.end_headers()
        logging.info('the message revered')
        logging.error('the messsage')
        remote.wfile.write((data).encode())

    except Exception as e:
        remote.send_response(500)
        remote.end_headers()
        remote.wfile.write(json.dumps("the exception is {e}".encode()))    
