__In iteration seven of *Cave Escape*, we're going to implement the logic to have more than one set of poles. One set of poles is simply not challenging enough, and the overall change in logic to suit such functionality is quite minor.__

## Iteration Seven will look like:
![Iteration Seven](https://raw.githubusercontent.com/itco-education/cave-escape/master/Documentation/Images/iteration_7.gif)

## Code

### New Code
The new code in iteration seven is as follows:

#### Addition One
```cpp
const float GRAVITY = 0.08f;
const int MAX_SPEED = 5;
const int JUMP_RECOVERY_BOOST = 2;
const int FOREGROUND_SCROLL_SPEED = -2;
const int NUM_POLES = 4;
```
- We've added a constant called ```NUM_POLES``` to store the number of sets of poles we want in the game. The code provided has ```NUM_POLES``` being equal to the value of four, so this means there will be exactly four sets of poles in the game.

#### Addition Two
```cpp
typedef struct pole_data poles[NUM_POLES];
```
- The second addition is an array of ```pole_data``` called ```poles```. This array is where our four sets of poles will be stored. You can see the array is declared as ```typedef struct pole_data poles[NUM_POLES];```. It's important to understand the logic in the square braces ```[NUM_POLES]```. Now, ```NUM_POLES``` is four and computers are zero based, meaning that our first set of poles is actually denoted by the numerical value of zero, the second set is denoted one, the third set two and the fourth set three!

#### Addition Three
```cpp
void update_pole_array(pole_data pole_array[])
{
	for (int i = 0; i < NUM_POLES; ++i)
	{
		update_poles(pole_array[i]);
	}
}
```
- We've added a procedure called ```update_pole_array()``` in order to update every single set of poles in the array. Notice how the procedure simply uses a ```for``` loop in order to call the procedure ```update_poles()``` on each set of poles in the array. We added this procedure because we know that the procedure ```update_poles()``` works with a single set of poles, so why not just call it for each set of poles in the array?

#### Addition Four
```cpp
void draw_pole_array(pole_data pole_array[])
{
	for (int i = 0; i < NUM_POLES; ++i)
	{
		draw_poles(pole_array[i]);
	}
}
```
-  We've added a procedure called ```draw_pole_array()``` in order to draw every single set of poles in the array. Notice how exactly like the procedure ```update_pole_array()```, ```draw_pole_array()``` simply uses a ```for``` loop, within which a call to the procedure ```draw_poles()``` is made for each set of poles in the array. We added this procedure because we know that the procedure ```draw_poles()``` works with a single set of poles, so why not just call it for each set of poles in the array?

### Any Changes to Main
```cpp
int main()
{
	// Initialisation
	open_window("Cave Escape", 432, 768);
	load_resource_bundle("CaveEscape", "cave_escape.txt");

	pole_data game_poles[NUM_POLES];

	for (int i = 0; i < NUM_POLES; ++i)
	{
		game_poles[i] = get_random_poles();
	}

	sprite player = get_new_player();

	do
	{
		// Update
		process_events();
		handle_input(player);
		update_pole_array(game_poles);
		update_velocity(player);
		update_sprite(player);

		// Pre-Draw
		clear_screen(COLOR_WHITE);

		// Draw
		draw_pole_array(game_poles);
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
Instead of the variable ```game_poles``` being a value of ```pole_data```, it is now a value of our array, ```poles```. We've also added a ```for``` loop to ensure that we set up all of the poles for the game. Our two new procedures to update and draw the array of poles, ```update_pole_array()``` and ```draw_pole_array()``` are also being called!

### Have a Crack
Now it's time for you to have a go at implementing iteration seven on your own.

### Complete Code
The complete code for iteration seven can be found [here](https://raw.githubusercontent.com/itco-education/cave-escape/master/CPP/cave_escape_7.cpp).
