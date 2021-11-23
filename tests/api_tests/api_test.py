import requests


url = "http://192.168.1.240:8080"
route = {
    'token': '/api/auth/token',
    'users': '/api/users'
}

class ApiTest:

    PASS_respond = '[200]'
    FAIL_respond = ['[400]', '[401]', '[404]', '[406]', '[500]']
    CREATE_respond = '[201]'

    def set_up(self):
        """This is a function to print out the introduction of this test suite."""
        print('This is API testing for:\n'
              '1. Register new users\n'
              '2. Review users registered in system\n'
              '3. If authenticated I can get personal information of users\n'
              '4. If authenticated I can update personal information of users')
        print('*'*100)

    def tear_down(self):
        """This is a function to print out the tear down status of this test suite."""
        print('*'*100)
        print('The API test is completed.')

    def get_token(self):
        """Get token method will retrieve the generated token
        that will be used for authorization.
        """
        user_data = ('xiaobixu', 'thisISaPassword')
        try:
            response = requests.get(url + route['token'], auth=user_data)
            resp_text = response.json()
            return resp_text['token']
        except:
            print('Oops, something wrong happened!')

    def set_header(self):
        """Set header method will return a header with token
        that will be passed in request
        """
        token = self.get_token()
        headers = {
            'Content-Type': 'application/json',
            'Token': token
        }
        return headers

    def get_users(self):
        """Get_users methods will fetch all the existing users for review"""
        print('Retrieving all the registered users...')
        try:
            response = requests.get(url + route['users'], headers=self.set_header())
            result_file = open('all_users_json.txt', 'w')
            resp_text = response.json()
            result_file.write(str(resp_text))
            if self.PASS_respond in str(response):
                print('The respond code is {}: {}'.format(self.PASS_respond, resp_text['status']))
            else:
                for i in self.FAIL_respond:
                    if i in str(response):
                        print('Response code is {}: {}'.format(i, resp_text['status']))
            return response
        except:
            print('Oops, something wrong happened')
            return response

    def get_specific_user(self, username):
        """Get specific user method will return the information of a given user"""
        print('Getting user information of {}...'.format(username))
        try:
            response = requests.get(url + route['users'] + '/' + username, headers=self.set_header())
            resp_text = response.json()
            if self.PASS_respond in str(response):
                print('The respond code is {}: {}'.format(self.PASS_respond, resp_text['status']))
                print('The user information of {} is {}'.format(username, resp_text['payload']))
            else:
                for i in self.FAIL_respond:
                    if i in str(response):
                        print('Response code is {}: {}'.format(response, resp_text['message']))
                        print(resp_text['status'])
            return response
        except:
            print('Oops, something wrong happened')
            return response

    def register_users(self, users):
        """Register user method will register a list of users"""
        for user in users:
            print('Registering {} to system:'.format(user['username']))
            try:
                response = requests.post(url + route['users'], headers=self.set_header(), json=user)
                resp_text = response.json()
                if self.CREATE_respond in str(response):
                    print('The respond code is {}: User {} is {} successfully.'.format(self.CREATE_respond, user['username'],
                                                                         resp_text['message']))
                else:
                    for i in self.FAIL_respond:
                        if i in str(response):
                            print('Response code is {}: {}. This user has been registered successfully before.'
                                  .format(i, resp_text['message']))
            except:
                print('Oops, something wrong happened. User could not be registered')

    def update_user(self, username, payload):
        """Update user method will update personal information of a given user"""
        print('Updating user information for {}'.format(username))
        try:
            response = requests.put(url + route['users'] + '/' + username, headers=self.set_header(), json=payload)
            resp_text = response.json()
            if self.CREATE_respond in str(response):
                print('The response code is {}: {}'.format(self.CREATE_respond, resp_text['message']))
            else:
                for i in self.FAIL_respond:
                    if i in str(response):
                        print('The response code is {}: {}'.format(i, resp_text['message']))
            return response
        except:
            print('Oops, something wrong happened.')
            return response


    def delete_all_user(self):
        """Delete user method will delete all users"""
        try:
            response = requests.delete(url + route['users'], headers=self.set_header())
            print(response.json())
            return response
        except:
            print('Oops, something wrong happened.')
            return response

    def review_user(self, user_register, all_users) -> None:
        print('Reviewing the registered users in the system...')
        for user in user_register:
            if user['username'] in all_users['payload']:
                print('User {} has been registered in system successfully.'.format(user['username']))
            else:
                print('User {} is not registered in the system.'.format(user['username']))

    def verify_user_updated(self, payload_1, payload_2):
        if payload_1 == payload_2:
            return 1
        else:
            return 0

