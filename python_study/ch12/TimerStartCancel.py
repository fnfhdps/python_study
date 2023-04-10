import threading

count = 0

def on_timer():
    global count
    count += 1
    print(count)

    timer = threading.Timer(1, on_timer)
    timer.start()

    if count == 10:
        print('Canceling timer...')
        timer.cancel()
        
# 좀 더 간결한 방법
##    if count < 10:
##        timer = threading.Timer(1, on_timer)
##        timer.start()

print('Starting timer..')
on_timer()


