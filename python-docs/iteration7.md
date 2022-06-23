__In iteration seven of *Cave Escape*, we're going to implement the logic to have more than one set of poles. One set of poles is simply not challenging enough, and the overall change in logic to suit such functionality is quite minor.__

## Iteration Seven will look like:
![Iteration Seven](https://raw.githubusercontent.com/itco-education/cave-escape/master/Documentation/Images/iteration_7.gif)

## Code

### New Code
The new code in iteration seven is as follows:

#### Addition One
```python
GRAVITY = 0.08
MAX_SPEED = 5
JUMP_RECOVERY_BOOST = 2
FOREGROUND_SCROLL_SPEED = -2
NUM_POLES = 4
```

- We've added a constant called ```NUM_POLES``` to store the number of sets of poles we want in the game. The code provided has ```NUM_POLES``` being equal to the value of four, so this means there will be exactly four sets of poles in the game.

#### Addition Two
```python
def update_pole_array(pole_array):
    for i in range(len(pole_array)):
        pole_array[i] = update_poles(pole_array[i])

    return pole_array
```
- We've added a procedure called ```update_pole_array()``` in order to update every single set of poles in the array. Notice how the procedure simply uses a ```for``` loop in order to call the procedure ```update_poles()``` on each set of poles in the array. We added this procedure because we know that the procedure ```update_poles()``` works with a single set of poles, so why not just call it for each set of poles in the array?

#### Addition Four
```python
def draw_pole_array(pole_array):
    for i in range(len(pole_array)):
        draw_poles(pole_array[i])
```

-  We've added a procedure called ```draw_pole_array()``` in order to draw every single set of poles in the array. Notice how exactly like the procedure ```update_pole_array()```, ```draw_pole_array()``` simply uses a ```for``` loop, within which a call to the procedure ```draw_poles()``` is made for each set of poles in the array. We added this procedure because we know that the procedure ```draw_poles()``` works with a single set of poles, so why not just call it for each set of poles in the array?

### Any Changes to Main
```python
def main():
    open_window("Cave Escape", 432, 768)
    load_resource_bundle("CaveEscape", "cave_escape.txt")

    game_poles = [get_random_poles() for i in range(NUM_POLES)]

    player = get_new_player()

    while not window_close_requested_named("Cave Escape"):
        # Update
        process_events()
        handle_input(player)
        game_poles = update_pole_array(game_poles)
        update_velocity(player)
        update_sprite(player)

        # Pre-Draw
        clear_screen(color_white())

        # Draw
        draw_pole_array(game_poles)
        draw_sprite(player)

        # Post-Draw
        refresh_screen()

    # Cleanup
    free_resource_bundle("CaveEscape")
    close_window("Cave Escape")
```
Instead of the variable ```game_poles``` being a value of ```pole_data```, it is now a value of our array, ```poles```. We've also added a ```for``` loop to ensure that we set up all of the poles for the game. Our two new procedures to update and draw the array of poles, ```update_pole_array()``` and ```draw_pole_array()``` are also being called!

### Have a Crack
Now it's time for you to have a go at implementing iteration seven on your own.

### Complete Code
The complete code for iteration seven can be found [here](https://raw.githubusercontent.com/itco-education/cave-escape/master/python/iteration_7.py).
