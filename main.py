import sys

if "balls" in sys.argv:
    import balls.balls
elif "spiral" in sys.argv:
    import spiral.spiral
elif "spiral_sand" in sys.argv:
    import spiral.spiral_sand
