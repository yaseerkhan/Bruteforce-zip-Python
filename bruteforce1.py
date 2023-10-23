'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile


# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        with ZipFile('enc.zip', 'r') as zip_file:
            zip_file.extractall(pwd=password)
            return True # password correct
    except Exception as e:
        return False


def main():
    print("[+] Beginning bruteforce ")
    count_line = 0
    with open('rockyou.txt', 'rb') as wordlist:
        for line_number, password in enumerate(wordlist, start=1):
            password = password.strip()

            if attempt_extract('enc.zip', password):
                print(f'Attempt {line_number}: {password}')
                print(f'Success! Password found: {password}')
                print(f'Line in wordlist: {line_number}')

                break
            else:
                print(f'Attempt {line_number}: {password}')

        else:
            print('Password not found in the wordlist.')


if __name__ == "__main__":
    main()
