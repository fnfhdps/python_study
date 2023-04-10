import threading

def on_timer(count):
    count += 1
    print(count)

##    timer = threading.Timer(1, on_timer, args=[count])
##    timer.start()
##
##    if count == 10:
##        print('Canceling timer..')
##        timer.cancel()

    if count < 1000:
        timer = threading.Timer(300, on_timer, args=[count])
        timer.start()

print('Starting timer..')
on_timer(0)
print('Canceling timer..')
