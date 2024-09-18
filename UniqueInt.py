#!/usr/bin/python3
import os
import time

class UniqueInt:

    def processFile(self, inputFilePath, outputFilePath):
        """
        Processes the input file to extract unique integers and writes them to the output file.
        Each line of the file is expected to contain one integer.
        """
        unique_numbers = self.readNextItemFromFile(inputFilePath)
        sorted_unique_numbers = self.sortNumbers(unique_numbers)
        self.write_unique_integers(sorted_unique_numbers, outputFilePath)

    def readNextItemFromFile(self, inputFilePath):
        """
        Reads integers from the input file, ensuring each integer is within the valid range and unique.
        Returns a list of unique integers.
        """
        unique_numbers = []

        # Open the input file and read line by line
        with open(inputFilePath, 'r') as file:
            for line in file:
                try:
                    # Try to convert the line to an integer
                    number = int(line.strip())
                    
                    # If the number is within range and not already in the list, add it
                    if -1023 <= number <= 1023 and number not in unique_numbers:
                        unique_numbers.append(number)
                except ValueError:
                    # Ignore lines that don't contain valid integers
                    continue
        
        return unique_numbers

    def sortNumbers(self, numbers):
        """
        Sorts the list of numbers in increasing order using a basic sorting algorithm (Bubble Sort).
        """
        n = len(numbers)

        # Simple Bubble Sort to sort numbers
        for i in range(n):
            for j in range(n - i - 1):
                if numbers[j] > numbers[j + 1]:
                    # Swap if numbers are out of order
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        return numbers

    def write_unique_integers(self, numbers, outputFilePath):
        """
        Writes the sorted list of unique integers to the output file.
        """
        with open(outputFilePath, 'w') as file:
            for number in numbers:
                file.write(f"{number}\n")


if __name__ == "__main__":
    # Define where the input files are located and where to save the output
    input_folder = "/home/jade/UniqueInt/inputs"
    output_folder = "/home/jade/UniqueInt/results"
    
    # Create an instance of the UniqueInt class
    unique_int_processor = UniqueInt()

    # Process each text file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{filename}_results.txt")

            # Measure the time it takes to process the file
            start_time = time.time()
            unique_int_processor.processFile(input_path, output_path)
            end_time = time.time()

            print(f"Processed {filename} in {end_time - start_time:.4f} seconds")

