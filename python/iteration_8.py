from splashkit import *

GRAVITY = 0.08
MAX_SPEED = 5
JUMP_RECOVERY_BOOST = 2
FOREGROUND_SCROLL_SPEED = -2
BACKGROUND_SCROLL_SPEED = -1

NUM_POLES = 4

class pole_data:
    def __init__(self, _score_limiter, _up_pole, _down_pole):
        self.score_limiter = _score_limiter
        self.up_pole = _up_pole
        self.down_pole = _down_pole

class scene_data:
    def __init__(self, _background, _foreground, _foreroof):
        self.background = _background
        self.foreground = _foreground
        self.foreroof = _foreroof

class game_data:
    def __init__(self, _scene, _poles, _player):
        self.scene = _scene
        self.poles = _poles
        self.player = _player

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

def get_new_scene():
    
    resultBackground = create_sprite_with_bitmap_named("Background")
    sprite_set_x(resultBackground, 0)
    sprite_set_y(resultBackground, 0)
    sprite_set_dx(resultBackground, BACKGROUND_SCROLL_SPEED)

    resultForeground = create_sprite_with_bitmap_and_animation_named("Foreground", "ForegroundAnimations")
    sprite_set_x(resultForeground, 0)
    sprite_set_y(resultForeground, screen_height() - sprite_height(resultForeground))
    sprite_set_dx(resultForeground, FOREGROUND_SCROLL_SPEED)
    sprite_start_animation_named(resultForeground, "Fire")

    resultForeroof = create_sprite_with_bitmap_named("Foreroof")
    sprite_set_x(resultForeroof, 0)
    sprite_set_y(resultForeroof, 0)
    sprite_set_dx(resultForeroof, FOREGROUND_SCROLL_SPEED)

    return scene_data(resultBackground, resultForeground, resultForeroof)

def get_new_game():
    load_resource_bundle("CaveEscape", "cave_escape.txt")

    resultScene = get_new_scene()
    resultPoles = [get_random_poles() for i in range(NUM_POLES)]
    resultPlayer = get_new_player()

    return game_data(resultScene, resultPoles, resultPlayer)

def update_scene(scene):
    update_sprite(scene.background)
    update_sprite(scene.foreground)
    update_sprite(scene.foreroof)

    if sprite_x(scene.background) <= -(sprite_width(scene.background) / 2):
        sprite_set_x(scene.background, 0)

    if sprite_x(scene.foreground) <= -(sprite_width(scene.foreground) / 2):
        sprite_set_x(scene.foreground, 0)
        sprite_set_x(scene.foreroof, 0)

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

def update_pole_array(pole_array):
    for i in range(len(pole_array)):
        pole_array[i] = update_poles(pole_array[i])

    return pole_array

def draw_poles(poles):
    draw_sprite(poles.up_pole)
    draw_sprite(poles.down_pole)

def draw_pole_array(pole_array):
    for i in range(len(pole_array)):
        draw_poles(pole_array[i])

def update_player(player):
    update_velocity(player)
    update_sprite(player)

def update_game(game):
    process_events()
    handle_input(game.player)
    game.poles = update_pole_array(game.poles)
    update_player(game.player)
    update_scene(game.scene)
    return game

def draw_game(game):
    draw_sprite(game.scene.background)
    draw_pole_array(game.poles)
    draw_sprite(game.player)
    draw_sprite(game.scene.foreground)
    draw_sprite(game.scene.foreroof)
    
def main():

    open_window("Cave Escape", 432, 768)

    game_data = get_new_game()

    while not window_close_requested_named("Cave Escape"):
        # Update
        game_data = update_game(game_data)

        # Pre-Draw
        clear_screen(color_white())

        # Draw
        draw_game(game_data)

        # Post-Draw
        refresh_screen()

    # Cleanup
    free_resource_bundle("CaveEscape")
    close_window("Cave Escape")

main()