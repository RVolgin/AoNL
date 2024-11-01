label aonl_prologue:
    $ aonl_chapter(0)
    $ prolog_time()
    play music music_list["a_promise_from_distant_days_v2"] fadein 3
    $ renpy.pause(3)
    scene anim prolog_1 with dissolve
    window show
    "Вот уже шестнадцать лет я жила обычной жизнью как одна из тысячи жителей моего — и не только моего — города."
    "День ото дня школа, затем Школа Искусств и снова дом."
    "Наверное, если бы проводился эксперимент по нахождению истинного серого цвета, моя жизнь вполне бы подошла под это значение."
    "Но я не могу пожаловаться на то, что это как-то давило на меня или мешало, вовсе нет."
    "Я свыклась с обыденностью, и это постоянство стало для меня ключом ко внутреннему спокойствию. Из-за этого я не слишком часто проявляла эмоции, разве что рисование картин позволяло мне выражать мысли на холсте."
    "Наверняка это и послужило толчком к тому, чтобы поступить в Школу Искусств."
    "С самого начала мне лучше всего удавалось изображать природу, умиротворённую тишиной, не затравленную человеком, который, по своей натуре, стремился к завоеванию всего ради удовлетворения собственного эгоизма."
    "Зато когда приходилось рисовать людей, у меня тут же возникали проблемы.{w} Тяжело изображать человека, когда ты стараешься по минимуму контактировать с ними."
    "Из-за моей отрешённости от общества меня многие называли странной и не слишком уж торопились понимать."
    "Иногда это доставляло неприятности, ведь всегда найдутся те, для кого необычность человека — нечто сродни неполноценности, что даёт им повод для издевательств."
    "В один момент это послужило причиной того, что я замкнулась в себе окончательно, стараясь никого не подпускать близко."
    "Со временем одиночество стало для меня абсолютно привычным, и я уже была готова смириться с тем, что всю жизнь проведу, прячась в коконе внутренней самозащиты, который я создала вокруг себя, дабы никто и никогда не узнал то, о чём я думаю, чем живу и о чём мечтаю."
    "Я попросту разочаровалась в людях и уже не верила, что появится хоть кто-то, кто сможет понять меня и принять. Так я и жила — простая, тихая, серая мышка… Лена Тихонова."
    window hide
    scene bg black with fade3
    
    scene bg ext_camp_entrance_night
    show owl:
        pos (931, 88)
    show prologue_dream
    with fade3
    window show
    "Но однажды, весь цикл постоянной серой, скучной жизни начал нарушаться: я стала наблюдать странные сны."
    "Каждую ночь, ложась спать, я видела необычные кадры, изображающие некое место, сильно напоминающее пионерлагерь времён Советского Союза."
    "Все эти снимки никогда не складывались в единую картину, напоминая, скорее, не смонтированные в полноценное видео куски киноплёнки."
    "И каждый раз мне открывались всё новые места, раз за разом проплывая в сознании застывшими в статике деревьями, домами, мальчишками и девочками, одетыми в пионерскую форму."
    "И так снова и снова.{w} Пока однажды не случилось то, чего я никак не ожидала: все мои сны из разрозненных кусочков мозаики начали складываться вместе в один долгий сон, в котором оживает всё, что я видела раньше…"
    window hide
    stop music fadeout 3
    scene bg black with fade3
    $ renpy.pause (3)
    jump aonl_day1
