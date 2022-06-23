from splashkit import *

GRAVITY = 0.08
MAX_SPEED = 5
JUMP_RECOVERY_BOOST = 2
FOREGROUND_SCROLL_SPEED = -2

class pole_data:
    def __init__(self, _score_limiter, _up_pole, _down_pole):
        self.score_limiter = _score_limiter
        self.up_pole = _up_pole
        self.down_pole = _down_pole

def get_new_player():
    
    result = create_sprite_with_bitmap_and_animation_named("Player", "PlayerAnimations")

    sprite_set_x(result, (screen_width() / 2) - sprite_width(result))
    sprite_set_y(result, screen_width() / 2)
    sprite_start_animation_named(result, "Fly")

    return result

def get_random_poles():

    resultUpPole = create_sprite_with_bitmap_named("UpPole")
    resultDownPole = create_sprite_with_bitmap_named("DownPole")

    sprite_set_x(resultUpPole, screen_width() + rnd_int(1200))
    sprite_set_y(resultUpPole, screen_height() - sprite_height(resultUpPole))

    sprite_set_x(resultDownPole, sprite_x(resultUpPole))
    sprite_set_y(resultDownPole, 0)

    sprite_set_dx(resultUpPole, FOREGROUND_SCROLL_SPEED)
    sprite_set_dx(resultDownPole, FOREGROUND_SCROLL_SPEED)

    result = pole_data(False, resultUpPole, resultDownPole)

    return result

def handle_input(player):
    if key_typed(KeyCode.space_key):
        sprite_set_dy(player, sprite_dy(player) - JUMP_RECOVERY_BOOST)

def reset_pole_data(poles):
    free_sprite(poles.up_pole)
    free_sprite(poles.down_pole)

    poles = get_random_poles()
    return poles

def update_velocity(player):
    sprite_set_dy(player, sprite_dy(player) + GRAVITY)

    if sprite_dy(player) > MAX_SPEED:
        sprite_set_dy(player, MAX_SPEED)
    elif sprite_dy(player) < -MAX_SPEED:
        sprite_set_dy(player, -MAX_SPEED)

def update_poles(poles):
    update_sprite(poles.up_pole)
    update_sprite(poles.down_pole)

    if ((sprite_x(poles.up_pole) + sprite_width(poles.up_pole)) < 0):
        poles = reset_pole_data(poles)

    return poles

def draw_poles(poles):
    draw_sprite(poles.up_pole)
    draw_sprite(poles.down_pole)


def main():

    open_window("Cave Escape", 432, 768)
    load_resource_bundle("CaveEscape", "cave_escape.txt")

    game_poles = get_random_poles()
    player = get_new_player()

    while not window_close_requested_named("Cave Escape"):
        # Update
        process_events()
        handle_input(player)
        game_poles = update_poles(game_poles)
        update_velocity(player)
        update_sprite(player)

        # Pre-Draw
        clear_screen(color_white())

        # Draw
        draw_poles(game_poles)
        draw_sprite(player)

        # Post-Draw
        refresh_screen()

    # Cleanup
    free_resource_bundle("CaveEscape")
    close_window("Cave Escape")

main()