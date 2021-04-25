# Write you email parser code here ...

# Import all required modules
import re


class EmailParser:
    # regex pattern that validate email
    pattern = r'^([a-zA-Z])([a-zA-Z0-9+]+)@([a-zA-Z])([a-zA-Z0-9]+)\.com$'
    keys = ['username', 'domain']

    @classmethod
    def parse(cls, email):
        ''' parse email and return a dictionary of username and domain if valid and return None otherwise'''

        if not type(email) is str:
            return None

        pattern = re.compile(cls.pattern)

        search_email = pattern.search(email)

        if search_email:
            grouped_email = search_email.group() # 'ola@gmail.com'
            splittee_email = grouped_email.split('@') # [ola, gmail.com]

            return cls.convert_to_dict(cls.keys, splittee_email)

        return search_email

        # Add implementation here ...
    def convert_to_dict(first_list, second_list):
        '''
          Takes in two lists as params and return them as a dictionary.

          Parameters:
            first_list (list []): first_list to serve as keys  
            second_list (list []): second_list to serve as values

          Returns:
            convert_to_dict(list, list): return a dictionary of two lists 
        '''
        return dict(zip(first_list, second_list))


# -----------------------------------------------------
# EXPERIMENTS
# -----------------------------------------------------
# Ensure to clear out codes below when you are done
# with experimentations
# -----------------------------------------------------
print('\n>>>> Experiment - EmailParser\n')

# result = EmailParser.parse('name@gmail.com')
# print(result)
print('')
