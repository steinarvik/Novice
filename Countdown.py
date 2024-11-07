import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

# Ask the user for the countdown time in seconds
time_in_seconds = int(input("Enter the time in seconds: "))
countdown_timer(time_in_seconds)