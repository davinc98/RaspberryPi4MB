import time 
tiempo = 0.1

# for i in range(10):
#     print(i)
#     time.sleep(tiempo)
#     print(time.time())
    
t1 = time.time()
t2 = time.time()

while True:
    if(t2-t1)<1:
        t2 = time.time()
    else:
        t1 = time.time()   
        print("Ya paso un segundo")         