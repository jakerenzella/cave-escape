from splashkit import *

def get_new_player():
    result = create_sprite_with_bitmap_and_animation_named("Player", "PlayerAnimations")

    sprite_set_x(result, (screen_width() / 2) - sprite_width(result))
    sprite_set_y(result, screen_width() / 2)
    sprite_start_animation_named(result, "Fly")

    return result

def main():

    open_window("Cave Escape", 432, 768)
    load_resource_bundle("CaveEscape", "cave_escape.txt")

    player = get_new_player()

    while not window_close_requested_named("Cave Escape"):
        # Update
        process_events()
        update_sprite(player)

        # Pre-Draw
        clear_screen(color_white())

        # Draw
        draw_sprite(player)

        # Post-Draw
        refresh_screen()

    # Cleanup
    free_resource_bundle("CaveEscape")
    close_window("Cave Escape")

main()