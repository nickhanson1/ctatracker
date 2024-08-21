from gpiozero import LED


class PiDisplay:

    current_display = []
    column = 0
    max_columns = 0

    def __init__(self, max_cols):
        self.max_columns = max_cols

    def set_current_display(display):
        current_display = display

    def get_column(self, matrix, column):
        col = []
        for i in range(len(matrix)):
            col.append(matrix[i][column])
        return col

    def update_display(self):
        column = self.get_column(self.current_display, row)
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

