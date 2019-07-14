import pygame, math
from utils import *

class Car:

    maxDistanceSensor = 15

    def __init__(self, id, carPosX, carPosY, baseDegree):
        self.id = id
        self.body = pygame.image.load("gameAsset/car2.png")
        self.rect = self.body.get_rect()
        self.rect.x = carPosX
        self.rect.y = carPosY
        self.rect.center = self.rect.x, self.rect.y
        self.crash = False
        self.end = False
        self.score = 0

        # movement
        self.forward = False
        self.backward = False
        self.left = False
        self.right = False
        self.angle = baseDegree

        self.turn_speed = 1.4
        self.top_speed = 4
        self.acceleration = 0.3
        self.deceleration = 0.2
        self.current_speed = 0
        self.move_x = 0
        self.move_y = 0

    def reset_data(self):
        self.left = False
        self.right = False
        self.forward = False
        self.backward = False

    def rotate(self):

        if self.angle > 360:
            self.angle = 0
        else:
            if self.angle < 0:
                self.angle = 360
        if self.left:
            self.angle += self.turn_speed * self.current_speed
        if self.right:
            self.angle -= self.turn_speed * self.current_speed

    def move(self):
        if self.forward:
            if self.current_speed < self.top_speed:
                self.current_speed += self.acceleration
        else:
            if self.current_speed > 0:
                self.current_speed -= self.deceleration
            else:
                self.current_speed = 0

        angle_rad = deg_to_rad(self.angle)
        self.move_x = -(float(self.current_speed * math.sin(angle_rad)))
        self.move_y = -(float(self.current_speed * math.cos(angle_rad)))
        self.rect.x += self.move_x
        self.rect.y += self.move_y

    def display(self, main_surface):
        temp_image = pygame.transform.rotate(self.body, self.angle)
        main_surface.blit(temp_image, (self.rect.x, self.rect.y))

    def update(self, surface):
        self.isCrash(surface)
        self.isEnd(surface)
        self.getSensorValue(surface)

        if not self.end and not self.crash:
            self.move_x = 0
            self.move_y = 0
            self.rotate()
            self.move()
            self.reset_data()
            self.isCrash(surface)
            self.isEnd(surface)

    def getAllPixels(self):
        pixels = []

        if self.rect.topleft[0] < self.rect.bottomright[0]:
            startW = self.rect.topleft[0]
            endW = self.rect.bottomright[0]
        else:
            startW = self.rect.bottomright[0]
            endW = self.rect.topleft[0]

        if self.rect.topleft[1] < self.rect.bottomright[1]:
            startH = self.rect.topleft[1]
            endH = self.rect.bottomright[1]
        else:
            startH = self.rect.bottomright[1]
            endH = self.rect.topleft[1]


        for x in range (startW, endW + 1):
            for y in range(startH, endH + 1):
                 pixels.append( (x,y) )

        return pixels

    def displayBrokeCar(self, main_surface):
        temp_image = pygame.image.load("gameAsset/boom.png")
        main_surface.blit(temp_image, (self.rect.x, self.rect.y))
        pygame.display.flip()

    def isCrash(self, surface):
        for pos in self.getAllPixels():
            value = surface.get_at(pos)
            if value == (255, 0, 0):
                self.crash = True
                self.displayBrokeCar(surface)

    def isEnd(self, surface):
        for pos in self.getAllPixels():
            value = surface.get_at(pos)
            if value == (107, 81, 117):
                self.end = True

    def passCheckpoint(self, surface):
        for pos in self.getAllPixels():
            value = surface.get_at(pos)
            if value == (-1, -1, -1):
                self.end

    #return list of sensor left to right
    def getSensorValue(self, surface):

        zone_explore_pixel = 2
        sensor_x_1 = self.rect.x
        sensor_y_1 = self.rect.y

        mid_sensor_value = 0
        for i in [x * 0.1 for x in range(30, 45)]:
            temp_image = pygame.image.load("abeille.jpg")
            angle_rad = deg_to_rad(self.angle)
            move_sensor_x_1 = -(float(i * math.sin(angle_rad)))
            move_sensor_y_1 = -(float(i * math.cos(angle_rad)))
            sensor_x_1 += move_sensor_x_1
            sensor_y_1 += move_sensor_y_1
            surface.blit(temp_image, (sensor_x_1, sensor_y_1))
            listes_pos = getPosNear( (sensor_x_1, sensor_y_1), zone_explore_pixel)

            if isPixelCrash(surface, listes_pos):
                break
            else:
                mid_sensor_value += 1

        sensor_x_1 = self.rect.x
        sensor_y_1 = self.rect.y

        left_sensor1_value = 0
        for i in [x * 0.1 for x in range(30, 45)]:
            # left 1
            temp_image = pygame.image.load("elephant.jpg")
            angle_rad = deg_to_rad(self.angle + 70)
            move_sensor_x_1 = -(float(i * math.sin(angle_rad)))
            move_sensor_y_1 = -(float(i * math.cos(angle_rad)))
            sensor_x_1 += move_sensor_x_1
            sensor_y_1 += move_sensor_y_1
            surface.blit(temp_image, (sensor_x_1, sensor_y_1))
            listes_pos = getPosNear((sensor_x_1, sensor_y_1), zone_explore_pixel)

            if isPixelCrash(surface, listes_pos):
                break
            else:
                left_sensor1_value += 1


        sensor_x_1 = self.rect.x
        sensor_y_1 = self.rect.y
        left_sensor2_value = 0
        for i in [x * 0.1 for x in range(30, 45)]:
            # left 2
            temp_image = pygame.image.load("phasme.jpg")
            angle_rad = deg_to_rad(self.angle + 25)
            move_sensor_x_1 = -(float(i * math.sin(angle_rad)))
            move_sensor_y_1 = -(float(i * math.cos(angle_rad)))
            sensor_x_1 += move_sensor_x_1
            sensor_y_1 += move_sensor_y_1
            surface.blit(temp_image, (sensor_x_1, sensor_y_1))
            listes_pos = getPosNear((sensor_x_1, sensor_y_1), zone_explore_pixel)

            if isPixelCrash(surface, listes_pos):
                break
            else:
                left_sensor2_value += 1

        sensor_x_1 = self.rect.x
        sensor_y_1 = self.rect.y

        right_sensor1_value = 0
        for i in [x * 0.1 for x in range(30, 45)]:
            # right 1
            temp_image = pygame.image.load("elephant.jpg")
            angle_rad = deg_to_rad(self.angle - 70)
            move_sensor_x_1 = -(float(i * math.sin(angle_rad)))
            move_sensor_y_1 = -(float(i * math.cos(angle_rad)))
            sensor_x_1 += move_sensor_x_1
            sensor_y_1 += move_sensor_y_1
            surface.blit(temp_image, (sensor_x_1, sensor_y_1))
            listes_pos = getPosNear((sensor_x_1, sensor_y_1), zone_explore_pixel)

            if isPixelCrash(surface, listes_pos):
                break
            else:
                right_sensor1_value += 1

        sensor_x_1 = self.rect.x
        sensor_y_1 = self.rect.y
        right_sensor2_value = 0
        for i in [x * 0.1 for x in range(30, 45)]:
            # left 1
            temp_image = pygame.image.load("phasme.jpg")
            angle_rad = deg_to_rad(self.angle - 25)
            move_sensor_x_1 = -(float(i * math.sin(angle_rad)))
            move_sensor_y_1 = -(float(i * math.cos(angle_rad)))
            sensor_x_1 += move_sensor_x_1
            sensor_y_1 += move_sensor_y_1
            surface.blit(temp_image, (sensor_x_1, sensor_y_1))
            listes_pos = getPosNear((sensor_x_1, sensor_y_1), zone_explore_pixel)

            if isPixelCrash(surface, listes_pos):
                break
            else:
                right_sensor2_value += 1

        # print("mid    :", mid_sensor_value)
        # print("left1  :", left_sensor1_value)
        # print("left2  :", left_sensor2_value)
        # print("right1 :", right_sensor1_value)
        # print("right2 :", right_sensor2_value)

        pygame.display.flip()

        return [left_sensor1_value, left_sensor2_value, mid_sensor_value, right_sensor2_value, right_sensor1_value]


