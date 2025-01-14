"""Practice importing data"""
# 9-12 importing classes from modules

import user_privileges

user_admin1 = user_privileges.Admin('Tony', 'Stark', '39', 'male')

user_admin1.privileges.show_privileges()

# Or this works too
# from user_privileges import Admin
# user_admin1 = Admin('Tony', 'Stark', 39, 'male')
# user_admin1.privileges.show_privileges()
