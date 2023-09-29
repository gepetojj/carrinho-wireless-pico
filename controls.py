from machine import Pin, PWM

F = "forward"
B = "backward"
L = "left"
R = "right"
S = "stop"

AVAILABLE_CONTROLS = [F, B, L, R, S]


class Motor:
    def __init__(self, pin_1, pin_2, pin_vel):
        self.pin_1 = Pin(pin_1, Pin.OUT)
        self.pin_2 = Pin(pin_2, Pin.OUT)
        self.pin_vel = PWM(Pin(pin_vel, Pin.OUT))
        self.pin_vel.freq(1000)
        self.max_duty = 65025
        
    def move_forward(self, vel = 255):
        self.pin_1.on()
        self.pin_2.off()
        self.pin_vel.duty_u16(vel * self.max_duty / 255)
        
    def move_backward(self, vel = 255):
        self.pin_1.off()
        self.pin_2.on()
        self.pin_vel.duty_u16(vel * self.max_duty / 255)
        
    def stop(self):
        self.pin_1.off()
        self.pin_2.off()


def move(control, motor_one, motor_two, velocity = 255):
    if control == F:
        motor_one.move_forward(velocity)
        motor_two.move_forward(velocity)
        
    elif control == B:
        motor_one.move_backward(velocity)
        motor_two.move_backward(velocity)
        
    elif control == L:
        motor_one.move_forward(velocity)
        motor_two.stop()
        
    elif control == R:
        motor_one.stop()
        motor_two.move_forward(velocity)
        
    elif control == S:
        motor_one.stop()
        motor_two.stop()
