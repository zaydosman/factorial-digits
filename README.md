Factorial Digits

The factorial-digits.py file can be used to calculate the sum of the digits of a given number's factorial.

Prerequisites:

Python 3 and Docker should be installed. 

Guide:

1 Download "zaydosman.tar.gz" and extract the folder "factorial-digits".

2 Navigate to the folder directory /factorial-digits/ in your shell CLI.

3 Build the docker image using the command "docker build -t factorial-digits ."

4 Use the command "docker run --rm factorial-digits 1000" to run the container. The number 1000 is the input given as an argument, and can be changed to any non-negative integer of your choice.