# -*- coding: utf-8 -*-
"""
Idea fair simple android game
@author: Chris Minar
game engine class
"""

#import pygame_sdl2
#pygame_sdl2.import_as_pygame()
import pygame
from game_object import game_object as go
import time

class game_engine():
    #
    # Class Members
    #
    # Pygame variables

    #
    # Class Methods
    #
    """called when this class is initialised"""
    def __init__(self):
        # Initialise Pygame window
        #Finish initialising pygame
        #Add player to object list
        #Reset floor height based on new screen size

    """handle key presses"""
    def event_loop(self):
        #For each event that has happened(each keystroke):
            #If the key is a left mouse click or android touch make the square jump
            #If the key pressed is the android back button or the escape key, kill the program
    
    """update velocity and position of all game objects"""
    def update_physics(self):
        #setup timestep
        #take one timestep for each object in the objects list
            # x = x_0 + v_0*dt + 0.5*g*dt^2 
            # v = v_0 + g*dt 
            #make sure it doesn't go through the floor
            
    """main game loop"""
    def game_loop(self):
        while not self.done:
            #set background color
            #draw floor
            #check for and handle button presses
            #advance the time for all objects
            #Draw all objects
            #update screen

    """end the game and close the window"""            
    def quit_game(self):
