#include <splashkit.h>

sprite get_new_player()
{
    sprite result = create_sprite(bitmap_named("Player"), animation_script_named("PlayerAnimations"));

    sprite_set_x(result, (screen_width() / 2) - sprite_width(result));
    sprite_set_y(result, screen_height() / 2);
    sprite_start_animation(result, "Fly");

    return result;
}

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
