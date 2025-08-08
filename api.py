#this is the priogram related to accseing the file for chrom using the http 
from http.server import BaseHTTPRequestHandler,HTTPServer
import pandas as pd
import json
def read(filename):
    try:
        with open(filename,'r')as file:
            data=file.read()
        return data
    except FileNotFoundError:
        return None

class Get(BaseHTTPRequestHandler): 
    def res(self,data):
        try:
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(data.encode())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps("the exception is {e}".encode()))    
    def do_GET(self):
        if self.path=='/json':
            repose=json.dumps(read('jsonfile.json'))
            
            self.res(repose)
        if self.path=='/excel':
            try:
                response=pd.read_excel('ai.xlsx')
                responses = response.to_json(orient='records')
                self.res(responses)
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(json.dumps("file not found".encode()))
            except pd.errors.EmptyDataError:
                self.send_response(400)
                self.send_headers()
                self.wfile.write(json.dumps("file is empty".encode()))
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps("the exception is {e}".encode()))
        else:
            self.send_response(404,'file not found')
    def do_POST(self):
        if self.path == '/json/creat':
            length = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(length)
            try:
                datamain = json.loads(data.decode('utf-8'))
                datafinal=json.dumps(datamain)
                with open('jsonfile.json', 'a') as f:
                    f.write(datafinal)
                message=json.dumps("the message get sucees fully")
                self.res(message)
            except json.JSONDecodeError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(json.dumps("there is problem in the json file youn send".encode()))
            except Exception as e:
                self.send_response(500,'the excetion is{e}')
                self.end_headers()
                self.wfile.write(json.dumps("the exception is {e}".encode()))
        elif self.path=='/excel/create':
            try:
                contant=int(self.headers.get('Content-Length',0))
                data=self.rfile.read(contant)
                excel=json.loads(data)
                df=pd.DataFrame(excel)
                with pd.ExcelWriter('ai.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                    df.to_excel(writer, sheet_name='Sheet1', index=False,header=False, startrow=writer.sheets['Sheet1'].max_row)
                massage=json.dumps("the massage get sucesfully")
                self.res(message)
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
    
