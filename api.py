#this is the priogram related to accseing the file for chrom using the http 
from http.server import BaseHTTPRequestHandler,HTTPServer
import pandas as pd
import hardcorevalues as static
from helperfunction import Response as help
import json
import logging
def read(filename):
    try:
        with open(filename,'r')as file:
            data=file.read()
        return data
    except FileNotFoundError:
        return None
#this class handel all the http requests
class Get(BaseHTTPRequestHandler):   
    def do_GET(self):
        if self.path==static.Get_json:
            repose=json.dumps(read(static.jsonfile))

            #the helper function are called
            help.response(self,repose)
        elif self.path==static.Get_excel:
            try:
                response=pd.read_excel(static.excelfile)
                responses = response.to_json(orient='records')
                #the helper function are called
                help.response(self,responses)
            except FileNotFoundError:
                self.send_response(static.error_code)
                self.end_headers()
                self.wfile.write(json.dumps(static.error_message).encode())
            except pd.errors.EmptyDataError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps("file is empty".encode()))
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps("the exception is {e}".encode()))
        else:
            self.send_response(static.error_code)
            self.end_headers()
            self.wfile.write(json.dumps(static.error_message).encode())
    def do_POST(self):
        if self.path == static.Post_json:
            length = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(length)
            try:
                datamain = json.loads(data.decode('utf-8'))
                datafinal=json.dumps(datamain)
                logging.basicConfig(filename="log.log",filemode='w',level=logging.info)
                logging.info('the message revered')
                with open(static.jsonfile, 'w') as f:
                    f.write(datafinal)
                message=json.dumps(static.success_message)
                #the helper function are called
                logging.basicConfig(filename="log.log",filemode='w',level=logging.info)
                logging.info('the message revered')
                help.response(self,message)
            except json.JSONDecodeError:
                self.send_response(static.error_code)
                self.end_headers()
                self.wfile.write(json.dumps(static.error_message).encode())
            except Exception as e:
                self.send_response(500,'the excetion is{e}')
                self.end_headers()
                self.wfile.write(json.dumps("the exception is {e}".encode()))
        elif self.path==static.Post_excel:
            try:
                contant=int(self.headers.get('Content-Length',0))
                data=self.rfile.read(contant)
                excel=json.loads(data)
                df=pd.DataFrame(excel)
                #the excel file is update
                with pd.ExcelWriter(static.excelfile, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                    df.to_excel(writer, sheet_name='Sheet1', index=False,header=False, startrow=writer.sheets['Sheet1'].max_row)
                massage=json.dumps("the massage get sucesfully")
                #the helper function are called
                help.response(message)
            except json.JSONDecodeError:
                self.send_response(404,"FileNotFoundError")
                self.end_headers()
                self.wfile.write(json.dumps("there is problem in the json file youn send".encode()))
            except FileNotFoundError:
                self.send_response(404,'file not found')
                self.end_headers()
                self.wfile.write(json.dumps("file not found".encode()))
            except Exception as e:
                self.send_response(500,'the excetion is{e}',)
                self.end_headers() 
                self.wfile.write(json.dumps("the exception is {e}".encode()))              
        else:
            self.send_response(404)
            self.end_headers()

def run(server=HTTPServer,clas=Get,port=8000):
    address=('',8000)
    start=server(address,clas)
    print(f'server is started{port}')
    start.serve_forever()

if __name__ == "__main__":
    run()
    
