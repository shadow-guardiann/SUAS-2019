# GET IMAGES AND THEIR LAT,LON,ALT,HEADING FROM THE UAV

# Run this on the client machine/laptop

import socket
import pickle
import numpy as np
from PIL import Image
import time, json

HOST = '192.168.0.100'
PORT = 50007
count = 0
print('IMAGING CLIENT READY')

while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(100)
	pdata = b''
	conn, addr = s.accept()
	print ('Connected by', addr)
	while 1:
		data = conn.recv(40960000)
		if not data:
			break
		pdata+= data

	deserialized = pickle.loads(pdata)
	print(deserialized[1])
	im = Image.fromarray(deserialized[0])
	print('SAVING IMAGE ',count)
	im.save('odlcs/'+str(count)+'.jpg')
	with open('odlcs/'+str(count)+'.json','wb') as outfile:
		json.dump(deserialized[1],outfile)
	count += 1
	conn.close()
	s.close()
	PORT += 1