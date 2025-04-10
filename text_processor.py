
# Python code to process input.txt and create output.txt  

# Read the contents of input.txt  
with open('input.txt', 'r') as file:  
    content = file.readlines()  

# Count the number of words and convert to uppercase  
word_count = 0  
uppercase_content = []  

for line in content:  
    # Count words in the current line  
    words = line.split()  
    word_count += len(words)  
    
    # Convert line to uppercase  
    uppercase_content.append(line.upper())  

# Write the processed text and word count to output.txt  
with open('output.txt', 'w') as output_file:  
    # Write uppercase content  
    output_file.writelines(uppercase_content)  
    
    # Write the word count  
    output_file.write(f'\nWord Count: {word_count}\n')  

# Print a success message  
print("The output.txt file has been created successfully!")  
