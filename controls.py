from machine import Pin

F = "forward"
B = "backward"
L = "left"
R = "right"
S = "stop"

AVAILABLE_CONTROLS = [F, B, L, R, S]


class Motor:
    def __init__(self, pin_1, pin_2):
        self.pin_1 = Pin(pin_1, Pin.OUT)
        self.pin_2 = Pin(pin_2, Pin.OUT)
        
    def move_forward(self):
        self.pin_1.on()
        self.pin_2.off()
        
    def move_backward(self):
        self.pin_1.off()
        self.pin_2.on()
        
    def stop(self):
        self.pin_1.off()
        self.pin_2.off()


def move(control, motor_one, motor_two):
    if control == F:
        motor_one.move_forward()
        motor_two.move_forward()
        
    elif control == B:
        motor_one.move_backward()
        motor_two.move_backward()
        
    elif control == L:
        motor_one.move_forward()
        motor_two.stop()
        
    elif control == R:
        motor_one.stop()
        motor_two.move_forward()
        
    elif control == S:
        motor_one.stop()
        motor_two.stop()
