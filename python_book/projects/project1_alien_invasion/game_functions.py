import sys
from time import sleep

import pygame
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    '''Response to keypresses and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_events_keyup(event, ship)


def check_events_keyup(event, ship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_events_keydown(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    # create a new bullet
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    ''' Update images on the screen and flip to new screen'''
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    '''Update the position of the bullets and manage bullet'''
    # update position
    bullets.update()

    # remove bullet that useless
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # check collision
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # if all bullets die then make new
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def get_row_max_alien(ai_settings, alien):
    ''' calculate the number of aliens each row '''
    alien_width = alien.rect.width
    aliens_gap = alien.aliens_gap
    alien_border_gap = alien.alien_border_gap

    available_space_x = ai_settings.screen_width - 2 * alien_border_gap
    row_max_alien = int(available_space_x/(alien_width+aliens_gap))
    return row_max_alien


def get_line_max_alien(ai_settings, ship_height, alien_height):
    ''' calculate how many lines can have '''
    available_space_y = (ai_settings.screen_height -
                         3 * alien_height - ship_height)
    line_max_alien = int(available_space_y/(2*alien_height))
    return line_max_alien


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    ''' create a alien and determine its position '''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien.alien_border_gap + \
        alien_number*(alien_width + alien.aliens_gap)
    alien.y = alien.alien_border_gap + \
        (alien.rect.height+alien.aliens_gap)*row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    ''' create a full fleet of aliens'''
    # calculate the number of aliens each row
    alien = Alien(ai_settings, screen)
    row_max_alien = get_row_max_alien(ai_settings, alien)
    line_max_alien = get_line_max_alien(
        ai_settings, ship.rect.height, alien.rect.height)

    # create the fleet of aliens
    for row_number in range(line_max_alien):
        for alien_number in range(row_max_alien):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    ''' respond to ship being hit by alien '''
    # lose one life
    stats.life -= 1

    # clear aliens and bullets
    aliens.empty()
    bullets.empty()

    # create a new fleet and renew ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # pause
    sleep(2)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # check alien-ship collision
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
        # pass


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
