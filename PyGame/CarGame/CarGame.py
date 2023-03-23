import pygame
from CarCrash import Crash
from random import randint

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 1100)
W, H = 500, 700

dis = pygame.display.set_mode((W, H))
pygame.display.set_caption("CarRace")
pygame.display.set_icon(pygame.image.load('icon_car.jpg'))
pygame.mixer.music.load('bit_8b.mp3',)
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)
motor_sound = pygame.mixer.Sound('zv_motor.mp3')
pygame.mixer.Sound.play(motor_sound)
boom_sound = pygame.mixer.Sound('boom.mp3')
car = pygame.image.load("car12.jpg").convert_alpha()
car = pygame.transform.scale(car, (50, 100))
car.set_colorkey((255, 255, 255))
car_rect = car.get_rect(topleft=(225, 575))

fon = pygame.image.load("дорога_2д.jpg").convert()
fon = pygame.transform.scale(fon, (W, H))

car1 = pygame.image.load("car_11.png").convert_alpha()
car1 = pygame.transform.scale(car1, (50, 100))
car1.set_colorkey((255, 255, 255))
car2 = pygame.image.load("car_12.png").convert_alpha()
car2 = pygame.transform.scale(car2, (50, 100))
car2.set_colorkey((255, 255, 255))
car3 = pygame.image.load("car_13.png").convert_alpha()
car3 = pygame.transform.scale(car3, (50, 100))
car3.set_colorkey((255, 255, 255))
car4 = pygame.image.load("car_14.png").convert_alpha()
car4 = pygame.transform.scale(car4, (50, 100))
car4.set_colorkey((255, 255, 255))

heal_font = pygame.font.SysFont("comicsansms", 25)

Crash_surf = [car1, car2, car3, car4]


def creatCrash(group):
    indx = randint(0, len(Crash_surf) - 1)
    x = randint(85, 385)
    speed = randint(13, 17)
    return Crash(x, speed, Crash_surf[indx], group)

health = 5

def Your_health(health):
    value = heal_font.render("Life: " + str(health), True, pygame.Color('OrangeRed'))
    dis.blit(value, [10, 30])

def Stolknovenie():
    global health
    for Crash_surf in Crash_1:
        if car_rect.colliderect(Crash_surf):
            pygame.mixer.Sound.play(boom_sound)
            health = health - 1
            Crash_surf.kill()
        elif health == 0:
            exit()


Crash_1 = pygame.sprite.Group()
clock = pygame.time.Clock()
FPS = 60
speed_car = 10

creatCrash(Crash_1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            creatCrash(Crash_1)
    bt = pygame.key.get_pressed()
    if bt[pygame.K_a]:
        car_rect.x -= speed_car
        if car_rect.x < 75:
            car_rect.x = 75
    elif bt[pygame.K_d]:
        car_rect.x += speed_car
        if car_rect.x > 385:
            car_rect.x = 385
    elif bt[pygame.K_w]:
        car_rect.y -= speed_car
        if car_rect.y < 200:
            car_rect.y = 200
    elif bt[pygame.K_s]:
        car_rect.y += speed_car
        if car_rect.y > 575:
            car_rect.y = 575

    Stolknovenie()
    dis.blit(fon, (0, 0))
    Crash_1.draw(dis)
    Your_health(health)
    dis.blit(car, car_rect)
    pygame.display.update()
    clock.tick(FPS)
    Crash_1.update(H)
