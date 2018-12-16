"""
get local python environment variable
"""

import os

def get_os_env():
    """
        Get local environment and return it
    """
    env = os.environ
#    print("env \n" , env)
    return env

if __name__ == "__main__":
    en = get_os_env()
#    print(type(en))
#    print(en)
    for k in en:
        print(k,"=",en[k])
