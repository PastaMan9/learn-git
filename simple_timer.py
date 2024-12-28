import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Время вышло!")

if __name__ == "__main__":
    try:
        t = int(input("Введите время в секундах: "))
        countdown_timer(t)
    except ValueError:
        print("Пожалуйста, введите целое число.")
