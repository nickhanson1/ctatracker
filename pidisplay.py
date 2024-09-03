from gpiozero import LED


class PiDisplay:

    current_display = []
    column = 0
    max_columns = 0

    def __init__(self, rows, cols):
        self.max_columns = cols
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

    def update_display(self, cmd_line = False):
        if cmd_line:
            self.print_display()
            return
        column = self.get_column(self.current_display, column)
        for i in range(1, 15):
            led = LED(i)
            if column[i] == 0:
                led.on()
            else:
                led.off()
        
        binary = str(bin(column))

        for i in range(len(binary)):
            led = LED(14 + i + 1)
            if binary[i] == "1":
                led.on()
            else:
                led.off()
        
        self.column = (self.column + 1) % self.max_columns

