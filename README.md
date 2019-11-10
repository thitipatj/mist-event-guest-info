# mist-event-guest-info
Sample script to get a full list of authorized guest, write to CSV file, and show a random guest's email address (with mask)
Please run event-query.py once, and run event-random.py at your own convenience.
Compatible with Python2.7

The python file need configuration file to run. Please create "config.ini" with mandatory information. 
> Configuration file not included in this project.

Here's the component of the project:

## Configuration File Example:

```
[Global_Var]
ORG = 118cbf2b-xxxx-xxxx-xxxx-beee9a0220aa
SITE = 61982c4a-xxxx-xxxx-xxxx-bb281afa1620
TOKEN = biLXLTNTzG72G............TooxupUl4JkdnGVJ
```
## event-query.py
The script will connect to Mist cloud and get the full list of authorized guest (from Mist's built-in guest portal), then write to the CSV file with column "Name" and "Email"

## event-random.py
The script will read the content in the CSV file (created by event-query.py), then random the lucky email, show up on the screen.
This script can be run multiple time, in case to random more lucky email.
