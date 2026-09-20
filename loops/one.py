attempts = 0
max_attempts = 5
wait_time = 1

import time

while attempts < 5:
    print("Attempts : ", attempts+1, "- Wait time : ", wait_time)
    n = input("Enter a number : ")
    time.sleep(wait_time)
    attempts+=1
    wait_time *= 2