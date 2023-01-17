# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). 
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to ASCII, 
# then XOR each byte with a given value, taken from a secret key. 
# 
# The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; 
# for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. 
# The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
# If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. 
# The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower case characters. 
# Using p059_cipher.txt (right click and 'Save Link/Target As...'), 
# a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, 
# decrypt the message and find the sum of the ASCII values in the original text.

# === 
# text to ascii: ord(text)
# ascii to text: chr(ascii)

# To encrypt the string 'Hello World'
# Choose a 3 character lower case key 'pie'
# convert key to ascii: [112, 105, 101]
# Encrypt each character in string, rotating through values in key
# For 'H'
# convert to ascii: ord('H') = 72
# apply key
# 72^112 = 56
# repeat for 'e' using 105, 'l' with 101...
#
# To decrypt message with key:
# Start with first character 56
# apply key with first value
# 56^112 = 72
# Now convert to text
# chr(72) = 'H'
# repeat, cycling through key


def sum_of_decrypted():
    f = open('resources/p059_cipher.txt')
    msg_strings = f.read().strip().split(',')   # list of strings
    f.close()
    encrypted_msg = [int(x) for x in msg_strings]   # list of ascii
    
    # to find the key, split the encrypted message into three parts
    # then find the most frequent ascii 
    # these should be spaces
    slices = [encrypted_msg[0::3], encrypted_msg[1::3], encrypted_msg[2::3]]
    encrypted_spaces = [max(set(s), key=s.count) for s in slices]
    ascii_space = ord(' ')
    key = [s^ascii_space for s in encrypted_spaces]
    
    decrypted_msg = encrypted_msg.copy()
    for i in range(3):
        decrypted_msg[i::3] = [c^key[i] for c in encrypted_msg[i::3]]   # for text convert one more time with chr()

    return sum(decrypted_msg)

# solution
print(sum_of_decrypted())
