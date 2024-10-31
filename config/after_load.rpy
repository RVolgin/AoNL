init 9999:
    # Добавляем наш обработчик в список вызовов после загрузки
    $ config.after_load_callbacks.append(aonl_after_load)
    # Сохраняем текущие значения курсора и заголовка окна
    $ aonl_config_mouse_backup = config.mouse
    $ aonl_config_window_title_backup = config.window_title
    
init python:
    def aonl_after_load():
        global save_name
        global aonl_config_mouse_backup
        global aonl_config_window_title_backup
        # Если загружаем сохранение из ИНЖ, то восстанавливаем курсор и заголовок окна для нашего мода
        if save_name.find(u'Искусство новой жизни') != -1:
            config.mouse = {'default' : [(aonl_imgs + "misc/cursor.png", 0, 0)]}
            config.window_title = u"Искусство новой жизни"
        # Это не наше сохранение, восстанавливаем значения по умолчанию, которые были сохранены при запуске игры
        else:
            config.mouse = aonl_config_mouse_backup
            config.window_title = aonl_config_window_title_backup