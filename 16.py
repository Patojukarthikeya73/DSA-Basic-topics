try:
    
    with open("file1.txt", "r") as infile:
        lines = infile.readlines()
        numerator = int(lines[0].strip())
        denominator = int(lines[1].strip())

    
    result = numerator / denominator
    output_message = f"Result: {result}"

except ZeroDivisionError:
    output_message = "Can't divide by zero."

except (ValueError, IndexError):
    output_message = "Invalid input. Please enter two numbers in the input file."

with open("output.txt", "w") as outfile:
    outfile.write(output_message)

