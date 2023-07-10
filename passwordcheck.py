#===========Password Checker using Password API===========

import requests
import hashlib
import sys

def request_api_data(quary_character):
    url = 'https://api.pwnedpasswords.com/range/' + quary_character
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error Fetching: {response.status_code}, Check the API and try again')
    return response

def password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, rest = sha1password[:5], sha1password[5:]
    res = request_api_data(first5_char)
    return password_leaks_count(res, rest)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... You should change your password')
        else:
            print(f'{password} was NOT found.. Carry On!')
    return 'done!'

if __name__=='__main__':
    main(sys.argv[1:])
