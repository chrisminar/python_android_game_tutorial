# Make a game for computers and android using Python!  
This is the repository that goes along with the [Youtube]() series.  
The series is a guide to go from zero programming experience to having a working game on your android phone.  
This repository contains the basic files we go through in the Youtube videos and the full game source code.  

##Part 1: get game working on computer  
###1. Install git bash
###2. clone this repo to your computer (example filepath)  
	> cd /c/Users/Chris\ Minar/Documents/Python  
	> git clone https://github.com/chrisminar/python_android_game_tutorial  
###3. Install anaconda 2.7 32 bit  
###4. Install pygame 2.7 32 bit  
###5. go through code with youtube series  
###6. debug the code!  

##Part 2: port to android  
1. install pygame_sdl2  
-install gitbash  
-open git bash and move to pygame_sdl2 directory  
	> cd /c/Users/Chris\ Minar/Documents/pygame_sdl2  
-install pygame_sdl2  
	> python setup.py install  
-go though code and uncomment pygame_sdl2 imports  
-if the game doesn't run correctly try restarting spyder  
2. install java sdk  
3. go to rapt directory  
	> cd /c/Users/Chris\ Minar/Documents/rapt  
4.install android sdk  
	> python android.py installsdk  
5. build game for phone  
	> python android.py configure "/c/Users/Chris\ Minar/Documents/Python/python_android_game_tutorial"  
-full name: android test  
-short name: android test  
-package name: chris.android_test  
-human-readable version: 1.0  
-version code: 100  
-orientation: 1  
-expansion apk: 1  
-android version: 3  
-application layout: 1  
-include source code: no  
-permisions: vibrate  
-sqlite3: no  
-PIL: no  
6. prepare phone for game  
-install phone drivers on computer  
-turn on developer mode on phone (google for your phone)  
7. install game on phone (this will take a few minutes) 
	> python android.py --launch build /c/Users/Chris\ Minar/Documents/Python/python_android_game_tutorial release install  


Documentation:  
rapt: https://github.com/renpytom/rapt-pygame-example  
pygame_sdl2: http://pygame-sdl2.readthedocs.io/en/latest/  
pygame: https://www.pygame.org/wiki/index  
