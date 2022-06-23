__Iteration nine is going to be quite a big one too, where there are some big changes to improve gameplay in order to make our game...more of a game. In this iteration, we're going to add some music to give the game its own little soundtrack, which will make the experience more immersive. The big changes, on top of the music, are the addition of collisions, so the player can collide with the environment, a scoring system and the ability to have the game reset if the player does collide with the environment. Iteration nine very nearly implements a completely functional game, ready for shipping.__

## Iteration nine will look like:
![Iteration Nine](https://raw.githubusercontent.com/itco-education/cave-escape/master/Documentation/Images/iteration_9.gif)

## Code

### New Code
The new code in iteration nine is as follows:

#### Addition One
```cpp
struct pole_data
{
	bool score_limiter;
	sprite up_pole;
	sprite down_pole;
};
```
- You may have been wondering what the bool ```score_limiter``` in ```pole_data``` is for. Well, it finally has a use in this iteration! We need this to be able to make the scoring system work. We'll talk more about it soon. Promise.

#### Addition Two
```cpp    
typedef struct player_data
{
	sprite sprite_data;
	int score;
	bool is_dead;
} player_data;
```
- We've added a new struct called ```player_data```. Our player can no longer just be a sprite. If you take a look at the struct, you'll notice it has three fields. The first of which is our player sprite. The next being the ```score``` and the third being a field called ```is_dead```. We need this field to tell the game when the player dies from colliding with the environment.

#### Addition Three
```cpp    
typedef struct game_data
{
	scene_data scene;
	pole_data poles[NUM_POLES];
	player_data player;
} game_data;
```
- The ```game_data``` struct has changed only slightly. Instead of the ```player``` field being a sprite, it is now a value of our new struct ```player_data```.

#### Addition Four
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

	return result;
}
```
- Our function ```get_new_player()``` has had to change in order to support the new scoring system as well as our collision system. In the function, we now set the ```score``` to zero and set the player to be alive when the function is called (```result.is_dead = false```). It also now returns ```player_data``` instead of ```sprite```.

#### Addition Five
```cpp
pole_data get_random_poles()
{
	pole_data result;

	result.up_pole = create_sprite(bitmap_named("UpPole"));
	result.down_pole = create_sprite(bitmap_named("DownPole"));

	sprite_set_x(result.up_pole, screen_width() + rnd(1200));
	sprite_set_y(result.up_pole, screen_height() - sprite_height(result.up_pole) - rnd(bitmap_height(bitmap_named("Foreground"))) + 1);

	sprite_set_x(result.down_pole, sprite_x(result.up_pole));
	sprite_set_y(result.down_pole, rnd(bitmap_height(bitmap_named("Foreroof"))) + 1);

	sprite_set_dx(result.up_pole, FOREGROUND_SCROLL_SPEED);
	sprite_set_dx(result.down_pole, FOREGROUND_SCROLL_SPEED);

	result.score_limiter = true;

	return result;
}
```
- The ```get_random_poles()``` function has also changed. Only slightly, though. Notice that the function now sets the ```pole_data``` value that it returns to have a ```score_limiter``` value of ```true```. Additionally, the positioning of the poles in terms of their vertical position is random. Because we have the roof and the floor, we can position the poles more dynamically. Now, we're going to use the ```score_limiter``` to increment the score of the player every time they pass a set of poles. Once they pass a set of poles, the player's score will be incremented and the ```score_limiter``` for that set of poles will be set to ```false```. The reasoning behind this will become more clear when we talk about the changes made to ```update_poles()```.

#### Addition Six
```cpp
void handle_input(player_data &player)
{
    if (key_typed(SPACE_KEY))
    {
        sprite_set_dy(player.sprite_data, sprite_dy(player.sprite_data) - JUMP_RECOVERY_BOOST);
    }
}
```
- ```handle_input()``` previously took a sprite as an argument, but due to our changes to the way the player is stored, it now needs to take a ```player_data```. We also need to append ```.sprite_data``` to the end of ```player```, as ```player``` is now a ```player_data```, not a ```sprite```.

#### Addition Seven
```cpp
void update_poles(pole_data &poles, player_data &player)
{
	update_sprite(poles.up_pole);
	update_sprite(poles.down_pole);

	if ((sprite_x(poles.up_pole) < sprite_x(player.sprite_data)) && poles.score_limiter)
	{
		poles.score_limiter = false;
		++player.score;
	}

	if ((sprite_x(poles.up_pole) + sprite_width(poles.up_pole)) < 0)
	{
		reset_pole_data(poles);
	}
}
```
- Now we're going to take a look at the changes made to ```update_poles()```. Take a close look at the conditional statements in this procedure. In particular, let's focus on this conditional section of code here ```if ((sprite_x(poles.up_pole) < sprite_x(player.sprite_data)) && poles.score_limiter)``` to understand why we need the ```score_limiter```. We're checking to see ```if``` the player has passed any poles and ```if``` the ```score_limiter``` is ```true```. If those conditions are ```true```, we then set the ```score_limiter``` field  to ```false``` and increment the player's ```score```. Now, ```score_limiter``` has to change to ```false``` because, if it never did, once the player passes some poles, the ```if``` statement would evaluate to ```true``` and the player's score would keep incrementing because the player would be beyond the poles. Phew. Tongue twisting. The best way to see the bug that this would cause is to remove this condition ```poles.score_limiter``` from the ```if``` statement.

#### Addition Eight
```cpp
void update_pole_array(pole_data pole_array[], player_data &player)
{
    for (int i = 0; i < NUM_POLES; ++i)
    {
        update_poles(pole_array[i], player);
    }
}
```
- Because ```update_poles()``` now takes the player as a second argument, we also need to update ```update_pole_array()```, as it calls ```update_poles()```.

### Addition Nine
```cpp
void update_player(player_data &player)
{
    update_velocity(player.sprite_data);
    update_sprite(player.sprite_data);
}
```
- ```update_player()``` previously took a sprite as an argument, but due to our changes to the way the player is stored, it now needs to take a ```player_data```. Additionally, ```update_velocity()``` and ```update_sprite()``` still take sprites as arguments, so we need to append ```.sprite_data``` to the end of ```player```.

#### Addition Ten
```cpp
void check_for_collisions(game_data &game)
{
	if (sprite_collision(game.player.sprite_data, game.scene.foreground) ||
		sprite_collision(game.player.sprite_data, game.scene.foreroof))
	{
		game.player.is_dead = true;

		return;
	}

	for (int i = 0; i < NUM_POLES; ++i)
	{
		if (sprite_collision(game.player.sprite_data, game.poles[i].up_pole) ||
			sprite_collision(game.player.sprite_data, game.poles[i].down_pole))
		{
			game.player.is_dead = true;

			return;
		}
	}
}
```
- We've got a new procedure called ```check_for_collisions()```. The role of this procedure is to check to see if the player has collided with any of the eligible game elements (the poles, the roof and the floor). If the player does collide with anything that it shouldn't, we set the player's ```is_dead``` field to ```true```.

#### Addition Eleven
```cpp
void reset_player(player_data &player)
{
	free_sprite(player.sprite_data);

	player = get_new_player();
}
```
- Another new procedure called ```reset_player()``` has been added to reset the player to a default state. When we say default state, we mean a new game where the score is zero and the player has to start over. This procedure is only used when the player dies (collides with the environment).

#### Addition Twelve
```cpp
void reset_game(game_data &game)
{
	reset_player(game.player);

	for (int i = 0; i < NUM_POLES; ++i)
	{
		reset_pole_data(game.poles[i]);
	}
}
```
- A procedure called ```reset_game()``` has been added to reset the game to the default state. This procedure is only used when the player dies.

#### Addition Thirteen
```cpp
void update_game(game_data &game)
{
	if (!game.player.is_dead)
	{
		check_for_collisions(game);
		handle_input(game.player);
		update_scene(game.scene);
		update_pole_array(game.poles, game.player);
		update_player(game.player);
	}
	else
	{
		reset_game(game);
	}
}
```
- The procedure ```update_game()``` has changed in order to act upon the player's death. So, as long as the player is not dead, we want the game to run normally, with poles scrolling across the screen that the player has to avoid. If the player has died, ```update_game()``` knows when that happens and will reset the game. Notice that because we changed ```update_pole_array()```, it now needs a second argument.

#### Addition Fourteen
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
	draw_text(str, COLOR_WHITE, "GameFont", 21, 10, 0);
}
```
- ```draw_game()``` has changed to simply draw the score to the top left of the screen so that we can see how good (or bad!) we are at playing the game. The function ```sprintf()``` is actually a standard C function, not a function that comes with SplashKit. For this reason, we need to add a line at the top of the code, just below ```#include <splashkit.h>```. The line to add is ```#include <cstdio>```. It looks very similar to the previous line, but instead of including SplashKit, we're including cstdio, which stands for C Standard Input/Output. Notice also that there's no ```.h``` at the end of the filename, because it is a standard C library, not a library that somebody else has written, like SplashKit.

#### Addition Fifteen
```cpp
game_data set_up_game()
{
	game_data result;

	load_resource_bundle("CaveEscape", "cave_escape.txt");

	result.scene = get_new_scene();

	for (int i = 0; i < NUM_POLES; ++i)
	{
		result.poles[i] = get_random_poles();
	}

	result.player = get_new_player();

	fade_music_in("GameMusic", -1, 15000);

	return result;
}
```
- Finally, we'll add a single line to ```set_up_game()``` that will play some background music.

### You're the Same, Main
Main has not changed.

### Have a Crack
Now it's time for you to have a go at implementing iteration nine on your own.

### Complete Code
The complete code for iteration nine can be found [here](https://raw.githubusercontent.com/itco-education/cave-escape/master/CPP/cave_escape_9.cpp).
