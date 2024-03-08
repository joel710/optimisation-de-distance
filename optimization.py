import sys
import math

# game loop
while True:
    # x: x position of your pod
    # y: y position of your pod
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    x, y, next_checkpoint_x, next_checkpoint_y = [int(i) for i in input().split()]

    # Calculate the distance to the next checkpoint
    distance = math.sqrt((next_checkpoint_x - x)*2 + (next_checkpoint_y - y)*2)

    # Adjust the thrust based on the distance to the checkpoint
    thrust = min(max(int(distance * 0.75), 0), 100)

    # Output the target position and thrust
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust))
