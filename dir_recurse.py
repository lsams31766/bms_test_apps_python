#dir_recurse.py
# show files and dirs recursively

import os 

#root = "/idm/ldap/code/test"
root = "/idm/ldap/code/je_rules_query_app"
ignore_dirs = ['venv', 'vscode', 'backups', 'logs', 'pycache']

def ignore_path(path):
    for i in ignore_dirs:
        if i in path:
            return True
    return False

def list_all(path):
    files = os.listdir(path)
    dirs_found = []
    if ignore_path(path):
        return
    for file in files:
        low_path = os.path.join(path,file)
        if os.path.isdir(low_path):
            dirs_found.append(low_path)
        else:
            print("\t",file)
    for d in dirs_found:
        if not ignore_path(d):
            print(d)
            list_all(d)
    dirs_found = []
    #list_all(d[0])
    #    list_all(d)

print(root)
list_all(root)