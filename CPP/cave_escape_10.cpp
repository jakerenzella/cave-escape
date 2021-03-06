#include <splashkit.h>
#include <cstdio>

const float GRAVITY = 0.08f;
const int MAX_SPEED = 5;
const int JUMP_RECOVERY_BOOST = 2;
const int FOREGROUND_SCROLL_SPEED = -2;
const int BACKGROUND_SCROLL_SPEED = -1;
const int NUM_POLES = 4;

struct scene_data
{
    sprite background;
    sprite foreground;
    sprite foreroof;
};

struct pole_data
{
    bool score_limiter;
    sprite up_pole;
    sprite down_pole;
};

typedef struct pole_data poles[NUM_POLES];

enum player_state
{
    MENU,
    PLAY
};

enum game_color
{
    PURPLE,
    ORANGE
};

typedef struct player_data
{
    player_state state;
    sprite sprite_data;
    bool is_dead;
    int score;
} player_data;

typedef struct game_data
{
    scene_data scene;
    pole_data poles[NUM_POLES];
    player_data player;
    game_color color;

} game_data;

scene_data get_new_scene(game_color color)
{
    scene_data result;

    result.background = create_sprite(bitmap_named("Background"));

    sprite_set_x(result.background, 0);
    sprite_set_y(result.background, 0);
    sprite_set_dx(result.background, BACKGROUND_SCROLL_SPEED);

    // result.foreground_purple = create_sprite(bitmap_named("ForegroundPurple"), animation_script_named("ForegroundAnimations"));
    result.foreground = create_sprite(bitmap_named("Foreground"), animation_script_named("ForegroundAnimations"));

    sprite_set_x(result.foreground, 0);
    sprite_set_y(result.foreground, screen_height() - sprite_height(result.foreground));
    sprite_set_dx(result.foreground, FOREGROUND_SCROLL_SPEED);
    sprite_start_animation(result.foreground, "Fire");

    // sprite_set_x(result.foreground_purple, 0);
    // sprite_set_y(result.foreground_purple, screen_height() - sprite_height(result.foreground_purple));
    // sprite_set_dx(result.foreground_purple, FOREGROUND_SCROLL_SPEED);
    // sprite_start_animation(result.foreground_purple, "Fire");
    
    result.foreroof = create_sprite(bitmap_named("Foreroof"));

    sprite_set_x(result.foreroof, 0);
    sprite_set_y(result.foreroof, 0);
    sprite_set_dx(result.foreroof, FOREGROUND_SCROLL_SPEED);

    return result;
}

pole_data get_random_poles()
{
    pole_data result;

    result.up_pole = create_sprite(bitmap_named("UpPole"));
    result.down_pole = create_sprite(bitmap_named("DownPole"));

    sprite_set_x(result.up_pole, screen_width() + rnd(1200));
    sprite_set_y(result.up_pole, screen_height() - sprite_height(result.up_pole) - rnd(bitmap_height(bitmap_named("Foreground"))) + 1);

    sprite_set_x(result.down_pole, sprite_x(result.up_pole));
    sprite_set_y(result.down_pole, rnd(bitmap_height(bitmap_named("Foreroof"))) + 1);

    sprite_set_dx(result.up_pole, FOREGROUND_SCROLL_SPEED);
    sprite_set_dx(result.down_pole, FOREGROUND_SCROLL_SPEED);

    result.score_limiter = true;

    return result;
}

player_data get_new_player()
{
    player_data result;

    result.sprite_data = create_sprite(bitmap_named("Player"), animation_script_named("PlayerAnimations"));

    sprite_set_x(result.sprite_data, (screen_width() / 2) - sprite_width(result.sprite_data));
    sprite_set_y(result.sprite_data, screen_height() / 2);
    sprite_start_animation(result.sprite_data, "Fly");

    result.score = 0;
    result.is_dead = false;
    result.state = MENU;

    return result;
}

game_data set_up_game()
{
    game_data result;
    result.color = PURPLE;

    load_resource_bundle("CaveEscape", "cave_escape.txt");

    result.scene = get_new_scene(result.color);

    for (int i = 0; i < NUM_POLES; ++i)
    {
        result.poles[i] = get_random_poles();
    }

    result.player = get_new_player();

    fade_music_in("GameMusic", -1, 15000);

    return result;
}

void check_for_collisions(game_data &game)
{
    if (sprite_collision(game.player.sprite_data, game.scene.foreground) || sprite_collision(game.player.sprite_data, game.scene.foreroof))
    {
        game.player.is_dead = true;

        return;
    }

    for (int i = 0; i < NUM_POLES; ++i)
    {
        if (sprite_collision(game.player.sprite_data, game.poles[i].up_pole) || sprite_collision(game.player.sprite_data, game.poles[i].down_pole))
        {
            game.player.is_dead = true;

            return;
        }
    }
}

void handle_input(game_data &game)
{
    if (key_typed(SPACE_KEY))
    {
        if (game.player.state == PLAY)
        {
            sprite_set_dy(game.player.sprite_data, sprite_dy(game.player.sprite_data) - JUMP_RECOVERY_BOOST);
        }
        else
        {
            game.player.state = PLAY;
        }
    }
    if (key_typed(NUM_0_KEY))
    {
        game.color = PURPLE;
        game.scene.foreground = create_sprite(bitmap_named("ForegroundPurple"), animation_script_named("ForegroundAnimations"));
    } 
    if (key_typed(NUM_1_KEY))
    {
        game.color = ORANGE;
        game.scene.foreground = create_sprite(bitmap_named("Foreground"), animation_script_named("ForegroundAnimations"));
    }
}

void update_scene(scene_data &scene)
{
    update_sprite(scene.background);
    update_sprite(scene.foreground);
    update_sprite(scene.foreroof);

    if (sprite_x(scene.background) <= -(sprite_width(scene.background) / 2))
    {
        sprite_set_x(scene.background, 0);
    }

    if (sprite_x(scene.foreground) <= -(sprite_width(scene.foreground) / 2))
    {
        sprite_set_x(scene.foreground, 0);
        sprite_set_x(scene.foreroof, 0);
    }
}

void reset_pole_data(pole_data &poles)
{
    free_sprite(poles.up_pole);
    free_sprite(poles.down_pole);

    poles = get_random_poles();
}

void update_poles(pole_data &poles, player_data &player)
{
    update_sprite(poles.up_pole);
    update_sprite(poles.down_pole);

    if ((sprite_x(poles.up_pole) < sprite_x(player.sprite_data)) &&poles.score_limiter)
    {
        poles.score_limiter = false;
        ++player.score;
    }

    if ((sprite_x(poles.up_pole) + sprite_width(poles.up_pole)) < 0)
    {
        reset_pole_data(poles);
    }
}

void update_pole_array(pole_data pole_array[], player_data &player)
{
    for (int i = 0; i < NUM_POLES; ++i)
    {
        update_poles(pole_array[i], player);
    }
}

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

void update_player(player_data &player)
{
    if (player.state == PLAY)
    {
        update_velocity(player.sprite_data);
    }

    update_sprite(player.sprite_data);
}

void reset_player(player_data &player)
{
    free_sprite(player.sprite_data);

    player = get_new_player();
}

void reset_game(game_data &game)
{
    reset_player(game.player);

    for (int i = 0; i < NUM_POLES; ++i)
    {
        reset_pole_data(game.poles[i]);
    }
}

void update_game(game_data &game)
{
    if (!game.player.is_dead)
    {
        check_for_collisions(game);
        handle_input(game);
        write_line(game.color);
        update_scene(game.scene);
        update_player(game.player);

        if (game.player.state == PLAY)
        {
            update_pole_array(game.poles, game.player);
        }
    }
    else
    {
        reset_game(game);
    }
}

void draw_poles(pole_data &poles)
{
    draw_sprite(poles.up_pole);
    draw_sprite(poles.down_pole);
}

void draw_pole_array(pole_data pole_array[])
{
    for (int i = 0; i < NUM_POLES; ++i)
    {
        draw_poles(pole_array[i]);
    }
}

void draw_game(game_data &game)
{
    char str[15];

    sprintf(str, "%d", game.player.score);

    draw_sprite(game.scene.background);
    draw_pole_array(game.poles);
    draw_sprite(game.scene.foreroof);
    draw_sprite(game.scene.foreground);


    draw_sprite(game.player.sprite_data);

    if (game.player.state == PLAY)
    {
        draw_text(str, COLOR_WHITE, "GameFont", 21, 10, 0);
    }
    else
    {
        draw_bitmap(bitmap_named("Logo"), 0, 40);
        draw_text("PRESS SPACE!", COLOR_WHITE, "GameFont", 21, 68, 180);
    }
}

int main()
{
    // Initialisation
    open_window("Cave Escape", 432, 768);

    game_data game = set_up_game();

    do
    {
        // Update
        process_events();
        update_game(game);

        // Pre-Draw
        clear_screen(COLOR_WHITE);

        // Draw
        draw_game(game);

        // Post-Draw
        refresh_screen(60);
    } while (!window_close_requested("Cave Escape"));

    // Cleanup
    free_resource_bundle("CaveEscape");
    close_window("Cave Escape");

    return 0;
}
