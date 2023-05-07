# Web_Bots_Detection
Steps to implement the project:
1.	Please download the entire source code from the GitHub link provided above.
2.	Keep all the files in the same directory.
3.	Run these files in the following order:
    a. To set up the server:
        i.	app.py
    b. Log generation:
        i. For web scraper generated logs: web_scraper_no_time.py for no time delays, web_scraper_constant_time.py for constant time delay and web_scraper_random_time.py for random time delay between HTTP requests (make sure to change the file name in app.py).
        ii.	For manual/human logs: http://localhost:8000
    c. To classify the generated logs:
        i. bot_detector_no_time.py, bot_detector_constant_time.py, and bot_detector_random_time.py for each time delay type.
        
       
Required Libraries:
os
flask
logging
datetime
bs4 (beautifulsoup)
requests
random
time
re
statistics
matplotlib


Setting everything up takes about 5 minutes (assuming you have all the required libraries installed).

Running the scripts takes few seconds with provided threshold value in the file. To get the results using different threshold value, just change the threshold value in the file and rerun the script.
