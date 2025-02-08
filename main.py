import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    dt = 0
    Score = 0
    shots_fired = 0
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)

        for obj in asteroids:
            for shot in shots:
                if obj.collisions(shot):
                    obj.split()
                    shot.kill()
                    Score += 1
                    shots_fired += 1

            if obj.collisions(player):
                print("Game over!")
                print(f"Score: {Score}")
                print(f"Shots fired: {shots_fired}")
                print(f"Accuracy: {(shots_fired / Score) * 100}%")
                exit()
            
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()