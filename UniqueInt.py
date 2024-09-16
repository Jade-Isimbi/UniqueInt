#!/usr/bin/python3
import os
import time

class UniqueInt:

    def processFile(self, inputFilePath, outputFilePath):
        """
        Processes the input file to extract unique integers and writes them to the output file.
        Each line of the file is expected to contain one integer.
        """
        unique_num = self.readNextItemFromFile(inputFilePath)
        self.write_unique_integers(unique_num, outputFilePath)
def readNextItemFromFile(self, inputFilePath):
        """
        Reads integers from the input file, ensuring each integer is within the valid range and unique.
        Returns a sorted list of unique integers.
        """
        unique_num = set()
        
        with open(inputFilePath, 'r') as input_file:
            for line in input_file:
                try:
                    number = int(line.strip())
                    
                    # Check if the number is within the valid range
                    if -1023 <= number <= 1023:
                        unique_num.add(number)
                except ValueError:
                    # Ignore lines that don't contain valid integers
                    continue
        
        return sorted(unique_num)

    def write_unique_integers(self, unique_num, outputFilePath):
        """
        Writes the list of unique integers to the output file.
        """
        with open(outputFilePath, 'w') as output_file:
            for number in unique_num:
                output_file.write(f"{number}\n"
                        )
                if __name__ == "__main__":
    input_folder = "/home/jade/UniqueInt/inputs"
    output_folder = "/home/jade/UniqueInt/results"

    unique_int_processor = UniqueInt()

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{filename}_results.txt")

            # Timing for each file
            start_time = time.time()
            unique_int_processor.processFile(input_path, output_path)
            end_time = time.time()

            print(f"Processed {filename} in {end_time - start_time:.4f} seconds")

