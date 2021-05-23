# =================== SETUP =================== #

# package imports
import models

# =================== METHODS =================== #

class Cart_Utils ():
    
    # verify user as product lister
    def verify_owner (item, user):
        # check if user owns product
        is_owner = item.user.id == user.id

        return is_owner