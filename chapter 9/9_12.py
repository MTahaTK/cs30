# 9-12
print("\n9-12")

from admin_et_privileges import *

admin = Admin('bub', 'wakker')
admin.describe_user()

admin.privileges.privileges = [
    "to wakk bubs"
]

admin.privileges.show_privileges()
