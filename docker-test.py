import time
from datetime import datetime
import socket 
import secrets
import string


# Get the current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Get the hostname
hostname = socket.gethostname()

# Log the start time
print(f"Start Time - {current_datetime}")
print (f"Running on - Hostname: {hostname}")

for x in range(1,10):
   print("Running test to get sample value")
   length = 10  # You can adjust this to your desired length
   random_string = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))
   print("Sample-Value:", random_string)
   time.sleep(10)

# Get the end time
end_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Log the end time
print(f"End Time - {end_datetime}")
