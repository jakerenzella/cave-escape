**In the second iteration of *Cave Escape*, you will implement the functionality to have your game draw a player character to the screen. The player will be drawn to the centre of the graphics window and come complete with an animation!**

## Iteration Two will look like:
![Iteration Two](https://raw.githubusercontent.com/itco-education/cave-escape/master/Documentation/Images/iteration_2.gif)

## Code

### New Code
The new code in iteration two is as follows:

#### Addition One
```cpp
sprite get_new_player()
{
	sprite result = create_sprite(bitmap_named("Player"), animation_script_named("PlayerAnimations"));

	sprite_set_x(result, (screen_width() / 2) - sprite_width(result));
	sprite_set_y(result, screen_height() / 2);
	sprite_start_animation(result, "Fly");

	return result;
}
```
- The ```get_new_player()``` function, as demonstrated in the code above, is used to generate the data associated with the player entity that we'll be using in our game. It's important to note that the function uses a variable called ```result``` to store the value that is calculated. So, in short, the function is creating a sprite for the player, setting the sprite's location to the centre of the screen and then setting an animation for the sprite. Once the function finishes, it returns the sprite it creates (the ```result``` variable).

### You've Changed, Main
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

Take a close look at the ```main()``` procedure. A few things have changed in order to cater for our new ```get_new_player()``` function, as well as drawing our player to the screen. The sprite that the function ```get_new_player()``` returns is assigned to a variable called ```player```, and then within the game loop, the ```player``` sprite variable is updated and drawn.

### Have a Crack
Now it's time for you to have a go at implementing iteration two on your own. As before, you'll have to type the instructions above into your text editor. Continue to try and resist the urge to copy and paste code if it arises, as typing it out helps to build your understanding of what the code is doing. When you're done, you'll need to build and run your code to see if it works. If you encounter any build errors, you'll have to resolve those, then build and run the game again.

### Complete Code
The complete code for iteration two can be found [here](https://raw.githubusercontent.com/itco-education/cave-escape/master/CPP/cave_escape_2.cpp).
