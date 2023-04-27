

# import python API library
import requests
import sys

# Given a GitHub organization id, retrieve all information about the organization. Return the information as a Python dictionary.
# Given a GitHub organization id, retrieve a list of all of the members of the organization. Return the list of members as a Python list of strings, where each string contains the member’s   (i.e., GitHub username) attribute.
# Given a GitHub organization id, return a list of repositories controlled by the organization. Return the list f repositories as a Python list of strings, where each string contains the repository   attribute.


def menu1(url):
    '''
        Given a GitHub organization id, retrieve all information about the organization.
    '''
    # Type hints
    url:str
    org:str
    response:bool
    CustomUrl:str

    org = input("Enter organization ID: ")
    CustomUrl = url + org
    # use git api to send a request
    response = requests.get(url=CustomUrl)
    print("Status code: " , response.status_code)
    # Retrun server response into python dict
    print(response.json())


def menu2(url):
    '''
        Given a GitHub organization id, retrieve a list of all of the members of the organization.
    '''

    # Type Hints
    memberList:list
    org:str
    CustomUrl:str
    response:bool


    memberList = []
    org = input("Enter organization ID: ")
    CustomUrl = url + org
    response = requests.get(url=CustomUrl)
    print("Status code: " , response.status_code)
    # Retrun server response into python dict
    returnData = response.json()
    # Create i an dict iterator; i (key)
    for i in returnData:
        # Iterate through dict keys and find a match
        if(i == "members_url"):
            # Add dict(returnData) value of key(i) to list(memberList)
            memberList.append(returnData[i])
    print(memberList)
 
def menu3(url):
    '''
        Given a GitHub organization id, return a list of repositories controlled by the organization
    '''

    # Type Hints
    repoList:list
    org:str
    CustomUrl:str
    response:bool

    repoList = []
    org = input("Enter organization ID: ")
    CustomUrl = url + org
    response = requests.get(url=CustomUrl)
    print("Status code: " , response.status_code)
    # Retrun server response into python dict
    returnData = response.json()
    # Create i an dict iterator; i (key)  
    for i in returnData:
        if(i == "name"):
            repoList.append(returnData[i])
    print(repoList)

def main():
    #Create menu
    url ="https://api.github.com/orgs/"
    print("1. Retrieve all information about the requested organization\n2. Retrieve a list of all of the members of the organization\n3. return a list of repositories controlled by the organization ")
    i = input("Enter selection: ")
    if(i == "1"):
        menu1(url)
    if(i=="2"):
        menu2(url)
    if(i=="3"):
        menu3(url)

if __name__ == "__main__":
    main()