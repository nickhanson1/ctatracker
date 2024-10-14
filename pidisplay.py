from gpiozero import LED

with RPi.GPIO as GPIO

GPIO.setMode(GPIO.BCM)


class PiDisplay:

    current_display = []
    column = 0
    max_columns = 0
    max_rows = 0

    #Pins for anodes
    PIN_LATCH_A = 16
    PIN_CLOCK_A = 20
    PIN_DATA_A  = 21

    PIN_LATCH_C = 13
    PIN_CLOCK_C = 19
    PIN_DATA_C = 26

    def __init__(self, rows, cols):
        self.max_columns = cols
        self.max_rows = rows
        current_display = [[0] * cols] * rows

    def set_current_display(self, display):
        self.current_display = display

    def get_column(self, matrix, column):
        col = []
        for i in range(len(matrix)):
            col.append(matrix[i][column])
        return col

    
    def print_display(self):
        for r in self.current_display:
            print(r)
        print()
        print()

    #sets all pins to 0
    def reset_pins(self):
        GPIO.output(self.PIN_LATCH_C, 0)
        GPIO.output(self.PIN_CLOCK_C, 0)
        GPIO.output(self.PIN_DATA_C, 0)
        GPIO.output(self.PIN_LATCH_A, 0)
        GPIO.output(self.PIN_CLOCK_A, 0)
        GPIO.output(self.PIN_DATA_A, 0)

    # sets rows to 011111111111111
    def reset_rows(self):
        GPIO.output(self.PIN_LATCH_C, 0)
        GPIO.output(self.PIN_DATA_C, 1)
        for i in range(max_columns - 1):
            GPIO.output(self.PIN_CLOCK_C, 1)
            GPIO.output(self.PIN_CLOCK_C, 0)
        GPIO.output(self.PIN_DATA_C,  0)
        GPIO.output(self.PIN_CLOCK_C, 1)
        GPIO.output(self.PIN_CLOCK_C, 0)
        GPIO.output(self.PIN_LATCH_C, 1)
    
    #shifts the low voltage in the cathode shift register up one position
    # i.e. 011111111111111 -> 10111111111111 -> 110111111111111 > 11101111111111 -> etc.
    def push_rows(self):
        GPIO.output(self.PIN_LATCH_C, 0)
        GPIO.output(self.PIN_DATA_C, 1)
        GPIO.output(self.PIN_CLOCK_C, 1)
        GPIO.output(self.PIN_CLOCK_C, 0)
        GPIO.output(self.PIN_LATCH_C, 1)

    # prints to the display once
    def update_display(self, cmd_line = False):
        GPIO.output(self.PIN_DATA_C, 1)
        
        for i in range(max_rows):
            GPIO.output(self.PIN_LATCH_A, 0)
            GPIO.output(self.PIN_CLOCK_A, 0)
            line = self.display[i]
            for j in range(max_columns):
                GPIO.output(self.PIN_DATA_A, line[j])
                GPIO.output(self.PIN_CLOCK_A, 1)                
                GPIO.output(self.PIN_CLOCK_A, 0)
            GPIO.output(self.PIN_LATCH_A, 1)
            if i != 0:
                self.push_rows()
        
        #reset cathode pins
        GPIO.output(self.PIN_LATCH_C, 0)        
        GPIO.output(self.PIN_DATA_C, 0)
        GPIO.output(self.PIN_CLOCK_C, 1)
        GPIO.output(self.PIN_CLOCK_C, 0)
        GPIO.output(self.PIN_DATA_C, 0)
        GPIO.output(self.PIN_LATCH_C, 1)
        
        

