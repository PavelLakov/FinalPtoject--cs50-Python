import pytest
from project import caesar_cipher, get_shifts, encrypt_text, decrypt_text

# Test cases for the caesar_cipher function
def test_caesar_cipher():
    # Testing basic encryption and decryption
    assert caesar_cipher("abc", [1], False) == "bcd", "Basic encryption failed"
    assert caesar_cipher("bcd", [1], True) == "abc", "Basic decryption failed"
 

# Test cases for the get_shifts function
def test_get_shifts():
    # Testing valid input
    assert get_shifts("1,2,3") == [1, 2, 3], "Failed to parse valid shifts"
    # Testing invalid input
    with pytest.raises(ValueError):
        get_shifts("invalid"), "Failed to raise ValueError on invalid input"



def test_encrypt_text():
    # This test assumes encrypt_text function takes plaintext and shift as input and returns ciphertext
    assert encrypt_text("abc", "1") == "bcd", "Encryption failed for input 'abc' with shift '1'"
    

def test_decrypt_text():
    # This test assumes decrypt_text function takes ciphertext and shift as input and returns plaintext
    assert decrypt_text("bcd", "1") == "abc", "Decryption failed for input 'bcd' with shift '1'"
    
if __name__ == "__main__":
    pytest.main()
