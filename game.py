import os
import sys
import math
import random
<<<<<<< HEAD
=======

>>>>>>> a983a5f25776e4ea825b7da092cfa41fb1205730
import pygame

from scripts.utils import load_image, load_images, Animation
from scripts.entities import PhysicsEntity, Player, Enemy
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds
from scripts.particle import Particle
from scripts.spark import Spark

<<<<<<< HEAD
class GameIntro:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Chef Game - Introduction')
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.intro_text = [
            "Welcome to The Chef Game!",
            "",
            "Story:",
            "You were a peaceful chef who cooked the tastiest food in all the land.",
            "But these days you have nothing. The Sky Barons came and took all your ingredients!",
            "You decide to fly to their sky castle and take it all back.",
            "Time for REVENGE!",
            "",
            "Controls:",
            "WASD for movement",
            "W twice to double jump",
            "SPACE to dash attack",
            "R to restart level",
            "ESC to quit",
            "",
            "Press any key to start the game..."
        ]
        self.text_height = len(self.intro_text) * 40  # Total height of all lines of text
        self.text_start_y = (self.screen.get_height() - self.text_height) // 2  # Y-position to start drawing text

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    running = False
            
            self.screen.fill((0, 0, 0))
            y = self.text_start_y  # Start drawing text from calculated y-position
            for text in self.intro_text:
                text_render = self.font.render(text, True, (255, 255, 255))
                text_rect = text_render.get_rect(center=(self.screen.get_width() // 2, y))
                self.screen.blit(text_render, text_rect)
                y += 40  # Increase y-position for next line of text
            
            pygame.display.flip()
            self.clock.tick(60)


=======
>>>>>>> a983a5f25776e4ea825b7da092cfa41fb1205730
class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('ninja game')
        self.screen = pygame.display.set_mode((1920, 1080))
        self.display = pygame.Surface((320, 170), pygame.SRCALPHA)
        self.display_2 = pygame.Surface((320, 170))
<<<<<<< HEAD
        self.clock = pygame.time.Clock()
        self.movement = [False, False, False, False]  # Updated to include up and down movement
=======

        self.clock = pygame.time.Clock()
        
        self.movement = [False, False]
        
>>>>>>> a983a5f25776e4ea825b7da092cfa41fb1205730
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png'),
            'background': load_image('background.png'),
            'clouds': load_images('clouds'),
            'enemy/idle': Animation(load_images('entities/enemy/idle'), img_dur=6),
            'enemy/run': Animation(load_images('entities/enemy/run'), img_dur=4),
            'player/idle': Animation(load_images('entities/player/idle'), img_dur=6),
            'player/run': Animation(load_images('entities/player/run'), img_dur=4),
            'player/jump': Animation(load_images('entities/player/jump')),
            'player/slide': Animation(load_images('entities/player/slide')),
            'player/wall_slide': Animation(load_images('entities/player/wall_slide')),
            'particle/leaf': Animation(load_images('particles/leaf'), img_dur=20, loop=False),
            'particle/particle': Animation(load_images('particles/particle'), img_dur=6, loop=False),
            'gun': load_image('gun.png'),
            'projectile': load_image('projectile.png'),
        }
        
<<<<<<< HEAD
        # Load sounds
=======
>>>>>>> a983a5f25776e4ea825b7da092cfa41fb1205730
        self.sfx = {
            'jump': pygame.mixer.Sound('data/sfx/jump.wav'),
            'dash': pygame.mixer.Sound('data/sfx/dash.wav'),
            'hit': pygame.mixer.Sound('data/sfx/hit.wav'),
            'shoot': pygame.mixer.Sound('data/sfx/shoot.wav'),
            'ambience': pygame.mixer.Sound('data/sfx/ambience.wav'),
        }
        
<<<<<<< HEAD
        # Set sound volumes
=======
>>>>>>> a983a5f25776e4ea825b7da092cfa41fb1205730
        self.sfx['ambience'].set_volume(0.2)
        self.sfx['shoot'].set_volume(0.4)
        self.sfx['hit'].set_volume(0.8)
        self.sfx['dash'].set_volume(0.3)
        self.sfx['jump'].set_volume(0.7)
        
<<<<<<< HEAD
        # Initialize clouds
        self.clouds = Clouds(self.assets['clouds'], count=16)
        
        # Initialize player
        self.player = Player(self, (50, 50), (8, 15))
        
        # Initialize tilemap
        self.tilemap = Tilemap(self, tile_size=16)
        
        # Initialize level and load the first level
        self.level = 0
        self.load_level(self.level)
        
        # Initialize other game parameters
        self.screenshake = 0
        self.transition = -30
        self.victory = False  # New variable to track victory state
        
        # Initialize font
        self.font = pygame.font.Font(None, 36)  # Add this line to initialize the font

        
    def load_level(self, map_id):
        # Load tilemap
        self.tilemap.load('data/maps/' + str(map_id) + '.json')
        
        # Initialize leaf spawners and enemies
=======
        self.clouds = Clouds(self.assets['clouds'], count=16)
        
        self.player = Player(self, (50, 50), (8, 15))
        
        self.tilemap = Tilemap(self, tile_size=16)
        
        self.level = 0
        self.load_level(self.level)
        
        self.screenshake = 0
        
    def load_level(self, map_id):
        self.tilemap.load('data/maps/' + str(map_id) + '.json')
        
>>>>>>> a983a5f25776e4ea825b7da092cfa41fb1205730
        self.leaf_spawners = []
        for tree in self.tilemap.extract([('large_decor', 2)], keep=True):
            self.leaf_spawners.append(pygame.Rect(4 + tree['pos'][0], 4 + tree['pos'][1], 23, 13))
            
        self.enemies = []
        for spawner in self.tilemap.extract([('spawners', 0), ('spawners', 1)]):
            if spawner['variant'] == 0:
                self.player.pos = spawner['pos']
                self.player.air_time = 0
            else:
                self.enemies.append(Enemy(self, spawner['pos'], (8, 15)))
            
        self.projectiles = []
        self.particles = []
        self.sparks = []
        
        self.scroll = [0, 0]
        self.dead = 0
        self.transition = -30
        
    def run(self):
        pygame.mixer.music.load('data/music.wav')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        
        self.sfx['ambience'].play(-1)
        
        while True:
            self.display.fill((0, 0, 0, 0))
            self.display_2.blit(self.assets['background'], (0, 0))
            
            self.screenshake = max(0, self.screenshake - 1)
            
            if not len(self.enemies):
                self.transition += 1
                if self.transition > 30:
<<<<<<< HEAD
                    if self.level == len(os.listdir('data/maps')) - 1:  # Check if it's the last level
                        self.victory = True  # Set victory to True if it's the last level
                    else:
                        self.level = min(self.level + 1, len(os.listdir('data/maps')) - 1)
                        self.load_level(self.level)
=======
                    self.level = min(self.level + 1, len(os.listdir('data/maps')) - 1)
                    self.load_level(self.level)
>>>>>>> a983a5f25776e4ea825b7da092cfa41fb1205730
            if self.transition < 0:
                self.transition += 1
            
            if self.dead:
                self.dead += 1
                if self.dead >= 10:
                    self.transition = min(30, self.transition + 1)
                if self.dead > 40:
                    self.load_level(self.level)
            
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            for rect in self.leaf_spawners:
                if random.random() * 49999 < rect.width * rect.height:
                    pos = (rect.x + random.random() * rect.width, rect.y + random.random() * rect.height)
                    self.particles.append(Particle(self, 'leaf', pos, velocity=[-0.1, 0.3], frame=random.randint(0, 20)))
            
            self.clouds.update()
            self.clouds.render(self.display_2, offset=render_scroll)
            
            self.tilemap.render(self.display, offset=render_scroll)
            
            for enemy in self.enemies.copy():
                kill = enemy.update(self.tilemap, (0, 0))
                enemy.render(self.display, offset=render_scroll)
                if kill:
                    self.enemies.remove(enemy)
            
            if not self.dead:
<<<<<<< HEAD
                self.player.update(self.tilemap, (self.movement[1] - self.movement[0], self.movement[3] - self.movement[2]))  # Pass up and down movement
=======
                self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
>>>>>>> a983a5f25776e4ea825b7da092cfa41fb1205730
                self.player.render(self.display, offset=render_scroll)
            
            # [[x, y], direction, timer]
            for projectile in self.projectiles.copy():
                projectile[0][0] += projectile[1]
                projectile[2] += 1
                img = self.assets['projectile']
                self.display.blit(img, (projectile[0][0] - img.get_width() / 2 - render_scroll[0], projectile[0][1] - img.get_height() / 2 - render_scroll[1]))
                if self.tilemap.solid_check(projectile[0]):
                    self.projectiles.remove(projectile)
                    for i in range(4):
                        self.sparks.append(Spark(projectile[0], random.random() - 0.5 + (math.pi if projectile[1] > 0 else 0), 2 + random.random()))
                elif projectile[2] > 360:
                    self.projectiles.remove(projectile)
                elif abs(self.player.dashing) < 50:
                    if self.player.rect().collidepoint(projectile[0]):
                        self.projectiles.remove(projectile)
                        self.dead += 1
                        self.sfx['hit'].play()
                        self.screenshake = max(16, self.screenshake)
                        for i in range(30):
                            angle = random.random() * math.pi * 2
                            speed = random.random() * 5
                            self.sparks.append(Spark(self.player.rect().center, angle, 2 + random.random()))
                            self.particles.append(Particle(self, 'particle', self.player.rect().center, velocity=[math.cos(angle + math.pi) * speed * 0.5, math.sin(angle + math.pi) * speed * 0.5], frame=random.randint(0, 7)))
                        
            for spark in self.sparks.copy():
                kill = spark.update()
                spark.render(self.display, offset=render_scroll)
                if kill:
                    self.sparks.remove(spark)
                    
            display_mask = pygame.mask.from_surface(self.display)
            display_sillhouette = display_mask.to_surface(setcolor=(0, 0, 0, 180), unsetcolor=(0, 0, 0, 0))
            for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                self.display_2.blit(display_sillhouette, offset)
            
            for particle in self.particles.copy():
                kill = particle.update()
                particle.render(self.display, offset=render_scroll)
                if particle.type == 'leaf':
                    particle.pos[0] += math.sin(particle.animation.frame * 0.035) * 0.3
                if kill:
                    self.particles.remove(particle)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        if self.player.jump():
                            self.sfx['jump'].play()
                    if event.key == pygame.K_SPACE:
                        self.player.dash()
<<<<<<< HEAD
                    if event.key == pygame.K_r:
                        self.load_level(self.level)  # Restart level when "R" key is pressed
                    if event.key == pygame.K_LEFT:  # Move to the previous level
                        self.level = max(0, self.level - 1)
                        self.load_level(self.level)
                    if event.key == pygame.K_RIGHT:  # Move to the next level
                        self.level = min(self.level + 1, len(os.listdir('data/maps')) - 1)
                        self.load_level(self.level)
            
=======
>>>>>>> a983a5f25776e4ea825b7da092cfa41fb1205730
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
<<<<<<< HEAD
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
                        self.movement[3] = False
=======

>>>>>>> a983a5f25776e4ea825b7da092cfa41fb1205730
                        
            if self.transition:
                transition_surf = pygame.Surface(self.display.get_size())
                pygame.draw.circle(transition_surf, (255, 255, 255), (self.display.get_width() // 2, self.display.get_height() // 2), (30 - abs(self.transition)) * 8)
                transition_surf.set_colorkey((255, 255, 255))
                self.display.blit(transition_surf, (0, 0))
                
            self.display_2.blit(self.display, (0, 0))
            
            screenshake_offset = (random.random() * self.screenshake - self.screenshake / 2, random.random() * self.screenshake - self.screenshake / 2)
            self.screen.blit(pygame.transform.scale(self.display_2, self.screen.get_size()), screenshake_offset)
            pygame.display.update()
            self.clock.tick(60)
<<<<<<< HEAD
            
            if self.victory:  # Display victory message if victory is achieved
                self.screen.fill((0, 0, 0))
                victory_text = "Congratulations! You have defeated The Sky Barons and taken back your ingredients! Thanks for playing!"
                text_render = self.font.render(victory_text, True, (255, 255, 255))
                text_rect = text_render.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
                self.screen.blit(text_render, text_rect)
                pygame.display.flip()
                pygame.time.wait(5000)  # Display for 5 seconds
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    intro = GameIntro()
    intro.run()
    main_game = Game()
    main_game.run()
=======

Game().run()
>>>>>>> a983a5f25776e4ea825b7da092cfa41fb1205730
