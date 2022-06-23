**In the first iteration of *Cave Escape*, you will implement the boiler plate code for a simple game. The boiler plate code includes the instructions to open a graphics window and the execution of a basic game loop, where all of the instructions that you implement will be called from.**

* The term *boiler plate code* is used to describe code that almost all programs will need - common code.

## Step 0
[Download the resources for Cave-Escape](https://github.com/itco-education/cave-escape/releases/download/resources/Resources.zip)

## Iteration One will look like:

![Iteration One](https://raw.githubusercontent.com/itco-education/cave-escape/master/Documentation/Images/iteration_1.png)

## Code

### Complete Code
The complete code for iteration one is as follows:


```cpp
#include <splashkit.h>

int main()
{
	// Initialisation
	open_window("Cave Escape", 432, 768);

	do
	{
		// Update
		process_events();

		// Pre-Draw
		clear_screen(COLOR_WHITE);

		// Post-Draw
		refresh_screen();
	} while (!window_close_requested("Cave Escape"));

	// Cleanup
	close_window("Cave Escape");

	return 0;
}
```

### How It Works
In C++, the ```main()``` function is always the entry point of a program - meaning that the program will start executing in main.

In the code above, *main* is responsible for executing all of the instructions required for our game to run. The instructions are executed in sequence, meaning that the code within the ```main()``` procedure will be executed in the exact order in which it is specified.

So, that being said, let's take a moment to analyse the ```main()``` procedure and the instructions it is executing. The sequence is as follows:

  1. Firstly, a call to ```open_window()``` is made, where we can see that the title of the window being opened is **Cave Escape**, and the width and height of the window is 432 by 768 pixels.
  2. Next, we enter the game loop. The game loop will loop over and over until the user closes the window, meaning that all of the instructions will be continually executed for as long as the loop is running. Note that the condition of the loop is ```window_close_requested()```.

	The following instructions are executed within the game loop:
      1. ```process_events()``` is called. ```process_events()``` is used to listen for any user input made while the game is running.
      2. We then clear the screen with ```clear_screen()``` before we draw anything to it (we're not drawing anything in this iteration, but that will come soon!)
      3. We then refresh the screen with ```refresh_screen()``` so that we can see what we've drawn.

### Have a Crack
Now it's time for you to have a go at implementing iteration one on your own. You'll have to type the instructions above into your text editor. Try and resist the urge to copy and paste code if it arises, as typing it out helps to build your understanding of what the code is doing. When you're done, you'll need to build and run your code to see if it works. If you encounter any build errors, you'll have to resolve those, then build and run the game again.
