'''
    Author: Vidit Maheshwrai
    Date: 20170204 (YYYYMMDD)
    Copyright :

    Purpose: Utility function specific to inventoryManagement app

    History:

'''

# Description: To check for authentication of incoming data
# Input : authentication code
# Output : boolean true or false

def authentication(auth_code):
    if(auth_code == "Kamina"):
        return True
    else:
        return False
