'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

# Use a method to attempt to extract the zip file with a given password
#def attempt_extract(zf_handle, password):


def main():
    print("[+] Beginning bruteforce ")
    count_line = 0
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            # Write your logic here...
            # Iterate through password entries in rockyou.txt
            for line in f:
                for word in line.split():
                    try:
                        count_line += 1
                        zf.extractall(pwd=word)
                        print("Password found at line", count_line)
                        print("Password is", word.decode())
                        return True
                    except:
                        continue
        return False

            # Attempt to extract the zip file using each password

            # Handle correct password extract versus incorrect password attempt)

    #print("[+] Password not found in list")

if __name__ == "__main__":
    main()