from splashkit import *

def main():
    open_window("Cave Escape", 432, 768)
    while not window_close_requested_named("Cave Escape"):
        # Update
        process_events()

        # Pre-Draw
        clear_screen(color_white())

        # Post-Draw
        refresh_screen()

    # Cleanup
    close_window("Cave Escape")

main()