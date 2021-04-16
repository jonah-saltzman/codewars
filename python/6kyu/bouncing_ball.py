# A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.

# He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

# His mother looks out of a window 1.5 meters from the ground.

# How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

# Three conditions must be met for a valid experiment:
# Float parameter "h" in meters must be greater than 0
# Float parameter "bounce" must be greater than 0 and less than 1
# Float parameter "window" must be less than h.

def bouncing_ball(h, bounce, window):
    passes = 0
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    else:
        return b(h, bounce, window, passes)


def b(h, bounce, window, passes):
    h = h * bounce
    if h > window:
        return b(h, bounce, window, passes + 2)
    else:
        return passes + 1
