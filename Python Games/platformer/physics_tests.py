# Model for jumping physics:

y_position = 0
y_velocity = 4
y_acceleration = -0.5

while True:
    # Jump-key is pressed:
    print(f"Y-Position: {y_position}, Y-Velocity: {y_velocity}")
    y_velocity += y_acceleration
    y_position += y_velocity
    if y_position == 0:
        # Collide with ground:
        print(f"Y-Position: {y_position}, Y-Velocity: {y_velocity}")
        break
