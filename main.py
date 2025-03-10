import sys

import pygame

import constants
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.check_collisions(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
