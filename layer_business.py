from layer_database import User, collection_user


def create_user(**kwargs):
    user_name = kwargs['name']
    user_username = kwargs['username']
    user_email = kwargs['email']
    user_password = kwargs['password']
    
    try:
        my_user = User()
        my_user.email = user_email
        my_user.name = user_name
        my_user.username = user_username
        my_user.password = user_password

        collection_user.insert_one(my_user.__dict__) # insert dict

    except Exception as e:
        print(e)
        return False

    return True

def get_all_users():

    all_users = collection_user.find({}) # all users

    return all_users

def get_user_or_none(username):

    user = collection_user.find_one({'username': username})

    return user
