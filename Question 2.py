import pygame


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.is_jumping = False
        self.jump_count = 10
        self.health = 100
        self.lives = 3
        self.projectiles = []

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if not self.is_jumping:
            if keys[pygame.K_SPACE]:
                self.is_jumping = True
        else:
            if self.jump_count >= -10:
                self.y -= (self.jump_count * abs(self.jump_count)) * 0.5
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.is_jumping = False

    def shoot(self):
        projectile = Projectile(self.x, self.y)
        self.projectiles.append(projectile)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.lives -= 1
            self.health = 100

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 255), (self.x, self.y, 50, 50))


class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 7
        self.damage = 10

    def move(self):
        self.x += self.speed

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 10, 5))


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 50
        self.speed = 2
        self.damage = 10

    def move(self):
        self.x -= self.speed

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:

            def draw(self, win):
                pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 50, 50))


def main():
    pygame.init()
    win = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    player = Player(50, 500)

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        win.fill((0, 0, 0))
        player.draw(win)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
