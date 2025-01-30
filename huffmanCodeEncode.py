from collections import Counter
import sys

# Create the new list contain all the key from new dictionary
def keyforlist(new_dic):
    keys = list(new_dic.keys())
    return keys

# Create the new list contain all the value from new dictionary
def valueforlist(new_dic):
    value = list(new_dic.values())
    return value

# Sort the dictionary by value and key
def sort_dict(dic):
    sorted_dic = dict(sorted(dic.items(), key=lambda x: (x[1], x[0])))
    return sorted_dic

# Update the huffman code for the left and right child
def update_huffmancode(huffmancode, keys, index, value):
    for key in keys[index]:
        if key in huffmancode:
            huffmancode[key] = value + huffmancode[key]
        else:
            huffmancode[key] = value


def huffman(sorted_dic):
    index = 0
    huffmancode = {}
    while index < len(sorted_dic) - 1:
        keys = keyforlist(sorted_dic)
        value = valueforlist(sorted_dic)
        if keys[index] < keys[index + 1]:
            parentkey = keys[index] + keys[index + 1]
            parentvalue = value[index] + value[index + 1]
            sorted_dic[parentkey] = parentvalue
            update_huffmancode(huffmancode, keys, index, '0')
            update_huffmancode(huffmancode, keys, index + 1, '1')
        else:
            parentkey = keys[index + 1] + keys[index]
            parentvalue = value[index + 1] + value[index]
            sorted_dic[parentkey] = parentvalue
            update_huffmancode(huffmancode, keys, index + 1, '0')
            update_huffmancode(huffmancode, keys, index, '1')
        sorted_dic = sort_dict(sorted_dic)
        index += 2
    result = dict(sorted(huffmancode.items()))
    return result

# Calculate the average and write it to the end of the file
def FindAverage(result, temp):
    total = 0
    frequency = 0
    for key in result:
        for key1 in temp:
            if key == key1:
                total += len(result[key]) * temp[key1]
    for value in temp.values():
        frequency += value
    average = total / frequency
    return average

# Write the huffman code to the file
def create_code_txt(huffmancode, average):
    with open('code.txt', 'w') as file:
        for key, value in huffmancode.items():
            # Write space as a visible symbol in the file
            if key == ' ':
                file.write(f"[space]:{value}\n")
            else:
                file.write(f"{key}:{value}\n")
        file.write(f"Average:{average}\n")

# Encode the message using the huffman code
def create_encodemsg_txt(huffmancode, content, output_path):
    with open(output_path, 'w') as file:
        for char in content:
            file.write(huffmancode[char])

# Main function
def main():
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        content = list(file.read())
    dic = dict(Counter(content))
    if "\n" in dic:
        del dic["\n"]
    sorted_dic = sort_dict(dic)
    temp = sorted_dic.copy()

    # Generate Huffman codes and encode the file
    result = huffman(sorted_dic)
    average = FindAverage(result, temp)
    create_code_txt(result, average)
    create_encodemsg_txt(result, content, 'encodemsg.txt')

if __name__ == "__main__":
    main()