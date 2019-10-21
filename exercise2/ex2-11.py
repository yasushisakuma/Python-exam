import socket
print("ローカルipアドレスを取得します.")
host = socket.gethostname()#ホストを取得
ip = socket.gethostbyname(host)#ipアドレスを取得
print(ip) 