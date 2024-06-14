def create_code_dictionary():
    # dictionary with codes for each letter
    codes = {
        'A': '!', 'a': '9',
        'B': '@', 'b': '#',
        'C': '#', 'c': '=',
        'D': '$', 'd': ')',
        'E': '%', 'e': '+',
        'F': '^', 'f': '}',
        'G': '[', 'g': ']',
        'H': ':', 'h': ';',
        'I': '"', 'i': "'",
        'J': '<', 'j': '>',
        'K': '?', 'k': '/',
        'L': '|', 'l': '\\',
        'M': '~', 'm': '`',
        'N': '1', 'n': '2',
        'O': '3', 'o': '4',
        'P': '5', 'p': '6',
        'Q': '7', 'q': '8',
        'R': '0', 'r': 'z',
        'S': 'x', 's': 'c',
        'T': 'v', 't': 'b',
        'U': 'n', 'u': 'm',
        'V': 'a', 'v': 's',
        'W': 'd', 'w': 'f',
        'X': 'g', 'x': 'h',
        'Y': 'j', 'y': 'k',
        'Z': 'l', 'z': 'q',
        
    }
    return codes

def encrypt_file(input_filename, output_filename, codes):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()

        encrypted_content = ''
        for char in content:
            if char in codes:
                encrypted_content += codes[char]
            else:
                encrypted_content += char

        with open(output_filename, 'w') as file:
            file.write(encrypted_content)

        print(f"File encrypted and saved as {output_filename}")

    except FileNotFoundError:
        print(f"The file {input_filename} was not found.")

if __name__ == "__main__":
    codes = create_code_dictionary()
    encrypt_file('info_security-1.txt', 'encrypted.txt', codes)
