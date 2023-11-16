import threading

def test_01(msg):
    print("test01: " , msg)

def test_02(msg):
    print("test02: ", msg)

msg = "In THREAD Something"
t1 = threading.Thread(target=test_01, args=[msg])
msg = "In THREAD Anything"
t2 = threading.Thread(target=test_02, args=[msg])

t1.start()
t2.start()

# t1.join()
# t2.join()