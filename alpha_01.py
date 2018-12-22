import pygame
import pygame.gfxdraw

pygame.init()

class project:
    class display:
        size = (1280, 720)

        pygame.display.set_caption('ParkBaka')
        pygame.display.set_icon(pygame.image.load('.\\res\\image\\icon.ico'))

    exit = False
    window = pygame.display.set_mode(display.size)

class basic:
    class color:
        black = (0, 0, 0)
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        white = (255, 255, 255)

    class input:
        keystate = [False, False, False, False]

        lalt = False
        ralt = False

class camera:
    pos = [0, 0]
    speed = 3

class enemy:
    pos = [0, 0]
    size = 30
    speed = 3
    col = basic.color.red

class player:
    pos = [0, 0]
    size = 30
    speed = 3
    col = basic.color.blue

    @staticmethod
    def render():
        pygame.gfxdraw.aacircle(project.window, player.pos[0] - camera.pos[0] + project.display.size[0] // 2, player.pos[1] - camera.pos[1] + project.display.size[1] // 2, player.size, player.col)
        pygame.gfxdraw.filled_circle(project.window, player.pos[0] - camera.pos[0] + project.display.size[0] // 2, player.pos[1] - camera.pos[1] + project.display.size[1] // 2, player.size, player.col)

class obstacle:
    def __init__(self, x: int, y: int, w: int, h: int, color: tuple):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def render(self):
        pygame.gfxdraw.box(project.window, ((self.x - camera.pos[0] + project.display.size[0] // 2, self.y - camera.pos[1] + project.display.size[1] // 2), (self.w, self.h)), self.color)

obstacles = []
obstacles.append(obstacle(100, 100, 200, 200, basic.color.green))
obstacles.append(obstacle(-100, 100, 150, -100, basic.color.red))

def calc():
    if basic.input.keystate[0]:
        camera.pos[1] -= camera.speed
        player.pos[1] -= player.speed
    if basic.input.keystate[1]:
        camera.pos[0] -= camera.speed
        player.pos[0] -= player.speed
    if basic.input.keystate[2]:
        camera.pos[1] += camera.speed
        player.pos[1] += player.speed
    if basic.input.keystate[3]:
        camera.pos[0] += camera.speed
        player.pos[0] += player.speed

def print_screen():
    project.window.fill(basic.color.white)

    for OBSTACLE in obstacles:
        OBSTACLE.render()

    player.render()

while not project.exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            project.exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT:
                basic.input.lalt = True
            elif event.key == pygame.K_RALT:
                basic.input.ralt = True
            elif event.key == pygame.K_F4:
                if basic.input.lalt or basic.input.ralt:
                    project.exit = True
            elif event.key == pygame.K_w:
                basic.input.keystate[0] = True
            elif event.key == pygame.K_a:
                basic.input.keystate[1] = True
            elif event.key == pygame.K_s:
                basic.input.keystate[2] = True
            elif event.key == pygame.K_d:
                basic.input.keystate[3] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LALT:
                basic.input.lalt = False
            elif event.key == pygame.K_RALT:
                basic.input.ralt = False
            elif event.key == pygame.K_w:
                basic.input.keystate[0] = False
            elif event.key == pygame.K_a:
                basic.input.keystate[1] = False
            elif event.key == pygame.K_s:
                basic.input.keystate[2] = False
            elif event.key == pygame.K_d:
                basic.input.keystate[3] = False

    pygame.time.Clock().tick(60)

    calc()
    print_screen()

    pygame.display.flip()


pygame.quit()
exit()
