
"""AMAITHI'S HABIT TRACKER USING PIXELA API - FOLLOW THE INSTRUCTIONS TO GET STARTED WITH THIS CODE SNIPPET"""


from datetime import datetime
import requests
import os
import time

#------------------- UPDATE THE DETAILES BELOW------------

USERNAME = ""
TOKEN = ""
GRAPH_ID = ""
HABIT_NAME = ""
GRAPH_UNIT = "Minute"

#-------------------------Don't Change the Code Below------------
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

HEADERS = {
    "X-USER-TOKEN": TOKEN
}

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_CONFIG = {
        "id": GRAPH_ID,
        "name": HABIT_NAME,
        "unit": GRAPH_UNIT,
        "type": "float",
        "color": "ajisai",
        "timezone": "Singapore"
    }
TODAY = datetime.now().strftime("%Y%m%d")

# ------------------- CREATE NEW USER ------------------- #

def new_user():

    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    pixela_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(pixela_response.text)

# ------------------- CREATE NEW GRAPH ------------------- #

def new_graph():
    
    graph_response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=HEADERS)
    print(graph_response.text)

# ------------------- DELETE GRAPH ------------------- #

def delete_graph():
    
    delete_graph_response = requests.delete(
        url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}",
        json=GRAPH_CONFIG,
        headers=HEADERS
    )
    print(delete_graph_response.text)

# ------------------- POST A PIXEL ------------------- #

def post_a_pixel():

    POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

    quantity = input("How many Minutes did you perform Coding today?\n")

    POST_PIXEL_CONFIG = {
        "date": TODAY,
        "quantity": quantity,
    }

    post_pixel_response = requests.post(
        url=POST_PIXEL_ENDPOINT,
        json=POST_PIXEL_CONFIG,
        headers=HEADERS
    )
    print(post_pixel_response.text)

# ------------------- UPDATE A PIXEL ------------------- #

def update_pixel():
    
    date = input("Input date (YYYYMMDD):\n")

    UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

    quantity = input(f"How many Minutes did you perform Coding on {date}?\n")

    UPDATE_PIXEL_CONFIG = {
        "quantity": quantity,
    }

    update_pixel_response = requests.put(
        url=UPDATE_PIXEL_ENDPOINT,
        json=UPDATE_PIXEL_CONFIG,
        headers=HEADERS
    )
    print(update_pixel_response.text)

# ------------------- DELETE A PIXEL ------------------- #

def del_pixel():
    
    delete_date = input("Enter date to delete:\n(yyyyMMdd)\n")
    DELETE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{delete_date}"

    delete_pixel_response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=HEADERS)
    print(delete_pixel_response.text)
    
    
#-----------------------    VIEW THE GRAPH-------------

def view_graph():
    
    link = f"{GRAPH_ENDPOINT}/{GRAPH_ID}.html"
    
    print(f"\n Open the Below Link in a Web Browser To View the Graph..\m\n {link}")
    
#------------------------------------------------------------
    
if __name__ == "__main__":
   
    while True: 
        
        time.sleep(2)
        os.system('cls||clear')
        
        choice = int(input("""
                           WELCOME TO AMAITHI'S HABIT TRACKER POWERED BY PIXELA \n
                Would you like to:
                    1 - Post a pixel
                    2 - Update a pixel
                    3 - Delete a pixel \n
                    4 - Create a New account
                    5 - Create a New Graph
                    6 - View The Graph
                    7 - Delete a Graph \n
                    0 - To Exit
                    
                    Enter the Number Pointed to the Task You wanna Perform \n\t
                    """))
        
        if choice == 1:
            post_a_pixel()
        elif choice ==2:
            update_pixel()
        elif choice == 3:
            del_pixel()
        elif choice == 4:
            new_user()
        elif choice == 5:
            new_graph()
        elif choice == 6:
            view_graph()
        elif choice == 7:
            delete_graph()
        elif choice == 0:
            break
        else:
            print("kindly choose Between 0 & 7")
        
        
