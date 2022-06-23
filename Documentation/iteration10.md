__Iteration ten is the final iteration for the game! In this final iteration we will add a menu to the game so that it only starts when the player is ready.__

## Iteration ten will look like:
![Iteration Ten](https://raw.githubusercontent.com/itco-education/cave-escape/master/Documentation/Images/iteration_10.gif)

## Code

### New Code
The new code in iteration ten is as follows:

#### Addition One
```cpp
enum player_state
{
	MENU,
	PLAY
};
```
- We've added an enumeration called ```player_state``` with two values; ```MENU``` and ```PLAY```. This enumeration is going to be used to help the game determine whether or not to show the menu or to let the player play.

#### Addition Two
```cpp    
typedef struct player_data
{
	player_state state;
	sprite sprite_data;
	bool is_dead;
	int score;
} player_data;
```
-  Now because of the addition of the enumeration ```player_state```, we've changed the ```player_data``` struct to house the current game state. The new field is called ```state```.

#### Addition Three
```cpp
player_data get_new_player()
{
	player_data result;

	result.sprite_data = create_sprite(bitmap_named("Player"), animation_script_named("PlayerAnimations"));

	sprite_set_x(result.sprite_data, (screen_width() / 2) - sprite_width(result.sprite_data));
	sprite_set_y(result.sprite_data, screen_height() / 2);
	sprite_start_animation(result.sprite_data, "Fly");

	result.score = 0;
	result.is_dead = false;
	result.state = MENU;

	return result;
}
```
- The function ```get_new_player()``` has changed to set the value of the players's new field ```state``` to ```MENU```. This way, we can ensure that the game starts in the menu state.

#### Addition Four
```cpp
void handle_input(player_data &player)
{
	if (key_typed(SPACE_KEY))
	{
		if (player.state == PLAY)
		{
			sprite_set_dy(player.sprite_data, sprite_dy(player.sprite_data) - JUMP_RECOVERY_BOOST);
		}
		else
		{
			player.state = PLAY;
		}
	}
}
```
- The procedure ```handle_input()``` has changed to accommodate the implementation of the new menu state Basically, the change ensures that ```if``` the game hasn't started yet (the player's ```state``` is ```MENU```) and the player presses the space bar, we want to set the players's ```state``` to ```PLAY```. If the player is already playing, then just handle the input like we normally would by boosting the player's velocity.

#### Addition Five
```cpp
void update_player(player_data &player)
{
	if (player.state == PLAY)
	{
		update_velocity(player.sprite_data);
	}

	update_sprite(player.sprite_data);
}
```
- ```update_player()``` has also changed to suit the new menu state. The changes made ensure that we only update the player's velocity ```if``` the current ```state``` is set to ```PLAY```. Otherwise, the player will just hover in the middle of the screen. We're doing this so that the player only starts moving when we are ready to play!

#### Addition Six
```cpp
void update_game(game_data &game)
{
	if (!game.player.is_dead)
	{
		check_for_collisions(game);
		handle_input(game.player);
		update_scene(game.scene);
		update_player(game.player);

		if (game.player.state == PLAY)
		{
			update_pole_array(game.poles, game.player);
		}
	}
	else
	{
		reset_game(game);
	}
}
```
- The procedure ```update_game()``` also has a change to suit the menu state. The changes ensure that the poles only scroll across the screen if the player has started playing the game.

#### Addition Seven
```cpp
void draw_game(game_data &game)
{
	char str[15];

	sprintf(str, "%d", game.player.score);

	draw_sprite(game.scene.background);
	draw_pole_array(game.poles);
	draw_sprite(game.scene.foreroof);
	draw_sprite(game.scene.foreground);
	draw_sprite(game.player.sprite_data);

	if (game.player.state == PLAY)
	{
		draw_text(str, COLOR_WHITE, "GameFont", 21, 10, 0);
	}
	else
	{
		draw_bitmap(bitmap_named("Logo"), 0, 40);
		draw_text("PRESS SPACE!", COLOR_WHITE, "GameFont", 21, 55, 550);
	}
}
```
- Finally, ```draw_game()``` also has some minor changes. This is where we're drawing our new menu. So, ```if``` the player is not playing the game yet, we draw a menu to the screen for them, giving them instructions on how to start playing.

### Main Remains the Same
It really does.

### Have a Crack
Now it's time for you to have a go at implementing iteration ten on your own. You've done really well and you're pretty much done!

### Complete Code
The complete code for iteration ten can be found [here](https://raw.githubusercontent.com/itco-education/cave-escape/master/CPP/cave_escape_10.cpp).
