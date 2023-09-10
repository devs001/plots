import json
def dumping(stri,repos):
    with open(stri,'w') as file:
        json.dump(repos,file)