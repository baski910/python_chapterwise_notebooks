fh = open('demo_2.jpg','rb')

oh = open('demo_bck.jpg','wb')

oh.write(fh.read())

fh.close()
oh.close()