import rsa         #importing RSA from python library 

public_key, private_key = rsa.newkeys(1024)    #gnereating public and private with rsa.newkeys() method which takes the key lenghth as the paramter and the value of parameter must be greater then 16.

Input_msg = input("Enter the string:") # the message that will be encrypted
print("\n")
Encoded_msg = rsa.encrypt(Input_msg.encode(),public_key) # rsa.encrypt method will be used to encrypt the message with public key.

Decoded_msg = rsa.decrypt(Encoded_msg, private_key).decode() # the encrypted message will be decrypted by using rsa.decrypt method with private key.


print("Actual Message: ", Input_msg,"\n") # print the original message.

print("Encrypted Message: ", Encoded_msg,"\n") # print the encrypted message.

print("Decrypted Message: ", Decoded_msg,"\n") # print the decoded message.
