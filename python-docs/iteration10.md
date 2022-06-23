__Iteration ten is the final iteration for the game! In this final iteration we will add a menu to the game so that it only starts when the player is ready.__

## Iteration ten will look like:
![Iteration Ten](https://raw.githubusercontent.com/itco-education/cave-escape/master/Documentation/Images/iteration_10.gif)

## Code

### New Code
The new code in iteration ten is as follows:

#### Addition One
```python
class player_state(Enum):
    MENU = 1
    PLAY = 2
```
- We've added an enumeration called ```player_state``` with two values; ```MENU``` and ```PLAY```. This enumeration is going to be used to help the game determine whether or not to show the menu or to let the player play.

#### Addition Two
```python
class player_data:
    def __init__(self, _sprite_data, _score, _is_dead, _state):
        self.sprite_data = _sprite_data
        self.score = _score
        self.is_dead = _is_dead
        self.state = _state
```
-  Now because of the addition of the enumeration ```player_state```, we've changed the ```player_data``` class to house the current game state. The new field is called ```state```.

#### Addition Three
```python
def get_new_player():
    resultSpriteData = create_sprite_with_bitmap_and_animation_named("Player", "PlayerAnimations")

    sprite_set_x(resultSpriteData, (screen_width() / 2) - sprite_width(resultSpriteData))
    sprite_set_y(resultSpriteData, screen_width() / 2)
    sprite_start_animation_named(resultSpriteData, "Fly")

    resultScore = 0
    resultIsDead = False
    resultState = player_state.MENU

    return player_data(resultSpriteData, resultScore, resultIsDead, resultState)
```
- The function ```get_new_player()``` has changed to set the value of the players's new field ```state``` to ```MENU```. This way, we can ensure that the game starts in the menu state.

#### Addition Four
```python
def handle_input(player):
    if key_typed(KeyCode.space_key):
        if player.state == player_state.PLAY:
            sprite_set_dy(player.sprite_data, sprite_dy(player.sprite_data) - JUMP_RECOVERY_BOOST)
        else:
            player.state = player_state.PLAY
```
- The procedure ```handle_input()``` has changed to accommodate the implementation of the new menu state Basically, the change ensures that ```if``` the game hasn't started yet (the player's ```state``` is ```MENU```) and the player presses the space bar, we want to set the players's ```state``` to ```PLAY```. If the player is already playing, then just handle the input like we normally would by boosting the player's velocity.

#### Addition Five
```python
def update_player(player):
    if player.state == player_state.PLAY:
        update_velocity(player)

    update_sprite(player.sprite_data)
```
- ```update_player()``` has also changed to suit the new menu state. The changes made ensure that we only update the player's velocity ```if``` the current ```state``` is set to ```PLAY```. Otherwise, the player will just hover in the middle of the screen. We're doing this so that the player only starts moving when we are ready to play!

#### Addition Six
```python
def update_game(game):
    if not game.player.is_dead:
        game = check_for_collisions(game)
        process_events()
        handle_input(game.player)
        update_player(game.player)
        update_scene(game.scene)

        if game.player.state == player_state.PLAY:
            game = update_pole_array(game)

    else:
        game = reset_game(game)

    return game
```
- The procedure ```update_game()``` also has a change to suit the menu state. The changes ensure that the poles only scroll across the screen if the player has started playing the game.

#### Addition Seven
```python
def draw_game(game):
    draw_sprite(game.scene.background)
    draw_pole_array(game.poles)
    draw_sprite(game.player.sprite_data)
    draw_sprite(game.scene.foreground)
    draw_sprite(game.scene.foreroof)

    if game.player.state == player_state.PLAY:
        draw_text_font_as_string(str(game.player.score), color_white(), "GameFont", 21, 10, 0)
    else:
        draw_bitmap_named("Logo", 0, 40)
        draw_text_font_as_string("PRESS SPACE!", color_white(), "GameFont", 21, 55, 550)

```
- Finally, ```draw_game()``` also has some minor changes. This is where we're drawing our new menu. So, ```if``` the player is not playing the game yet, we draw a menu to the screen for them, giving them instructions on how to start playing.

### Main Remains the Same
It really does.

### Have a Crack
Now it's time for you to have a go at implementing iteration ten on your own. You've done really well and you're pretty much done!

### Complete Code
The complete code for iteration ten can be found [here](https://raw.githubusercontent.com/itco-education/cave-escape/master/python/iteration_10.py).
