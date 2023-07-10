# PasswordChecker
Check how many time the password has been used using Password API 

import requests: This line imports the requests library, which allows the code to send HTTP requests to the specified URL.

import hashlib: This line imports the hashlib library, which provides various hash functions, including SHA1, which is used in this code.

import sys: This line imports the sys module, which provides access to system-specific parameters and functions.

def request_api_data(quary_character):: This line defines a function called request_api_data that takes a parameter quary_character. This function is responsible for making a request to the API to fetch the data for the given query character.

url = 'https://api.pwnedpasswords.com/range/' + quary_character: This line creates the URL for the API request by appending the quary_character to the base URL.

response = requests.get(url): This line sends a GET request to the URL using the requests library and assigns the response to the response variable.

if response.status_code != 200:: This line checks if the response status code is not equal to 200, which indicates a successful response. If the status code is not 200, it raises a RuntimeError with an error message.

raise RuntimeError(f'Error Fetching: {response.status_code}, Check the API and try again'): This line raises a RuntimeError with an error message that includes the response status code.

return response: This line returns the response object.

def password_leaks_count(hashes, hash_to_check):: This line defines a function called password_leaks_count that takes two parameters: hashes and hash_to_check. This function is responsible for counting the number of occurrences of a specific hash in the provided hashes.

hashes = (line.split(':') for line in hashes.text.splitlines()): This line splits the response text into lines and then splits each line at the colon (':') to separate the hash and the count. The result is a generator expression that yields tuples of (hash, count).

for h, count in hashes:: This line iterates over the tuples of (hash, count) obtained in the previous step.

if h == hash_to_check:: This line checks if the current hash matches the hash_to_check parameter.

return count: This line returns the count of the matching hash.

return 0: This line returns 0 if no matching hash is found.

def pwned_api_check(password):: This line defines a function called pwned_api_check that takes a password as a parameter. This function is responsible for calculating the SHA1 hash of the password and checking if it appears in the breached passwords database using the previous functions.

sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper(): This line calculates the SHA1 hash of the password by encoding it as UTF-8, computing the hash, and converting it to a hexadecimal string. The resulting hash is converted to uppercase.

first5_char, rest = sha1password[:5], sha1password[5:]: This line splits the SHA1 hash into the first five characters (first5_char) and the remaining characters (rest).

res = request_api_data(first5_char): This line calls the request_api_data function to retrieve the data from the API based on the first five characters of the SHA1 hash.

return password_leaks_count(res, rest): This line returns the result of calling the password_leaks_count function, passing the retrieved data and the remaining characters of the SHA1 hash.

def main(args):: This line defines the main function that takes a list of arguments (args).

for password in args:: This line iterates over each password in the provided arguments.

count = pwned_api_check(password): This line calls the pwned_api_check function to check if the password has been breached and assigns the result to the count variable.

if count:: This line checks if the count is not zero (i.e., if the password was found in the breached passwords database).

print(f'{password} was found {count} times... You should change your password'): This line prints a message indicating that the password was found and advises the user to change it.

print(f'{password} was NOT found.. Carry On!'): This line prints a message indicating that the password was not found in the breached passwords database.

return 'done!': This line returns the string 'done!' to indicate the completion of the main function.

if __name__=='__main__':: This line checks if the script is being run directly (not imported as a module).

main(sys.argv[1:]): This line calls the main function, passing the command-line arguments (excluding the script name) as a list to check the passwords.
