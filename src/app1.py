from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import threading
data = {'result': 'this is a test'}
host = ('0.0.0.0', 8888)
host2= ('0.0.0.0',8889)

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
       # self.wfile.write(json.dumps(data).encode())
        self.wfile.write(f"welcome from {self.server.server_port} \n".encode('utf-8'))
        print(f"port: {self.server.server_port} response")        
def SRRR(host):
    server = HTTPServer(host, Resquest)
    print(f"response from: {host[0]}:{host[1]}\n")
    server.serve_forever()   
if __name__ == '__main__':
    thread1=threading.Thread(target=SRRR,args=(host,))#args acquire tuples, target to the action you want
    thread2=threading.Thread(target=SRRR,args=(host2,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


