from collections import Counter
import sys

def keyforlist(new_dic):                                        #Create the new list contain all the key from new dictionary
    keys = list(new_dic.keys())
    return keys

def valueforlist(new_dic):                                      # Create the new list contain all the value from new dictionary
    value = list(new_dic.values())
    return value

def sort_dict(dic):
    sorted_dic = dict(sorted(dic.items(),key=lambda x: (x[1],x[0])))
    return sorted_dic

def update_huffmancode(huffmancode,keys,index,value):           #update the huffman code for the left and right child
    for key in keys[index]:
        if key in huffmancode:                                  #if the key is already in the huffman code dictionary
            huffmancode[key] = value + huffmancode[key]
        else:                                                   #if the key is not in the huffman code dictionary
            huffmancode[key] = value

def huffman(sorted_dic):
    index = 0
    huffmancode = {}
    while (index< len(sorted_dic)-1):                           #loop until the length of the sorted dictionary is 1
        keys = keyforlist(sorted_dic)                           #get the key from the sorted dictionary
        value= valueforlist(sorted_dic)                         #get the value from the sorted dictionary
        if keys[index] < keys[index+1]:                         #compare the key to determine the parent key
            parentkey = keys[index] + keys[index+1]
            parentvalue = value[index] + value[index+1]         #combine the value of the parent key to get the parent value
            sorted_dic[parentkey] = parentvalue                 #add the parent key and value to the sorted dictionary
            update_huffmancode(huffmancode,keys,index,'0')      #update the huffman code for the left child
            update_huffmancode(huffmancode,keys,index+1,'1')    #update the huffman code for the right child
        else:
            parentkey = keys[index+1] + keys[index]             #same with the above but the key is different
            parentvalue = value[index+1] + value[index]
            sorted_dic[parentkey] = parentvalue
            update_huffmancode(huffmancode,keys,index+1,'0')
            update_huffmancode(huffmancode,keys,index,'1')    
        sorted_dic = sort_dict(sorted_dic)                      #sort the dictionary again
        index += 2                                              #increment the index by 2
    result = dict(sorted(huffmancode.items()))                  #sort the huffman code dictionary by key
    return result

def FindAverage(result,temp):
    total = 0
    frequency = 0
    for key in result:
        for key1 in temp:
            if key == key1:
                total += len(result[key])*temp[key1]
    for value in temp.values():
        frequency += value
    average = total/frequency
    return average

def create_code_txt(huffmancode,average):
    with open('code.txt','w') as file:
        for key,value in huffmancode.items():
            file.write(str(value) + '\n')
        file.write(str(average) + '\n')                         #write the average in the end of the file

def create_encodemsg_txt(huffmancode,content,output_path):
    with open(output_path,'w') as file:
        for char in content:
            for key in huffmancode:
                if char == key:
                    file.write(huffmancode[key])

def main():
    file_path = sys.argv[1]
    with open(file_path,'r') as file:
            content = []
            for char in file.read():
                content.append(char)                            #create a list contain all the character in the file
    dic = dict(Counter(content))                                #transform the list into dictionary base on the frequency of each character
    if "\n" in dic:
        del dic["\n"]                                           #remove the new line character from the dictionary
    sorted_dic = sort_dict(dic)                                 #sort the dictionary base on frequency
    temp = sorted_dic.copy()                                    #copy the sorted dictionary to a new dictionary for later use

    #Function call
    result = huffman(sorted_dic)                                #return the huffman code
    average = FindAverage(result,temp)                          #return the average length of the huffman code * frequency
    create_code_txt(result,average)                             #create the code.txt file
    create_encodemsg_txt(result, content,'encodemsg.txt')       #create the encodemsg.txt file

main()