import time
import os
import psutil

# Функция очистки жкрана
CLEAR = lambda: os.system('cls')

def main():
	"""

	Гравнвя Main функция
	"""

	# Задает размер экрана
	os.system("mode con cols=30 lines=7")
	# В бесконечном цикле считываем значенияиз ресурсов из системы и выводим их на экран
	while True:
		# Вызываем lmbda функцию для очистки экрана
		CLEAR()
		print(f"CPU     : {psutil.cpu_percent(interval=None)} %")
		print(f"Memory  : {psutil.virtual_memory()[2]} % | {round(psutil.virtual_memory()[3] / 1024 / 1024, 1)} MB")
		print(f"Swap M  : {psutil.swap_memory()[3]} % | {round(psutil.swap_memory()[1] / 1024 / 1024, 1)} MB")
		print(f"********** NETWORK **********")
		print(f"received: {round(psutil.net_io_counters(pernic=False, nowrap=True)[1] / 1024 / 1024, 1)} MB")
		print(f"send    : {round(psutil.net_io_counters(pernic=False, nowrap=True)[0] / 1024 / 1024, 1)} MB")
		time.sleep(0.5)


if __name__ == '__main__':
	main()
