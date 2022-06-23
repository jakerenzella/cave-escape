__Iteration nine is going to be quite a big one too, where there are some big changes to improve gameplay in order to make our game...more of a game. In this iteration, we're going to add some music to give the game its own little soundtrack, which will make the experience more immersive. The big changes, on top of the music, are the addition of collisions, so the player can collide with the environment, a scoring system and the ability to have the game reset if the player does collide with the environment. Iteration nine very nearly implements a completely functional game, ready for shipping.__

## Iteration nine will look like:
![Iteration Nine](https://raw.githubusercontent.com/itco-education/cave-escape/master/Documentation/Images/iteration_9.gif)

## Code

### New Code
The new code in iteration nine is as follows:


#### Addition Two
```python
class player_data:
    def __init__(self, _sprite_data, _score, _is_dead):
        self.sprite_data = _sprite_data
        self.score = _score
        self.is_dead = _is_dead
```
- We've added a new class called ```player_data```. Our player can no longer just be a sprite. If you take a look at the class, you'll notice it has three fields. The first of which is our player sprite. The next being the ```score``` and the third being a field called ```is_dead```. We need this field to tell the game when the player dies from colliding with the environment.

#### Addition Three
```python
class game_data:
    def __init__(self, _scene, _poles, _player):
        self.scene = _scene
        self.poles = _poles
        self.player = _player
```
- The ```game_data``` class has changed only slightly. Instead of the ```player``` field being a sprite, it is now a value of our new class ```player_data```.

#### Addition Four
```python
def get_new_player():
    resultSpriteData = create_sprite_with_bitmap_and_animation_named("Player", "PlayerAnimations")

    sprite_set_x(resultSpriteData, (screen_width() / 2) - sprite_width(resultSpriteData))
    sprite_set_y(resultSpriteData, screen_width() / 2)
    sprite_start_animation_named(resultSpriteData, "Fly")

    resultScore = 0
    resultIsDead = False

    return player_data(resultSpriteData, resultScore, resultIsDead)
```

- Our function ```get_new_player()``` has had to change in order to support the new scoring system as well as our collision system. In the function, we now set the ```score``` to zero and set the player to be alive when the function is called (```result.is_dead = false```). It also now returns ```player_data``` instead of ```sprite```.

#### Addition Five
```python
def get_random_poles():

    resultUpPole = create_sprite_with_bitmap_named("UpPole")
    resultDownPole = create_sprite_with_bitmap_named("DownPole")

    sprite_set_x(resultUpPole, screen_width() + rnd_int(1200))
    sprite_set_y(resultUpPole, screen_height() - sprite_height(resultUpPole) - rnd_int(bitmap_height_of_bitmap_named("Foreground")) + 1)

    sprite_set_x(resultDownPole, sprite_x(resultUpPole))
    sprite_set_y(resultDownPole, rnd_int(bitmap_height_of_bitmap_named("Foreroof")) + 1)

    sprite_set_dx(resultUpPole, FOREGROUND_SCROLL_SPEED)
    sprite_set_dx(resultDownPole, FOREGROUND_SCROLL_SPEED)

    return pole_data(True, resultUpPole, resultDownPole)
```
- The ```get_random_poles()``` function has also changed. Only slightly, though. Notice that the function now sets the ```pole_data``` value that it returns to have a ```score_limiter``` value of ```true```. Additionally, the positioning of the poles in terms of their vertical position is random. Because we have the roof and the floor, we can position the poles more dynamically. Now, we're going to use the ```score_limiter``` to increment the score of the player every time they pass a set of poles. Once they pass a set of poles, the player's score will be incremented and the ```score_limiter``` for that set of poles will be set to ```false```. The reasoning behind this will become more clear when we talk about the changes made to ```update_poles()```.

#### Addition Six
```python
def handle_input(player):
    if key_typed(KeyCode.space_key):
        sprite_set_dy(player.sprite_data, sprite_dy(player.sprite_data) - JUMP_RECOVERY_BOOST)
```
- ```handle_input()``` previously took a sprite as an argument, but due to our changes to the way the player is stored, it now needs to take a ```player_data```. We also need to append ```.sprite_data``` to the end of ```player```, as ```player``` is now a ```player_data```, not a ```sprite```.

#### Addition Seven
```python
def update_poles(poles, player):
    update_sprite(poles.up_pole)
    update_sprite(poles.down_pole)

    if sprite_x(poles.up_pole) < sprite_x(player.sprite_data) and poles.score_limiter:
        poles.score_limiter = False
        player.score += 1

    if (sprite_x(poles.up_pole) + sprite_width(poles.up_pole)) < 0:
        poles = reset_pole_data(poles)

    return poles
```

- Now we're going to take a look at the changes made to ```update_poles()```. Take a close look at the conditional statements in this procedure. In particular, let's focus on this conditional section of code here ```if ((sprite_x(poles.up_pole) < sprite_x(player.sprite_data)) && poles.score_limiter)``` to understand why we need the ```score_limiter```. We're checking to see ```if``` the player has passed any poles and ```if``` the ```score_limiter``` is ```true```. If those conditions are ```true```, we then set the ```score_limiter``` field  to ```false``` and increment the player's ```score```. Now, ```score_limiter``` has to change to ```false``` because, if it never did, once the player passes some poles, the ```if``` statement would evaluate to ```true``` and the player's score would keep incrementing because the player would be beyond the poles. Phew. Tongue twisting. The best way to see the bug that this would cause is to remove this condition ```poles.score_limiter``` from the ```if``` statement.

#### Addition Eight
```python
def update_pole_array(game):
    for i in range(len(game.poles)):
        game.poles[i] = update_poles(game.poles[i], game.player)

    return game
```
- Because ```update_poles()``` now takes the player as a second argument, we also need to update ```update_pole_array()```, as it calls ```update_poles()```.

### Addition Nine
```python
def update_player(player):
    update_velocity(player)
    update_sprite(player.sprite_data)
```
- ```update_player()``` previously took a sprite as an argument, but due to our changes to the way the player is stored, it now needs to take a ```player_data```. Additionally, ```update_velocity()``` and ```update_sprite()``` still take sprites as arguments, so we need to append ```.sprite_data``` to the end of ```player```.

#### Addition Ten
```python
def check_for_collisions(game):
    if sprite_collision(game.player.sprite_data, game.scene.foreground) or sprite_collision(game.player.sprite_data, game.scene.foreroof):
        game.player.is_dead = True

    for pole in game.poles:
        if sprite_collision(game.player.sprite_data, pole.up_pole) or sprite_collision(game.player.sprite_data, pole.down_pole):
            game.player.is_dead = True

    return game
```
- We've got a new procedure called ```check_for_collisions()```. The role of this procedure is to check to see if the player has collided with any of the eligible game elements (the poles, the roof and the floor). If the player does collide with anything that it shouldn't, we set the player's ```is_dead``` field to ```true```.

#### Addition Eleven
```python
def reset_player(player):
    free_sprite(player.sprite_data)
    player = get_new_player()
    return player
```
- Another new procedure called ```reset_player()``` has been added to reset the player to a default state. When we say default state, we mean a new game where the score is zero and the player has to start over. This procedure is only used when the player dies (collides with the environment).

#### Addition Twelve
```python
def reset_game(game):
    game.player = reset_player(game.player)
    for i in range(len(game.poles)):
        game.poles[i] = reset_pole_data(game.poles[i])

    return game
```
- A procedure called ```reset_game()``` has been added to reset the game to the default state. This procedure is only used when the player dies.

#### Addition Thirteen
```python
def update_game(game):
    if not game.player.is_dead:
        game = check_for_collisions(game)
        process_events()
        handle_input(game.player)
        game = update_pole_array(game)
        update_player(game.player)
        update_scene(game.scene)
    else:
        game = reset_game(game)

    return game
```
- The procedure ```update_game()``` has changed in order to act upon the player's death. So, as long as the player is not dead, we want the game to run normally, with poles scrolling across the screen that the player has to avoid. If the player has died, ```update_game()``` knows when that happens and will reset the game. Notice that because we changed ```update_pole_array()```, it now needs a second argument.

#### Addition Fourteen
```python
def draw_game(game):
    draw_sprite(game.scene.background)
    draw_pole_array(game.poles)
    draw_sprite(game.player.sprite_data)
    draw_sprite(game.scene.foreground)
    draw_sprite(game.scene.foreroof)

    draw_text_font_as_string(str(game.player.score), color_white(), "GameFont", 21, 10, 0)
```

- ```draw_game()``` has changed to simply draw the score to the top left of the screen so that we can see how good (or bad!) we are at playing the game. The function ```sprintf()``` is actually a standard C function, not a function that comes with SplashKit. For this reason, we need to add a line at the top of the code, just below ```#include <splashkit.h>```. The line to add is ```#include <cstdio>```. It looks very similar to the previous line, but instead of including SplashKit, we're including cstdio, which stands for C Standard Input/Output. Notice also that there's no ```.h``` at the end of the filename, because it is a standard C library, not a library that somebody else has written, like SplashKit.

#### Addition Fifteen
```python
def get_new_game():
    load_resource_bundle("CaveEscape", "cave_escape.txt")

    resultScene = get_new_scene()
    resultPoles = [get_random_poles() for i in range(NUM_POLES)]
    resultPlayer = get_new_player()

    return game_data(resultScene, resultPoles, resultPlayer)
```
- Finally, we'll add a single line to ```get_new_game()``` that will play some background music.

### You're the Same, Main
Main has not changed.

### Have a Crack
Now it's time for you to have a go at implementing iteration nine on your own.

### Complete Code
The complete code for iteration nine can be found [here](https://raw.githubusercontent.com/itco-education/cave-escape/master/python/iteration_9.py).
