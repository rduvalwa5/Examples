"""
python enviroment code
https://docs.python.org/3/library/platform.html?highlight=platform#module-platform
"""

import platform

print("system ",platform.system())
print("machine ",platform.machine())
print("processor ",platform.processor())
print("uname node ", platform.uname().node)
print("python version ", platform.python_version())
print("python implementation ", platform.python_implementation())
print("python release ", platform.release())
print("python build ", platform.python_build())
print("release alias ", platform.system_alias(platform.release(),platform.release(),platform.version()))
print("Mac version ", platform.mac_ver())