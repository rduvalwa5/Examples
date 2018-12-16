"""
get environemnt variables
"""

def get_os_env():
    """
        Get local environment and return it
    """
    env = os.environ
    print("env \n" , env)
    return env

if __name__ == "__main__":

    print(get_os_env)

