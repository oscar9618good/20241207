import time

your_time = int(input("Enter the time in seconds: "))

# 方法1:
for x in range(your_time, 0, -1):
    seconds = x % 60
    minutes = x // 60 % 60
    print(f"{minutes:02d}:{seconds:02d}")    # \r: carriage return
    time.sleep(1)
print("Time is up!")


# 方法2:
# def countdown_timer(seconds):
# 	while seconds:
# 		mins, secs = divmod(seconds, 60)
# 		timer = '{:02d}:{:02d}'.format(mins, secs)
# 		print(timer, end="\r")       # \r: carriage return
# 		time.sleep(1)
# 		seconds -= 1
# 	print('Time is up!')

# countdown_timer(your_time)