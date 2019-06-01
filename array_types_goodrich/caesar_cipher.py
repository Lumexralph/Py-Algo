class CaesarCipher:
    """Class for doing encryption and
    decryption using a Caesar cipher.
    """

    def __init__(self, shift):
        """Construct Caesar cipher using given
        integer shift for rotation.
        """
        encoder = [None] * 26         # temp array for encryption
        decoder = [None] * 26         # temp array for decryption
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)


    def encrypt(self, message):
        """Return string representing encripted message"""
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret"""
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')              # index from 0 to 25
                msg[k] = code[j]                        # swap the characters
        return ''.join(msg)

if __name__ == '__main__':
    cipher = CaesarCipher(4)
    message = "THE EAGLE IS IN PLAY, MEET AT JOE's"
    coded = cipher.encrypt(message)
    print('Secret: ', coded)

    answer = cipher.decrypt(coded)
    print('Message: ', answer)