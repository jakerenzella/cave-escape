__In iteration eight of *Cave Escape*, we're going to focus on polishing the game in terms of visual aesthetics and code presentation. Visually, the game is going to be practically complete after the eighth iteration. We're going to include a scrolling background for the game to help set the scene. The code tidy up involved in iteration eight is purely for convention and to conform to best practice of having well presented, readable code. This iteration sees the addition of nine new code additions, so it is quite busy.__

## Iteration Eight will look like:
![Iteration Eight](https://raw.githubusercontent.com/itco-education/cave-escape/master/Documentation/Images/iteration_8.gif)

## Code

### New Code
The new code in iteration eight is as follows:

#### Addition One
```python
GRAVITY = 0.08
MAX_SPEED = 5
JUMP_RECOVERY_BOOST = 2
FOREGROUND_SCROLL_SPEED = -2
BACKGROUND_SCROLL_SPEED = -1
NUM_POLES = 4
```

- We've added another constant called ```BACKGROUND_SCROLL_SPEED``` to store the value at which we want the background to scroll at. These values ```FOREGROUND_SCROLL_SPEED``` and ```BACKGROUND_SCROLL_SPEED``` are different because we want to create parallax scrolling.

#### Addition Two
```python
class scene_data:
    def __init__(self, _background, _foreground, _foreroof):
        self.background = _background
        self.foreground = _foreground
        self.foreroof = _foreroof
```
- The class ```scene_data``` has been added to house all the information related to the game's background. Notice it consists of three separate sprites, ```background```, ```foreground``` and ```foreroof```.

#### Addition Three
```python
class game_data:
    def __init__(self, _scene, _poles, _player):
        self.scene = _scene
        self.poles = _poles
        self.player = _player
```
-  The class ```game_data``` has been added to house all the information that the game relies upon, like the player, background and the poles. We'll talk more about this a little later when we discuss how the ```main()``` procedure has changed in this iteration.

#### Addition Four
```python
def get_new_scene():
    resultBackground = create_sprite_with_bitmap_named("Background")
    sprite_set_x(resultBackground, 0)
    sprite_set_y(resultBackground, 0)
    sprite_set_dx(resultBackground, BACKGROUND_SCROLL_SPEED)

    resultForeground = create_sprite_with_bitmap_and_animation_named("Foreground", "ForegroundAnimations")
    sprite_set_x(resultForeground, 0)
    sprite_set_y(resultForeground, screen_height() - sprite_height(resultForeground))
    sprite_set_dx(resultForeground, FOREGROUND_SCROLL_SPEED)
    sprite_start_animation_named(resultForeground, "Fire")

    resultForeroof = create_sprite_with_bitmap_named("Foreroof")
    sprite_set_x(resultForeroof, 0)
    sprite_set_y(resultForeroof, 0)
    sprite_set_dx(resultForeroof, FOREGROUND_SCROLL_SPEED)

    return scene_data(resultBackground, resultForeground, resultForeroof)
```
- Now, we need some logic in order to be able to add the background to the game so that we can see it. To do that, we've added a new function called ```get_new_scene()```, which is responsible for generating the data associated with the scene. This function behaves similarly to the functions ```get_new_player()``` and ```get_random_poles()```. The function ```get_new_scene()``` returns a value of ```scene_data```, and as you can see, it is responsible for setting all of the values within the ```scene_data``` class. It sets the sprites for the ```background```, ```foreground``` and ```foreroof```, as well as their locations and the animation for the ```foreground``` sprite. Because the background has a scrolling effect, the delta x, or horizontal movement speed of the three sprites have been set accordingly.

#### Addition Five
```python
def update_scene(scene):
    update_sprite(scene.background)
    update_sprite(scene.foreground)
    update_sprite(scene.foreroof)

    if sprite_x(scene.background) <= -(sprite_width(scene.background) / 2):
        sprite_set_x(scene.background, 0)

    if sprite_x(scene.foreground) <= -(sprite_width(scene.foreground) / 2):
        sprite_set_x(scene.foreground, 0)
        sprite_set_x(scene.foreroof, 0)
```
- A new procedure called ```update_scene()``` has been added to ensure that the background wraps continuously around the screen, similar to the fashion in which the poles do. The logic within the procedure makes sure that the game scene always renders the background in a manner which makes the scrolling of it seem infinite.

#### Addition Six
```python
def update_player(player):
    update_velocity(player)
    update_sprite(player)
```
- The procedure ```update_player()``` has been added so that the logic to update the player can be moved out of the ```main()``` procedure into a separate procedure which focusses exclusively on managing the player element. We've done this to conform to good conventional practice and to apply what is called modular decomposition. Briefly, modular decomposition involves separating code into logical blocks, which are focussed on a specific task, i.e. updating the player.

#### Addition Seven
```python
def update_game(game):
    process_events()
    handle_input(game.player)
    game.poles = update_pole_array(game.poles)
    update_player(game.player)
    update_scene(game.scene)
    return game
```
- A procedure called ```update_game()``` has been added, for the same reasons as the procedure ```update_player()```. This is another application of good practice and a general code tidy up.

#### Addition Eight
```python
def draw_game(game):
    draw_sprite(game.scene.background)
    draw_pole_array(game.poles)
    draw_sprite(game.player)
    draw_sprite(game.scene.foreground)
    draw_sprite(game.scene.foreroof)
```
- Yet another procedure has been added to apply modular decomposition to our game. The procedure ```draw_game()``` has been created to house all the calls that are responsible for drawing the game elements to the screen.

#### Addition Nine
```python
def get_new_game():
    load_resource_bundle("CaveEscape", "cave_escape.txt")

    resultScene = get_new_scene()
    resultPoles = [get_random_poles() for i in range(NUM_POLES)]
    resultPlayer = get_new_player()

    return game_data(resultScene, resultPoles, resultPlayer)
```

- Finally, this big iteration concludes with the addition of a new procedure called ```set_up_game()```. Out of good practice, we've moved all the game setup calls from the ```main()``` procedure into a single procedure called ```set_up_game()```. It is here where all the game elements are instantiated, such as the background, poles, and player.

### A Little Change to Main
```python
def main():
    open_window("Cave Escape", 432, 768)

    game_data = get_new_game()

    while not window_close_requested_named("Cave Escape"):
        # Update
        game_data = update_game(game_data)

        # Pre-Draw
        clear_screen(color_white())

        # Draw
        draw_game(game_data)

        # Post-Draw
        refresh_screen()

    # Cleanup
    free_resource_bundle("CaveEscape")
    close_window("Cave Escape")
```

Look how tidy the ```main()``` procedure looks now after our code tidy up. We now only have a single variable called ```game```, which is a value of ```game_data```. We call our new procedure ```set_up_game()``` before the game loop to set the game up, then in our game loop, we have calls to ```update_game()``` and ```draw_game()```, which handle everything else that the game depends on.

### Have a Crack
Now it's time for you to have a go at implementing iteration eight on your own.

### Complete Code
The complete code for iteration eight can be found [here](https://raw.githubusercontent.com/itco-education/cave-escape/master/python/iteration_8.py).
