import requests
from requests.exceptions import HTTPError

def jsontest (url='https://httpbin.org/get'):
    try:
        print(url)
        response = requests.get(url)
        #response.raise_for_status()
        # access JSOn content
        jsonResponse = response.json()
        print("Entire JSON response")
        print(jsonResponse)

        print("JSON response[step_status]")
        print(jsonResponse['step_status'])

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')



def menu():
    print("MAIN MENU")
    print("-----------------")
    print("1. Print pay check")
    print("2. Change benefits")
    print("3. Exit")

    choice = input("Choose menu option (1-3): ")
    while choice not in ['1', '2', '3']:
        choice = input("Invalid choice.  Choose menu option (1-3): ")
    return int(choice)


menu_chosen = True
choice = menu()
print("You chose menu option", choice)
if choice == 1 :
    jsontest(url='http://localhost:8000/')