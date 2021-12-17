"""
    💡 Difference between string and bits
"""

# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are 8-bit values
def main():
    # setting some initial values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a string"
    print(s)

    # Try to combine the two. The line below will show an error:
    # print(s + b)

    # Bytes and strings need to be properly encoded and
    # decoded before being used together
    s2 = b.decode('utf-8')
    print(s + s2)

    b2 = s.encode('utf-8')
    print(b + b2)

    # Encode the string as UTF-32
    b3 = s.encode('utf-32')
    print(b3)

if __name__ == "__main__":
    main()