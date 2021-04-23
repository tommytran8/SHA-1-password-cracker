import hashlib
from unittest import main

def crack_sha1_hash(hash, use_salts=False):
    with open("top-10000-passwords.txt", "r") as file, open("known-salts.txt", "r") as salts:
        file1 = file.readlines()
        salts1 = salts.readlines()
        salts.close()
        file.close()
        if use_salts:
            for password in file1:
                for salt in salts1:
                    # converts password into a hash with some known salts.
                    if (hashlib.sha1(str.encode(salt.strip() + password.strip())).hexdigest() == hash):
                        # read in lines contain a trailing character '\n', so strip removes it
                        return password.strip()
                    elif (hashlib.sha1(str.encode(password.strip() + salt.strip())).hexdigest() == hash):
                        # read in lines contain a trailing character '\n', so strip removes it
                        return password.strip()
        else:
            for password in file1:
                # converts password into a hash.
                if (hashlib.sha1(str.encode(password.strip())).hexdigest() == hash):
                    # read in lines contain a trailing character '\n', so strip removes it
                    return password.strip()
        return "PASSWORD NOT IN DATABASE"
    
if __name__ == "__main__":
    print( crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", True))
