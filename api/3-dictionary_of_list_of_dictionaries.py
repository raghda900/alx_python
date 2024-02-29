"""This module makes 2 api requests and 
uses the informatiom given to write it to a json file
"""

import json
import requests 

def get_info():
    dictionary={}
    empurl= f'https://jsonplaceholder.typicode.com/users'
    
    # get employee information
    res2 = requests.get(empurl)
    employeedata = res2.json()
    
    for employee in employeedata:
        USER_ID = employee['id']
        USERNAME = employee['username']
        todo_URL = f'https://jsonplaceholder.typicode.com/users/{USER_ID}/todos'
        
        res1 = requests.get(todo_URL)
        data1 = res1.json()
        tasks = []

        for i in range(len(data1)):
            """loop to add task status and title"""
            TASK_COMPLETED_STATUS = data1[i]['completed']
            TASK_TITLE = data1[i]['title']
            tasks.append({"task": TASK_TITLE, "completed": TASK_COMPLETED_STATUS, "username":USERNAME})
        
        dictionary[USER_ID] =tasks
    with open(f'todo_all_employees.json', 'w', newline='') as file:
        # write dictionary to json file
        json.dump(dictionary , file)

if __name__ == "__main__":
    get_info()