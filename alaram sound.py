import time
import datetime
import winsound

def set_alarm(hour, minute):
    now = datetime.datetime.now()
    alarm_time = datetime.datetime(now.year, now.month, now.day, hour, minute)

    if alarm_time < now:
        alarm_time += datetime.timedelta(days=1)

    seconds_until_alarm = (alarm_time - now).total_seconds()
    print(f"Alarm set for {alarm_time.strftime('%I:%M %p')}. Waiting...")

    time.sleep(seconds_until_alarm)

    print("Alarm ringing!")
    winsound.Beep(1000, 1000)  # frequency (Hz), duration (ms)

# Example usage: Set alarm for 1:42 PM
set_alarm(13, 42)
