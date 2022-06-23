__In the fourth iteration of **Cave Escape**, we will actually implement the ability to have you control the way the player flies. Instead of the player just falling into the abyss, as it was in iteration three, iteration four sees the inclusion of the logic required to keep the player on the screen by using keyboard input. In particular, we're going to make it so that every time the space bar is pressed, the player is going to fly a little higher, and further away from the bottom of the screen.__

## Iteration Four will look like:
![Iteration Four](https://raw.githubusercontent.com/itco-education/cave-escape/master/Documentation/Images/iteration_4.gif)

## Code

### New Code
The new code in iteration four is as follows:

#### Addition One
```cpp
const float GRAVITY = 0.08f;
const int MAX_SPEED = 5;
const int JUMP_RECOVERY_BOOST = 2;
```
- In order to be able to control the player's velocity with user input, we've had to add a new constant value called ```JUMP_RECOVERY_BOOST```. The reason for this will become more clear when we talk about the new procedure ```handle_input()```.

#### Addition Two
```cpp
void handle_input(sprite player)
{
	if (key_typed(SPACE_KEY))
	{
		sprite_set_dy(player, sprite_dy(player) - JUMP_RECOVERY_BOOST);
	}
}
```
- The new procedure ```handle_input()``` is implemented to listen for user input while the game is running. Specifically, the input that it listens for is when the space bar is pressed. Every time the space bar is pressed, the ```handle_input()``` procedure will decrement the value of the constant ```JUMP_RECOVERY_BOOST``` from the player's current velocity. This means that each time the space bar is pressed, the player will fall a little slower, but only briefly. The aim is to have the user continually press the space bar to keep the player on the screen and give it the effect of flying!

### Main Has Changed, Again
```cpp
int main()
{
	// Initialisation
	open_window("Cave Escape", 432, 768);
	load_resource_bundle("CaveEscape", "cave_escape.txt");

	sprite player = get_new_player();

	do
	{
		// Update
		process_events();
		handle_input(player);
		update_velocity(player);
		update_sprite(player);

		// Pre-Draw
		clear_screen(COLOR_WHITE);

		// Draw
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

The ```main()``` procedure has now changed. Notice that in the game loop, there's now a call to the new procedure ```handle_input()```. This ensures that for each time the game loop executes, we're ensuring that we're listening for any user input, specifically, if the space bar has been pressed. Now we have a more functional game where the user finally has some control over the way the game behaves.

### Have a Crack
Now it's time for you to have a go at implementing iteration four on your own.

### Complete Code
The complete code for iteration four can be found [here](https://raw.githubusercontent.com/itco-education/cave-escape/master/CPP/cave_escape_4.cpp).
