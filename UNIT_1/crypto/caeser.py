
from helpers import alphabet_position, rotate_character  

def encrypt(text, rot):
    """Receives text and a rotation number, and returns an encrypted message."""
    encrypted_text = ""
    for char in text:
        letter = rotate_character(char, rot)                                    # calls the rotate_character function using (text) char and given rotation
        encrypted_text = encrypted_text + letter                                    # builds the encrypted text
    return (encrypted_text) 