import pygame

def main():
    pygame.init()
    gamer = pygame.image.load('data/gameover.png')
    screen = pygame.display.set_mode((600, 300))
    pygame.display.set_caption("game over")
    screen.fill((0, 0, 255))
    fps = 20
    clock = pygame.time.Clock()
    running = True
    x = -300
    while x <= 300:
        gm_r = gamer.get_rect(center=(x, 150))
        x += 10
        screen.blit(gamer, gm_r)
        clock.tick(fps)
        pygame.display.update()
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
main()