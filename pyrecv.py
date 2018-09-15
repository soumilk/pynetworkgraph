#!/usr/bin/env python2

import  socket
import matplotlib.pyplot  as  plt
#  we are looking for UDP (user datagram protocol )
#              ip_version4,         UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# defining ip and port below 
#ip="no need to define computer will detect automatically"
port=7890
#  binding ip and port with bind function that takes input as tuple
s.bind(("",port))

# defining  empty dictionary
x={}
for  i in range(5) :
#  now receiving data
	fulldata=s.recvfrom(100)
#spliting sentence into list of individual words
	data=fulldata[0].split()
	#creating new keys(default value 1) or updating previous keys(adding 1)
	for i in data:
		x[i]=x.get(i, 0) + 1
	print "data received:",data
y=x.items()
# unpacking a list of pairs into two tuples
a,b=zip(*y)
#labeling and creating graph by above two tuples
plt.xlabel("messages received")
plt.ylabel("number of occurance")
plt.scatter(a,b,label="dot plot",s=200)
plt.plot(a,b,label="line plot")
plt.bar(a,b,label="bar plot",color='green')
plt.legend()
plt.grid()
plt.show()
s.close()
