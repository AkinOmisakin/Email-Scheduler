# Description: This is the main script that will run the send_emails.py script every day at 6:30am

import schedule
import time

def job():
    print("I'm working...")

if __name__ == "__main__":
    schedule.every().day.at("06:30").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)