init 2:
    # Персонажи

    $ colors['aonl_d_golos'] = {'night': (225, 221, 125, 255), 'sunset': (225, 221, 125, 255), 'day': (225, 221, 125, 255), 'prolog': (225, 221, 125, 255)}
    $ names['aonl_d_golos'] = "Голос"
    $ store.names_list.append('aonl_d_golos')

    $ colors['aonl_d_unkman'] = {'night': (225, 221, 125, 255), 'sunset': (225, 221, 125, 255), 'day': (225, 221, 125, 255), 'prolog': (225, 221, 125, 255)}
    $ names['aonl_d_unkman'] = "Незнакомец"
    $ store.names_list.append('aonl_d_unkman')

    $ colors['aonl_deathman'] = {'night': (225, 221, 125, 255), 'sunset': (225, 221, 125, 255), 'day': (225, 221, 125, 255), 'prolog': (225, 221, 125, 255)}
    $ names['aonl_deathman'] = "Смерть"
    $ store.names_list.append('aonl_deathman')

    $ colors['aonl_woman'] = {'night': (225, 221, 125, 255), 'sunset': (225, 221, 125, 255), 'day': (225, 221, 125, 255), 'prolog': (225, 221, 125, 255)}
    $ names['aonl_woman'] = "Девушка"
    $ store.names_list.append('aonl_woman')

    # $ colors['aonl_dark_un'] = {'night': (225, 221, 125, 255), 'sunset': (225, 221, 125, 255), 'day': (225, 221, 125, 255), 'prolog': (225, 221, 125, 255)}
    # $ names['aonl_dark_un'] = "Тёмная Лена"
    # $ store.names_list.append('aonl_dark_un')


    # Функции

    
    transform shake_and_zoom1:
        subpixel True  # Для более плавной анимации
        parallel:  # Запускаем анимации одновременно
            linear 1.5 zoom 1.05 xalign 0.4 yalign 0.4 # Приближение фона сдвиг по осям 0.5 центр экрана

    transform shake_and_zoom2:
        subpixel True  # Для более плавной анимации
        parallel:  # Запускаем анимации одновременно
            linear 1.5 zoom 1.1 xalign 0.6 yalign 0.6 # Приближение фона сдвиг по осям 0.5 центр экрана

    transform shake_and_zoom3:
        subpixel True  # Для более плавной анимации
        parallel:  # Запускаем анимации одновременно
            linear 1.5 zoom 1.15 xalign 0.4 yalign 0.4 # Приближение фона сдвиг по осям 0.5 центр экрана

    transform shake_and_zoom4:
        subpixel True  # Для более плавной анимации
        parallel:  # Запускаем анимации одновременно
            linear 1.5 zoom 1.2 xalign 0.6 yalign 0.6 # Приближение фона сдвиг по осям 0.5 центр экрана

    transform shake_and_zoom5:
        subpixel True  # Для более плавной анимации
        parallel:  # Запускаем анимации одновременно
            linear 1.5 zoom 1.25 # Приближение фона
            
    transform from_bottom1:
        ypos 1.0 xpos 0.45  # Начальная позиция: внизу экрана
        linear 1.0 ypos 0.3 xpos 0.45  # Плавное движение вверх за 1 секунду до середины экрана
    
    transform from_bottom2:
        ypos 0.3 xpos 0.45  # Начальная позиция: внизу экрана
        linear 1.0 ypos 1.0 xpos 0.45 # Плавное движение вверх за 1 секунду вниз экрана
        
    transform from_bottom3:
        xpos -0.1  # Начальная позиция: слева экрана
        linear 2.4 xpos 2.0  # Плавное движение вправо за 1 секунду за переделы экрана

    transform from_bottom4:
        xpos -0.3  # Начальная позиция: слева экрана
        linear 2.4 xpos 2.0  # Плавное движение вправо за 1 секунду за переделы экрана
    
    transform from_mi1:
        linear 0.3 xpos 0.9 # Плавное движение за 0.3 секунду вправо
         
    transform from_mi2:
        linear 0.3 xpos 0.2  # Плавное движение за 0.3 секунду влево
    
    transform from_mi3:
        linear 0.3 xpos 0.5  # Плавное движение  за 0.3 секунду в центр
    




    image white_flash = Solid("#FFFFFF") # Белый прямоугольник
    
    image red_flash = Solid("#FF0000")  # Красный цвет  
    


    
    

    
    
    