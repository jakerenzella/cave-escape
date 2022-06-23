__In the fifth iteration of *Cave Escape*, we add quite a bit of functionality; more so than in the previous iterations. We're making a big step with this one. We're going to add an obstacle, and we'll refer to the obstacle as a set of poles. It's the aim of the game to avoid the poles, but we'll worry about that later. For now, let's just worry about getting the poles onto the screen. So, this iteration concerns the generation of a single set of poles as well as the way the poles behave.__

## Iteration Five will look like:
![Iteration Five](https://raw.githubusercontent.com/itco-education/cave-escape/master/Documentation/Images/iteration_5.gif)

## Code

### New Code
The new code in iteration five is as follows:

#### Addition One
```cpp
const float GRAVITY = 0.08f;
const int MAX_SPEED = 5;
const int JUMP_RECOVERY_BOOST = 2;
const int FOREGROUND_SCROLL_SPEED = -2;
```
- The poles that we're adding to the game will move horizontally across the screen, from left to right. In order to cater for this, we've added another constant called ```FOREGROUND_SCROLL_SPEED``` in order to keep track of the speed at which the poles travel across the screen.

#### Addition Two
```cpp    
struct pole_data
{
	bool score_limiter;
	sprite up_pole;
	sprite down_pole;
};
```
- In order to be able to keep track of the data required to add the poles to the game, we've added a struct called ```pole_data```. If you take a look at the ```pole_data``` struct, you'll notice that it has two fields as sprites, ```up_pole``` and ```down_pole```. The ```pole_data``` struct needs two sprites because one pole will come up from the bottom of the screen and the other will come down from the top.

#### Addition Three
```cpp    
pole_data get_random_poles()
{
	pole_data result;

	result.up_pole = create_sprite(bitmap_named("UpPole"));
	result.down_pole = create_sprite(bitmap_named("DownPole"));

	sprite_set_x(result.up_pole, screen_width() + rnd(1200));
	sprite_set_y(result.up_pole, screen_height() - sprite_height(result.up_pole));

	sprite_set_x(result.down_pole, sprite_x(result.up_pole));
	sprite_set_y(result.down_pole, 0);

	sprite_set_dx(result.up_pole, FOREGROUND_SCROLL_SPEED);
	sprite_set_dx(result.down_pole, FOREGROUND_SCROLL_SPEED);

	return result;
}
```
- Now, we need some logic in order to be able to add the poles to the game so that we can see them. So to start that off, we've got a new function called ```get_random_poles()```, which is responsible for generating the data associated with the poles. This function behaves similarly to the function ```get_new_player()```, as discussed in iteration two. ```get_random_poles()``` assigns the top and bottom poles their own sprites, sets their x location to a random location off the far right of the screen (this is intentional because we want to see the poles scroll onto the screen from the right) and sets their y locations so that they appear to be coming down from the top and up from the bottom of the screen. Finally, the function assigns their delta x, or horizontal movement speed to that of the value of the constant ```FOREGROUND_SCROLL_SPEED```.

#### Addition Four
```cpp
void update_poles(pole_data &poles)
{
	update_sprite(poles.up_pole);
	update_sprite(poles.down_pole);
}
```
- A procedure called ```update_poles()``` has been added to update the poles.

#### Addition Five
```cpp
void draw_poles(pole_data &poles)
{
	draw_sprite(poles.up_pole);
	draw_sprite(poles.down_pole);
}
```
- A procedure called ```draw_poles()``` has been added to draw the poles to the screen.

### More Changes to Main
```cpp
int main()
{
	// Initialisation
	open_window("Cave Escape", 432, 768);
	load_resource_bundle("CaveEscape", "cave_escape.txt");

	pole_data game_poles = get_random_poles();
	sprite player = get_new_player();

	do
	{
		// Update
		process_events();
		handle_input(player);
		update_poles(game_poles);
		update_velocity(player);
		update_sprite(player);

		// Pre-Draw
		clear_screen(COLOR_WHITE);

		// Draw
		draw_poles(game_poles);
		draw_sprite(player);

		// Post-Draw
		refresh_screen();
	} while (!window_close_requested("Cave Escape"));

	// Cleanup
	free_resource_bundle("CaveEscape");
	close_window("Cave Escape");

	return 0;
}
```
The ```main()``` procedure has now changed. Notice that we're now using our new function ```get_random_poles()``` and assigning the value it returns to a variable called ```game_poles```. In order to move the poles across the screen and draw them, we've added the calls to the procedures ```update_poles()``` and ```draw_poles()``` within the game loop.

### Have a Crack
Now it's time for you to have a go at implementing iteration five on your own.

### Complete Code
The complete code for iteration five can be found [here](https://raw.githubusercontent.com/itco-education/cave-escape/master/CPP/cave_escape_5.cpp).
