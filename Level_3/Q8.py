# You need to write a function that accepts an encoded string as a parameter.
# This string will contain a first name, last name, and an id.
# Values in the string can be separated by any number of zeros.
# The id is a numeric value but will contain no zeros. The function should
# parse the string and return a Python dictionary that contains the first name, last name, and id values.
# For example:
# Input : “Robert000Smith000123”
# Output: { “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }

def decode_string(encoded_string):
    parts = [part for part in encoded_string.split('0') if part]

    first_name = parts[0]
    last_name = parts[1]
    id_number = parts[2]

    decoded_dict = {
        "first_name": first_name,
        "last_name": last_name,
        "id": id_number
    }
    return decoded_dict

encoded_string = input("Write the first name, last name and ID using as many zeroes inbetween if you want: ")
decoded_dict = decode_string(encoded_string)
print(decoded_dict)
