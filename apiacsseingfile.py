#this is the priogram related to accseing the file for chrom using the http 
from http.server import BaseHTTPRequestHandler,HTTPServer
import pandas as pd
import json
def read(filename):
    with open(filename,'r')as file:
        data=file.read()
    return data


class Get(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/json':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            repose=read('jsonfile.json')
            self.wfile.write(repose.encode())
        if self.path=='/excel':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            response=pd.read_excel('ai.xlsx')
            responses = response.to_json(orient='records')
            self.wfile.write(responses.encode())
        else:
            self.send_response(404,'file not found')
    def do_POST(self):
        if self.path =='/json/creat':
            lenth=int(self.headers.get('Contant-Lenth',0))
            data=self.rfile.read(lenth)
            with open('jsonfile.json','a') as f:
                f.append(data)
            self.wfile.write(b"the fileis creted")
        else:
            self.send_response('404')

def run(server=HTTPServer,clas=Get,port=8000):
    address=('',8000)
    start=server(address,clas)
    print(f'server is started{port}')
    start.serve_forever()

if __name__ == "__main__":
    run()
    
