# AutomaticCatLitterBox

To run the code, you open the terminal and cd to the file location in where you stored the python files.
Running the code requires 
    1. adafruit_servokit library
    2. gpiozero library
    3. enable i2c in raspberry Pi
    4. enable serial for UART use in raspberry Pi

To run the code
    python main.py

For running the tests, you will need to install the func timeout library for testing the state machine

To run the two test code
    python main_test.py
        This test requires you to put in inputs to test the state machine
            WARNING:(Might need to input a few times before moving to the next state due to the the input function)
        To see what input are required to test the state machine, see the comments in my_states.py for more details
    
    python main_test_fast.py
        This is an automated test code that randomize the inputs for the state machine and test the state machine
        50 times
            The number of times for testing the state machine can be changed to suit your needs
            In addition to the probability of the inputs getting through the timer
        For more information, see comment in main_test_fast.py
