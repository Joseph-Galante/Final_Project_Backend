# =================== SETUP =================== #

# package imports
import models

# =================== METHODS =================== #

class Product_Utils ():
    
    # verify user as product lister
    def verify_lister (product, user):
        # check if user owns product
        is_owner = product.user.id == user.id

        return is_owner