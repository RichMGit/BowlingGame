frames = []
frame_total = []
while len(frames) < 2:
    ball_one = int(raw_input('Enter the score of ball one: '))
    ball_two = int(raw_input('Enter the score of ball two: '))
    #if ball_one == 10:

    frames.append([ball_one, ball_two])
frame_total = [sum(frame) for frame in frames]
total = sum(frame_total)
print(frame_total)
print(total)
