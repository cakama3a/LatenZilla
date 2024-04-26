# LatenZilla 1.0.0
# Speed Camera Latency Tester by John Punch

import pygame
import threading
import time
import sys

pygame.init()
pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

if not joysticks:
    print("No gamepad found")
    exit(1)
else:
    print(f"Found {len(joysticks)} gamepad(s)")
    for idx, joystick in enumerate(joysticks):
        print(f"{idx + 1}. {joystick.get_name()}")
    joystick = joysticks[0]
    joystick.init()

start_time = time.time()
prev_x_value = 0
prev_y_value = 0
prev_button_states = [False] * joystick.get_numbuttons()

def timer():
    while True:
        elapsed_time = time.time() - start_time
        elapsed_time_ms = int(elapsed_time * 1000)
        sys.stdout.write(f"\rTimer: {elapsed_time_ms} ms")
        sys.stdout.flush()
        time.sleep(0.001)

timer_thread = threading.Thread(target=timer)
timer_thread.daemon = True
timer_thread.start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1)

    if abs(x_axis) >= 0.99 and abs(prev_x_value) < 0.99:
        axis_time = time.time()
        axis_time_ms = int((axis_time - start_time) * 1000)
        sys.stdout.write(f"\rJoystick X-axis reached 0.99 at {axis_time_ms} ms\n")
        sys.stdout.flush()
    prev_x_value = x_axis

    if abs(y_axis) >= 0.99 and abs(prev_y_value) < 0.99:
        axis_time = time.time()
        axis_time_ms = int((axis_time - start_time) * 1000)
        sys.stdout.write(f"\rJoystick Y-axis reached 0.99 at {axis_time_ms} ms\n")
        sys.stdout.flush()
    prev_y_value = y_axis

    for button_idx in range(joystick.get_numbuttons()):
        button_state = joystick.get_button(button_idx)
        if button_state and not prev_button_states[button_idx]:
            button_time = time.time()
            button_time_ms = int((button_time - start_time) * 1000)
            sys.stdout.write(f"\rButton {button_idx} pressed at {button_time_ms} ms\n")
            sys.stdout.flush()
        prev_button_states[button_idx] = button_state

    time.sleep(0.001)