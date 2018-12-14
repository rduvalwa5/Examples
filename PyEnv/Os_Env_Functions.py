'''
Created on Feb 15, 2017

@author: rduvalwa2
'''
import os
import subprocess

print()


def get_os_env():
    """
        Get local environment and return it
    """
    env = os.environ
    print("env \n" , env)
    return env

def get_env_item(item): 
    print(os.environ[item])
    return os.environ[item] 

def os_get_variable(var):
    return os.getenv(var)
 
def put_env_var_shell():
    os.system("export JAVA='/usr/bin/java'")
    subprocess.check_call(["env"])
  
      
def get_all_tags():
    tags = []
    for tag in os.environ:
        tags.append(tag)
    return tags
 
def listEnvVar():
    envVarVal = []    
    for tag in get_all_tags():
        envVarVal.append((tag,os.environ[tag]))
    return envVarVal
    
if __name__ == "__main__":
    var = 'JAVA'
    val = '/usr/bin/java'
    put_env_var_shell()
    print(os.name)
    
    print(get_os_env())
    print(get_env_item('HOME')) 
    theseTags = get_all_tags()
    envTagValues = listEnvVar()
    for item in envTagValues:
        print(item)    
    for item in envTagValues:
        if item[0] == "HOME":
            print("Home is ", item[1])
 
    put_env_var_shell()