
# Read the code.txt file and store the huffman code in a dictionary
def read_code_txt(path):
    huffmancode = {}
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("Average:"):
                continue
            key, value = line.strip().split(':')
            # Convert [space] back to an actual space character
            if key == "[space]":
                huffmancode[value] = ' '
            else:
                huffmancode[value] = key
    return huffmancode

# Decode the message using the huffman code
def decode_message(huffmancode, encoded_path, output_path):
    with open(encoded_path, 'r') as file:
        encoded_message = file.read()
    
    decoded_message = ""
    temp_code = ""

    for bit in encoded_message:
        temp_code += bit
        if temp_code in huffmancode:
            decoded_message += huffmancode[temp_code]
            temp_code = ""

    with open(output_path, 'w') as file:
        file.write(decoded_message)

# Main function
def main():
    code_file = "code.txt"
    encoded_file = "encodemsg.txt"
    output_file = "decodedmsg.txt"

    huffmancode = read_code_txt(code_file)
    decode_message(huffmancode, encoded_file, output_file)

if __name__ == "__main__":
    main()