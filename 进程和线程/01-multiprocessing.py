from multiprocessing import Process
import time, os

def run_proc(name):
	for i in range(10):
		print("Run child process %s(%s)..."%(name, os.getpid()))
		time.sleep(1)
if __name__ == '__main__':
	print("Parent process %s..."%os.getpid())
	p = Process(target=run_proc, args=('test',))
	print("Child process will start...")
	p.start()
	p.join()
	print("Child process end..")