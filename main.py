import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    allAsteroids = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in updatable:
            obj.update(dt)

            if isinstance(obj, AsteroidField):
                continue

            if isinstance(obj, Player):
                for asteroid in asteroids:
                    if asteroid.checkCollision(obj):
                        print("GAMEOVER!")
                        exit(1)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
