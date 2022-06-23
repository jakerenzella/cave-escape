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
