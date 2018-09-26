from socketserver import *


class Server(ThreadingMixIn, UDPServer):
# class Server(ForkingTCPServer):
# class Server(ThreadingMixIn, TCPServer):
    pass


class Handler(DatagramRequestHandler):
    def hanle(self):
        while True:
            data = self.rfile.readline(1024)
            print(self.client_address)
            if not data:
                break
            print(data.decode())
            self.wfile.write(b'receive')
        


if __name__ == "__main__":
    server_addr = ('0.0.0.0', 8888)

    #　创建服务器对象
    server = Server(server_addr, Handler)
    #　启动服务器
    server.serve_forever()



















