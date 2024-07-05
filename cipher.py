class Cipher:
    def __init__(self, cipher_file_location, skey):
        self.self_content = bytearray()
        self.self_key = skey
        self.key = []

        with open(cipher_file_location, 'rb') as file:
            self.self_content.extend(file.read())
        try:
            self.sizeofkey = len(skey)
        except:
            pass
        self.convert_string_to_values(skey)

    def size_of_key(self, skey):
        return len(skey)

    def convert_string_to_values(self, skey):
        if skey:
            self.key = [ord(char) for char in skey]

    def vig(self, encrypt_or_decrypt):
        buffer = bytearray()
        if encrypt_or_decrypt == 'd':  # Decrypt
            self.key = [-k for k in self.key]

        count = 0
        print("key:",self.key)
        if self.key:
            for byte in self.self_content:
                if count == len(self.key):
                    count = 0
                new_byte = (byte + self.key[count]) % 256  # Ensure byte is in range [0, 255]
                print(byte,"-->",new_byte)
                buffer.append(new_byte)
                count += 1

            self.self_content = buffer

    def output(self, output_name):
        with open(output_name, 'wb') as file:
            file.write(self.self_content)

 
