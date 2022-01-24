import time
from threading import Timer


def display_msg(msg):  # function to be executed by timer
    print(msg+' '+time.strftime('%H:%M:%S'))


def run_once():
    display_msg('Timer started')
    t = Timer(5.0, display_msg, args=('Timer expired',))

    t.start()
    time.sleep(10)
    t.cancel()
    display_msg('Timer stopped')


class Repeater(Timer):
    def run(self):
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)
        print('Timer stopped')


repeat = Repeater(2, display_msg, args=(
    'Timer counting',), kwargs={})

print('Timer started counting')
repeat.start()
time.sleep(10)
repeat.cancel()


# if __name__ == '__main__':
#     run()
