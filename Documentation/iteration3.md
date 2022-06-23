__In the third iteration of *Cave Escape*, you will implement the functionality to give your player the ability to fly! Well, almost. You're going to add some velocity to the player so that it's not just stuck in the middle of the screen. Instead, when you're finished, the player will fall right off the bottom of the screen!__

## Iteration Three will look like:
![Iteration Three](https://raw.githubusercontent.com/itco-education/cave-escape/master/Documentation/Images/iteration_3.gif)

## Code

### New Code
The new code in iteration three is as follows:

#### Addition One
```cpp
const float GRAVITY = 0.08f;
const int MAX_SPEED = 5;
```
- We've taken the time to add some constant values that are going to be used in the calculation of the player's velocity. Those values represent an imposed ```GRAVITY``` and a ```MAX_SPEED``` in regards to what we want to impose as the maximum velocity the player can move, or fall at.

#### Addition Two
```cpp
void update_velocity(sprite player)
{
	sprite_set_dy(player, sprite_dy(player) + GRAVITY);

	if (sprite_dy(player) > MAX_SPEED)
	{
		sprite_set_dy(player, MAX_SPEED);
	}
	else if (sprite_dy(player) < -MAX_SPEED)
	{
		sprite_set_dy(player, -MAX_SPEED);
	}
}
```
- The ```update_velocity()``` procedure, as demonstrated in the code above, uses these two new constant values to determine what the player's speed will be by using conditional statements. The conditional statements ensure that ```if``` the player is not already falling at the ```MAX_SPEED```, increase its velocity, ```else if``` the player is already falling at the ```MAX_SPEED```, ensure that it stays falling at the ```MAX_SPEED``` rather than going any faster.

### Take a Look at Main
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

The ```main()``` procedure has now changed. Notice that in the game loop, there's now a call to the new procedure ```update_velocity()```. This ensures that for each time the game loop executes, we're ensuring that we're updating the player's velocity accordingly.

### Have a Crack
Now it's time for you to have a go at implementing iteration three on your own. Give it a crack and see how you go.

### Complete Code
The complete code for iteration three can be found [here](https://raw.githubusercontent.com/itco-education/cave-escape/master/CPP/cave_escape_3.cpp).
