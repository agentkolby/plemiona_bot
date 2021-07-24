import csv
import os
import sys

FILE_PATH = os.path.join(sys.path[0], "utilities", "cookies.csv")
print(FILE_PATH)

def get_cookies():

    cookies_dict = {}
    
    with open(FILE_PATH) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
    
        for row in csv_reader:
            cookie_name = row[0]
            cookie_value = row[1]

            cookies_dict[cookie_name] = cookie_value
        
        csv_file.close()

    return cookies_dict


            


