__In the sixth iteration of *Cave Escape*, we're going to make a few additions to ensure that once the poles move off the far left of the screen, they get moved back to their default position. This will ensure that the poles can be reused as obstacles.__

## Iteration Six will look like:
![Iteration Six](https://raw.githubusercontent.com/itco-education/cave-escape/master/Documentation/Images/iteration_6.gif)

## Code

### New Code
The new code in iteration six is as follows:

#### Addition One
```python
def reset_pole_data(poles):
    free_sprite(poles.up_pole)
    free_sprite(poles.down_pole)

    poles = get_random_poles()
    return poles
```

- We've added a new procedure called ```reset_pole_data()``` that is going to reset the poles once they move off the left of screen. Notice that it calls the function ```get_random_poles()``` that we implemented in iteration five. It makes sense to reuse code where you can, and the poles that the function ```get_random_poles()``` returns are exactly what we need when we have to reset them.

#### Addition Two
```python
def update_poles(poles):
    update_sprite(poles.up_pole)
    update_sprite(poles.down_pole)

    if ((sprite_x(poles.up_pole) + sprite_width(poles.up_pole)) < 0):
        poles = reset_pole_data(poles)

    return poles
```
- We've modified ```update_poles()``` to check to see if the poles have moved off the left of the screen and if they have, we simply reset them. Note that we only have to check to see if one of the poles have moved off of the screen, because they are vertically aligned.

### Any Changes to Main
Not in this iteration. Hurray!

In Main, instead of: 

```python
get_random_poles()
```
to:
```python
game_poles = get_random_poles()
```

### Have a Crack
Now it's time for you to have a go at implementing iteration six on your own.

### Complete Code
The complete code for iteration six can be found [here](https://raw.githubusercontent.com/itco-education/cave-escape/master/python/iteration_6.py).
