#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import msvcrt
import time
from threading import Thread
from multiprocessing import Process

#FETCH SYSTEM PLATFORM INFO 
if "idlelib" in sys.modules:
    def cls(): 
        print("\n" * 100)
    def getch():
        input()
else:
    if sys.platform in ['win32' , 'cygwin']:
        from msvcrt import getch
        def cls():
            os.system('cls')
    else:
        def cls():
            os.system('clear')        
        def getch():
            input()

runtime = 0
t_p = 40
t_s = 5 
t_l = 15
t_due = t_p*60
m_due= 'Pomodoro'

def bridge():
    t_min = str(int(t_due/60))
    print('Typical Pomodoro Alpha 1')
    print('')
    print('Mode: ' + m_due)
    print('')
    print('Time Left: ')
    print(t_min + ':00')
    print('')
    print('Controls: ')
    print('[Space] to Start & Pause')
    print('[R] to Reset')
    print('[M] to Change Mode')
    print('[S] to Settings')
    input_char = str(getch())[2]
    if input_char == ' ' and m_due== 'Pomodoro':
        cls()
        typical_pomodoro(pomodoro=t_p, short=t_s, long=t_l)
    elif input_char == ' ':
        cls()
        game_start()
    elif input_char.upper() == 'M':
        cls()
        mode_select()
    elif input_char.upper() == 'S':
        cls()
        settings()
    else:
        cls()
        bridge()
        

def settings():
    global t_p, t_l, t_s
    print('Typical Pomodoro Alpha 1')
    print('')
    print('Select from 1, 2, 3 or 4:')
    print('1. Pomodoro - ' + str(t_p) + ' min')
    print('2. Short Break - '+ str(t_l) + ' min')
    print('3. Long Break - '+ str(t_s) + ' min')
    print('4. Return')
    input_char = str(getch())[2]
    if input_char == '1':
        cls()
        print('Typical Pomodoro Alpha 1')
        print('')
        print('1. Pomodoro - ' + str(t_p) + ' min')
        new_time = input('Change to (min): ')
        t_p = new_time
        cls()
        settings()
    elif input_char == '2':
        cls()
        print('Typical Pomodoro Alpha 1')
        print('')        
        print('2. Short Break - '+ str(t_l) + ' min')
        new_time = input('Change to (min): ')
        t_s = new_time
        cls()
        settings()
    elif input_char == '3':
        cls()
        print('Typical Pomodoro Alpha 1')
        print('')
        print('3. Long Break - '+ str(t_s) + ' min')
        new_time = input('Change to (min): ')
        t_l = new_time
        cls()
        settings()
    else:
        cls()
        settings()
    
def mode_select():
    global t_due, m_due
    print('Typical Pomodoro Alpha 1')
    print('')
    print('Select from 1, 2, 3 or 4:')
    print('1. Pomodoro')
    print('2. Short Break')
    print('3. Long Break')
    print('4. Return')
    input_char = str(getch())[2]
    if input_char == '1':
        cls()
        runtime = 0
        t_due = t_p*60
        m_due= 'Pomodoro'
        bridge()
    elif input_char == '2':
        cls()
        runtime = 0
        t_due = t_s*60
        m_due= 'Short Break'
        bridge()
    elif input_char == '3':
        cls()
        runtime = 0
        t_due = t_l*60
        m_due= 'Long Break'
        bridge()
    elif input_char == '4':
        cls()
        bridge()
    else:
        cls()
        mode_select()
        
def typical_pomodoro(pomodoro, short, long):
    global runtime, t_due, m_due
    if runtime >= 0 and runtime < 4:
        t_due = pomodoro * 60
        m_due = 'Pomodoro'
        runtime += 1
    elif runtime < 0:
        t_due = short * 60
        m_due = 'Short Break'
    elif runtime == 4:
        t_due = long * 60
        m_due = 'Long Break'
        runtime = 0    
    runtime *= -1
    game_start()

def game_start():    
    global t_due, m_due
    cls()
    thread_1 = Thread(target=screen, args=())
    thread_2 = Thread(target=stopwatch, args=())
    thread_1.start()
    time.sleep(0.2)
    thread_2.start()
    controls()
 
flag_mode_select = False
flag_paused = False
flag_mode_select = False
flag_refresh_rate = False
flag_settings = False
flag_menu = True

def controls():
    input_char = str(getch())[2]
    global flag_paused, flag_mode_select, runtime, t_due, m_due
    if input_char == ' ' and flag_paused == False:
        flag_paused = True
        controls()
    elif input_char == ' ' and flag_paused == True:
        flag_paused = False
        controls()
    elif input_char.upper() == 'M' and flag_mode_select == False:
        flag_menu = False
        flag_mode_select = True
        controls()
    elif input_char == '1' and flag_mode_select == True:
        if m_due != 'Pomodoro': 
            runtime = 0
            t_due = t_p*60
            m_due= 'Pomodoro'
        flag_mode_select = False
        flag_menu = True
        game_start()
        controls()
    elif input_char == '2' and flag_mode_select == True:
        if m_due != 'Short Break': 
            runtime = 0
            t_due = t_s*60
            m_due= 'Short Break'     
        flag_mode_select = False
        flag_menu = True
        game_start()
        controls()
    elif input_char == '3' and flag_mode_select == True:
        if m_due != 'Long Break': 
            runtime = 0
            t_due = t_l*60
            m_due= 'Long Break'    
        flag_mode_select = False
        flag_menu = True
        game_start()
        controls()
    elif input_char == '4' and flag_mode_select == True:
        flag_mode_select = False
        flag_menu = True
        controls()        
    elif input_char.upper() == 'R':
        cls()
        thread.stop()
        flag_paused = True
        controls()
    else:
        cls()
        controls()

def stopwatch():
    global t_due
    while True:
        time.sleep(0.5)
        if not flag_paused:
            t_due -= 0.5
 
def screen():
    global t_min, t_sec
    print(t_due)
    while t_due: 
        cls()
        t_min = str(int(t_due / 60))
        if t_due % 60 >= 10:
            t_sec = str(int(t_due % 60))
        else:
            t_sec = '0' + str(int(t_due % 60))
        print('Typical Pomodoro Alpha 1')
        print('')
        print('Mode: ' + m_due)
        print('')
        print('Time Left: ')
        if flag_paused:
            print(t_min + ':' + t_sec + ' [PAUSED]')
        else:
            print(t_min + ':' + t_sec)
        print('')
        if flag_settings:
            print('Settings ')
            print('1. Mode Length.')
            print('2. Refresh Rate.') 
            print('3. Return')       
        if flag_mode_select:
            print('Mode Select')
            print('1. Pomodoro')
            print('2. Short Break')
            print('3. Long Break')
            print('4. Return')       
        if flag_refresh_rate:
            print('Settings - Refresh Rate')
            print('1. 2 FPS (Compatibility)')
            print('2. 5 FPS')
            print('3. 10 FPS')
            print('4. 20 FPS (Smooth)')
            print('5. Return')
        if flag_menu:
            print('Controls ')
            print('[Space] to Start & Pause')
            print('[R] to Reset')
            print('[M] to Change Mode')
            print('[S] to Settings')
        time.sleep(0.05)
        
        
def settings():
    global t_p, t_l, t_s
    print('Typical Pomodoro Alpha 1')
    print('')
    print('Select from 1, 2, 3 or 4:')
    print('1. Pomodoro - ' + str(t_p) + ' min')
    print('2. Short Break - '+ str(t_l) + ' min')
    print('3. Long Break - '+ str(t_s) + ' min')
    print('4. Return')
    input_char = str(getch())[2]
    if input_char == '1':
        cls()
        print('Typical Pomodoro Alpha 1')
        print('')
        print('1. Pomodoro - ' + str(t_p) + ' min')
        new_time = input('Change to (min): ')
        t_p = new_time
        cls()
        settings()
    elif input_char == '2':
        cls()
        print('Typical Pomodoro Alpha 1')
        print('')        
        print('2. Short Break - '+ str(t_l) + ' min')
        new_time = input('Change to (min): ')
        t_s = new_time
        cls()
        settings()
    elif input_char == '3':
        cls()
        print('Typical Pomodoro Alpha 1')
        print('')
        print('3. Long Break - '+ str(t_s) + ' min')
        new_time = input('Change to (min): ')
        t_l = new_time
        cls()
        settings()
    else:
        cls()
        settings()
        
if __name__ == '__main__':
    bridge()
    