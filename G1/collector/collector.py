from Shell import Shell
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from ontrafficwatch import OnTrafficWatch
import subprocess


def collecting_traffic(name):
    print(str(name) + ' Thread starts')
    shell = Shell()
    shell.execute("echo \"abcd\" | sudo -S stop my")
    shell.execute("echo \"abcd\" | sudo -S tcpdump -i any -v -G 20 not arp and not src 10.1.0.65 and not src "
                  "127.0.0.1 and not dst 10.1.0.65 and not dst 127.0.0.1 -w data-%S.pcap")

def allowed_traffic_generate(name):
    print(str(name) + ' Thread starts')
    shell = Shell()
    while True:
        shell.execute("echo \"abcd\" | sudo -S curl http://10.5.0.164:80")

        # TODO : FTP & Ping , Update other gateways


def __main():
    thread1 = threading.Thread(target=allowed_traffic_generate, args=('t1',))
    thread1.start()

    thread2 = threading.Thread(target=collecting_traffic, args=('t2',))
    thread2.start()

    watch = OnTrafficWatch()
    watch.run()


if __name__ == '__main__':
    __main()
