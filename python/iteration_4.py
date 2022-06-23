from splashkit import *

GRAVITY = 0.08
MAX_SPEED = 5
JUMP_RECOVERY_BOOST = 2

def get_new_player():
    result = create_sprite_with_bitmap_and_animation_named("Player", "PlayerAnimations")

    sprite_set_x(result, (screen_width() / 2) - sprite_width(result))
    sprite_set_y(result, screen_width() / 2)
    sprite_start_animation_named(result, "Fly")

    return result

def update_velocity(player):
    sprite_set_dy(player, sprite_dy(player) + GRAVITY)

    if sprite_dy(player) > MAX_SPEED:
        sprite_set_dy(player, MAX_SPEED)
    elif sprite_dy(player) < -MAX_SPEED:
        sprite_set_dy(player, -MAX_SPEED)

def handle_input(player):
    if key_typed(KeyCode.space_key):
        sprite_set_dy(player, sprite_dy(player) - JUMP_RECOVERY_BOOST)

def main():

    open_window("Cave Escape", 432, 768)
    load_resource_bundle("CaveEscape", "cave_escape.txt")

    player = get_new_player()

    while not window_close_requested_named("Cave Escape"):
        # Update
        process_events()
        handle_input(player)
        update_velocity(player)
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