from api_test import *


# Define funtion to headlines for test cases
def print_tc_title(tc_str):
    print('='*20, tc_str, '='*20)

# Create an object of class ApiTest and use methods from this class
test = ApiTest()

# Set up tests
test.set_up()

# New user data for registration
new_users = [
    {'username': 'user_1', 'password': '333333', 'firstname': 'Jenny', 'lastname': 'Makinen', 'phone': '0407463737'},
    {'username': 'user_2', 'password': '444444', 'firstname': 'Sami', 'lastname': 'Great', 'phone': '0509999999'},
    ]
# The user information that will update the previous one
payload_to_update = {
    'firstname': 'Jenni',
    'lastname': 'Alto',
    'phone': '040777777'
}
# The specified user name
username = 'user_1'

# TC1: Register new users
print_tc_title('TC-1 Register new users')
test.register_users(new_users)

# TC2: Review users registered in system
print_tc_title('TC-2 Review users registered in system')
response_review = test.get_users()
response_review_text = response_review.json()
test.review_user(new_users, response_review_text)

# TC3: If authenticated I can get personal information of users
print_tc_title('TC-3 If authenticated I can get personal information of users')
response_get_user = test.get_specific_user(username)

# TC4: If authenticated I can update personal information of users
print_tc_title('TC-4 If authenticated I can update personal information of users')
# The updated user information
payload_to_update = {
    'firstname': 'Jenni',
    'lastname': 'Alto',
    'phone': '040777777'
}
response_put = test.update_user(username, payload_to_update)
# Retrive the same user after its information got updated
user_after_update = test.get_specific_user(username)
payload_after_update = user_after_update.json()['payload']
# Verify if the update is applied to system
check_if_updated = test.verify_user_updated(payload_after_update, payload_to_update)
if check_if_updated:
    print("Update is successful")
else:
    print("Update is failed")


# Test tear down
test.tear_down()




