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

