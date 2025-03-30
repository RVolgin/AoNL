init python:
    mine_map = {
                "1":{
                    "1":["3","2"],
                    "2":["3","2"],
                    "3":["3","2"]
                    },
                "2":{
                    "1":["4","13"],
                    "4":["13","1"],
                    "13":["1","4"]
                    },
                "3":{
                    "1":["halt","5"],
                    "5":["1","halt"],
                    "halt":["5","1"]
                    },
                "4":{
                    "2":["5","6"],
                    "5":["6","2"],
                    "6":["2","5"]
                    },
                "5":{
                    "3":["7","4"],
                    "4":["3","7"],
                    "7":["4","3"]
                    },
                "6":{
                    "4":["9","12"],
                    "9":["12","4"],
                    "12":["4","9"]
                    },
                "7":{
                    "5":["10","8"],
                    "8":["5","10"],
                    "10":["8","5"]
                    },
                "8":{
                    "7":["10","9"],
                    "9":["7","10"],
                    "10":["9","7"]
                    },
                "9":{
                    "8":["11","6"],
                    "6":["8","11"],
                    "11":["6","8"]
                    },
                "10":{
                    "7":["halt","8"],
                    "8":["7","halt"],
                    "halt":["8","7"]
                    },
                "11":{
                    "9":["exit","12"],
                    "12":["9","exit"]
                    },
                "12":{
                    "13":["6","11"],
                    "6":["11","13"],
                    "11":["13","6"]
                    },
                "13":{
                    "2":["12","coalface"],
                    "12":["coalface","2"],
                    "coalface":["2","12"]
                    }
        }

    def aonl_mine_eval(direction):

        global point
        global previous_point
        global halt_visited
        global coalface_visited
        global back_to_start
        global mine_route
        global first_turn

        if direction == "left":
            old_point = point

            point = mine_map[point][previous_point][0]
            previous_point = old_point
        elif direction == "right":
            old_point = point

            point = mine_map[point][previous_point][1]
            previous_point = old_point

        if point == "exit":
            renpy.jump("aonl_mine_exit")
        elif point == "coalface":
            point = "13"
            previous_point = "coalface"
            renpy.jump("aonl_mine_coalface")
        elif point == "halt":
            if previous_point == "10":
                point = "3"
                previous_point = "halt"
                renpy.jump("aonl_mine_halt")
            elif previous_point == "3":
                point = "10"
                previous_point = "halt"
                renpy.jump("aonl_mine_halt")
        elif back_to_start and point == "1":
            renpy.jump("aonl_mine_return_to_start")
        else:
            back_to_start = True
            renpy.jump("aonl_mine_crossroad")


label aonl_day4_alt:

    if aonl_un_story:
        call aonl_new_chapter(4, "четвёртый", "Я не боюсь ни темноты, ни смерти —\nПока ты рядом, ничему не испугать!\nЛишь одного страшусь я в этой жизни — \nТобою недооценённой стать…")

    if aonl_sl_story:
        call aonl_new_chapter(4, "четвёртый", "Стою в тени, тобой забыта\nМогу лишь взглядом проводить\nКак ты ушёл с лесною девой\nВо тьму пещер желанье укрепить")

    $ prolog_time()
    $ persistent.sprite_time = "night"
    if aonl_sl_story:
        scene cg un_dance1
        show prologue_dream
        with fade2
        play music aonl_Lena_dream_1 fadein 2
        play ambience ambience_lake_shore_night fadeout 1 fadein 2
        window show
        "Юноша рядом со мной."
        "Нежно приобнимает за талию." 
        "Мы кружимся в медленном танце среди звёзд." 
        "Где-то на краю слуха плещутся волны." 
        "Но окружающая обстановка мало волнует." 
        "Главное вместе с ним, в его руках." 
        "Он аккуратно ведёт меня в танце, а я, стесняясь, отвожу взгляд, щеки горят пожаром." 
        "Семён притягивает ближе за талию." 
        "Поднимаю глаза, наши губы в паре сантиметрах друг от друга." 
        "Я так мечтала об этом…" 
        "Неосознанно, где-то внутри себя." 
        "И, похоже, что именно так всё и должно случиться!" 
        "Я готова отдать всё на свете за то, чтобы это сладкое мгновение никогда не заканчивалось..."
        window hide
        stop ambience fadeout 2
        scene cg d3_sl_dance
        show prologue_dream
        with flash
        window show
        "Но в глубине души..."
        "Осознаю, что всё было совершенно не так."
        "Реальность довольно жестока."
        "Жалко, что она может вторгаться даже в твои сны..."
        window hide
        scene bg int_house_of_un_night
        show aonl_un25 smile future_winter
        show prologue_dream
        with flash
        window show
        "Открыв глаза, я увидела через застилающие слёзы себя взрослую рядом с кроватью." 
        "Наверное, ещё сплю."
        "Женщина погладила меня по волосам и щеке, вытерла слёзы из глаз."
        "Стало чуть легче, но в груди по-прежнему больно."
        aonl_un25 "Бедненькая моя, тяжко?"
        un "Очень."
        aonl_un25 "Так бывает. Не всегда, получается, поступить правильно и получить своё счастье."
        un "А я могла быть счастливой?"
        aonl_un25 "Конечно. Не всё, но многое зависит от нас самих."
        un "Как же нужно было поступить?"
        aonl_un25 "Сама не знаю, но другой путь возможен, только не в этот раз."
        un "А что же теперь?"
        aonl_un25 "Теперь отпусти, может жизнь даст ещё один шанс."
        un "Мне тяжело отпустить, очень больно и горько."
        aonl_un25 "Знаю. Мы ведь с тобой одно и тоже."
        un "Я сошла с ума?"
        aonl_un25 "Нет."
        "Женщина снисходительно улыбнулась."
        window hide
        stop music fadeout 2

    if aonl_un_story:
        scene cg aonl_d6_un_dance
        show prologue_dream
        play music aonl_Lena_dream_1 fadein 2
        with fade2
        window show
        "Места, где видим любимого человека, приобретают лично для нас особое значение." 
        "Как и всё, что с ним связано." 
        "Любые, казалось бы, незначительные события благодаря любимому человеку могут оставаться в твоём сердце навечно."
        "И даже одна мысль о нём. Импульс, мгновенно сверкнувший в разуме, подобно молнии…"
        "Я стою рядом с ним. Он нежно приобнял за талию." 
        "От касаний юноши словно таю и улетаю куда-то далеко-далеко." 
        "Но хочется большего! Только один раз, всего один раз."
        "Вот его волосы, его лоб, губы. Сёма наклоняется ко мне." 
        "Я закрываю глаза и тянусь на встречу, ресницы мелко дрожат от предвкушения."
        "Сейчас, это случится сейчас…"
        "Легкий влажный поцелуй касается моих губ, словно трепещущие крылья бабочки."
        "Мощный разряд тока пробивает с головы до ног, связь с реальностью становится всё более зыбкой."
        "Я отвечаю." 
        "Робко, нежно, боясь спугнуть своей настойчивостью, но мне хочется ЕЩЁ!"
        "Он обнимает за талию, моя рука обвивает его шея, ложась на плечо, твердое как камень, плечо настоящего мужчины, МОЕГО МУЖЧИНЫ!"
        "Пальцы второй руки погружаются в волосы."
        "Мягкие, шелковистые, так приятно, когда они скользят между пальчиков."
        "Я теряю последние остатки стеснения и прижимаю его голову чуть сильнее." 
        "Наши языки находят друг друга, сплетаясь в танце любви и страсти."
        th "ДА! ВОТ ТАК! ЕЩЁ! ПРОШУ ЕЩЁ! НЕ ОСТАНАВЛИВАЙСЯ!"
        "Связь с миром теряется окончательно, в голове белой вспышкой взрывается бомба, лишая и слуха, и зрения, оставляя лишь чувство блаженства и эйфории."
        window hide
        scene anim prolog_1
        show prologue_dream
        with dissolve
        window show
        #Здесь ЦГ можно убрать и поставить черный экран с помехами
        aonl_un25 "Лена, Лена…"
        th "Кто-то зовёт по имени, Сёма? Да нет, мы же целуемся..."
        aonl_un25 "Лена, Лена…"
        window hide
        scene bg black with dissolve
        scene bg int_house_of_un_night
        show aonl_un25 smile future
        show prologue_dream
        show unblink 
        pause 1
        window show
        "Я открываю глаза и вижу себя взрослую. Она сидит возле кровати и нежно гладит мои волосы."
        "В голове проносятся воспоминания другой жизни и рассказ девочек на площади."
        "Я всё вспомнила!"
        show aonl_un25 smile2 future with dspr
        aonl_un25 "А мы оказывается, те ещё кокетки!"
        "Моя взрослая версия тихонько хихикнула, приложив ладошку ко рту."
        un "Ты видела?"
        show aonl_un25 smile3 future with dspr
        aonl_un25 "Конечно, у нас же одна память на двоих. Сёма очень хороший."
        "Она слегка покраснела, смущённо опустив глаза."
        un "В этот раз… У нас получится?"
        "Я слегка заикаясь спросила то, что волновало больше всего на свете."
        show aonl_un25 smile future with dspr
        aonl_un25 "Не знаю, пока всё идёт хорошо. Но чувствую, вскоре наступит момент, определяющий очень многое."
        un "Какой момент, что именно?"
        "Её слова меня не на шутку испугали."
        th "Неужели всё может рухнуть?"
        show aonl_un25 sad future with dspr
        aonl_un25 "Не знаю, честно не знаю. Главное не упусти свой шанс, Лена."
        stop music fadeout 2
        window hide
        
    $ day_time()
    $ persistent.sprite_time = "day"
    play sound sfx_close_door_1
    scene bg white with Dissolve(.25)
    scene bg int_house_of_un_day
    play ambience ambience_int_cabin_day fadein 2
    show mi normal pioneer
    with Dissolve(.75)
    window show
    "Я проснулась от возвращения Мику так резко, что не сразу поняла, когда закончился сон."
    "Или это были грёзы наяву?"
    show mi cry_smile pioneer with dspr
    mi "Ты уже проснулась! Как удачно, подруженька. Ты представляешь, я шла умываться, но уронила зубной порошок прямо в траву. Можешь свой одолжить?"
    un "Подожди, дай полностью проснуться."
    "Я потянулась."    
    play sound [sfx_blanket_off_stand, sfx_bed_squeak1] 
    "Затем, встав с кровати, потрогала одежду на вешалках – просохла."
    "Одевшись, наконец, сориентировалась и смогла нормально ответить."
    un "На линейку не опоздала?"
    show mi smile pioneer with dspr
    mi "Опоздала милая. Но я сказала, что ты ночью лекарства разбирала, поэтому отдыхаешь." 
    mi "И тогда вожатая сказала, что всё хорошо."
    un "Спасибо, Мику."
    th "Как же она меня выручает."
    mi "На здоровье, Лен."
    un "Тебе ещё порошок нужен? Возьми у меня в тумбочке."
    show mi cry_smile pioneer with dspr
    mi "Спасибо, Леночка."
    un "Тебе спасибо, за то, что вчера форму постирала. Не знаю, чтобы без тебя делала."
    show mi smile pioneer with dspr
    mi "Да никаких проблем подруга, ведь друзья помогают друг другу. Семён, например, со мной порошком хотел поделиться, но представляешь, забыл его дома."
    un "Семён?"
    
    if aonl_sl_story:
        "Пусть и старалась о нём не думать, но каждое упоминание юноши отдавалось болью в душе."
        mi "Да, он тоже шёл умываться, а потом отправился в домик. Мне кажется, Сёма о чём-то мечтает, словно не здесь. Он даже, кажется, чуть-чуть улыбаться начал."
        un "Мне тоже пора умыться."
        mi "Да Лен, конечно. Сегодня на завтраке…"
        window hide
        play sound [sfx_open_dooor_campus_1, sfx_close_door_campus_1]
        pause 1
        play ambience ambience_camp_center_day fadeout 1 fadein 2
        scene bg ext_house_of_un_day with dissolve
        pause 1
        scene bg ext_houses_day with dissolve
        pause 1
        scene bg ext_house_of_mt_day
        show sl normal pioneer far 
        with dissolve
        window show
        "Выйдя из домика, оборвала пулемётную речь Мику и увидела Славю, заходящую в домик вожатой."
        play sound [sfx_open_dooor_campus_1, sfx_close_door_campus_1]
        hide sl with dissolve
        th "Зачем она туда идёт с утра пораньше? Какие-то важные мероприятия запланированы?"
        th "А нет, с вожатой ведь Семён живёт, она к нему наверно."
        th "Не моё дело."
        window hide
        scene bg ext_washstand_day with dissolve
        pause 1
        scene bg ext_washstand2_day with dissolve
        play sound sfx_open_water_sink
        pause 1
        play sound_loop sfx_water_sink_stream
        window show
        "Холодная вода освежила голову. Стало чуть легче. Теперь поняла, что делать."
        th "Проведу спокойно оставшиеся 4 дня в лагере, избегая Семёна, и поеду домой, попытавшись забыть обо всём. Мне уже ничего не исправить."
        window hide
        window hide
        stop sound_loop
        play sound sfx_close_water_sink
        scene bg ext_house_of_un_day with dissolve
        pause 1
        play sound [sfx_open_dooor_campus_1, sfx_close_door_campus_1]
        pause 1
        play ambience ambience_int_cabin_day fadeout 1 fadein 2
        scene bg int_house_of_un_day with dissolve
        window show
        "Вернувшись, обнаружила, что Мику нет, а мой дневник лежит открытым на столе со вчерашнего дня."
        th "Ну блииииин — вот же я дура! Надеюсь, у Мику хватило такта не заглядывать в чужую тетрадь. В этот раз не забуду убрать."
        window hide
        scene cg aonl_un_diary with dissolve
        $ set_mode_nvl()
        play music aonl_lena_diary_writing fadein 2
        window show
        "«Дорогой дневник!{nw}"
        "Сегодня мне снился одновременно самый прекрасный и самый ужасный сон в жизни...{nw}" 
        "Только потеряв, я поняла, как много для меня значит Сёма.{nw}"
        "Уже поздно что-либо менять. Уверена, тогда сделаю только хуже.{nw}"  
        "Всё, что мне остаётся, это тихо уйти в тень, никому не мешая…»"
        window hide
        stop music fadeout 2
        $ set_mode_adv()
        window show
        scene bg int_house_of_un_day with dissolve
        "В этот раз, спрятав дневник под подушку, отправилась в столовую."
        window hide
    
    if aonl_un_story:
        "Напоминание о моём мужчине заставило сердце биться сильнее."
        un "Он умывается?"
        mi "Нет, уже закончил, а что?"
        un "Ничего Мику, просто самой надо привести себя в порядок."
        "Я взяла умывальные принадлежности и покинула домик вместе с Мику."
        window hide
        play ambience ambience_camp_center_day fadeout 1 fadein 2
        scene bg ext_washstand2_day with fade2
        play sound sfx_open_water_sink
        pause 1
        play sound_loop sfx_water_sink_stream
        window show
        "Холодная вода освежила голову, вернув трезвое мышление."
        th "Возможно, он ещё в домике. А значит, я могу к нему зайти, и мы…"
        th "Что мы?"
        "Я толком не знала, что будем делать, но чувствовала настоятельную потребность встретиться." 
        "Ведь он тоже мне обрадуется!"
        window hide
        stop sound_loop
        play sound sfx_close_water_sink
        pause 1
        play ambience ambience_int_cabin_day fadeout 1 fadein 2
        scene bg int_house_of_un_day with fade2
        window show
        "Зайдя домой, сложила гигиенические принадлежности, повертелась у зеркала проверяя как выгляжу. Поправила хвостики."
        "Окинула домик взглядом, проверяя, не забыла ли чего, и увидела открытый дневник на столе."
        th "Вот я дура!" 
        th "Надеюсь, у Мику хватило такта не заглядывать в чужую тетрадь." 
        th "В этот раз не забуду убрать."
        window hide
        scene cg aonl_un_diary with dissolve 
        # play sound (Пишет ручкой, можно взять из Четыре Горизонта: Зимней Сказке)
        $ set_mode_nvl()
        window show
        play music aonl_lena_diary_writing fadein 2
        "«Дорогой дневник!{nw}"
        "В этот раз мне приснился прекраснейший сон. Я танцевала с любимым мужчиной и в танце он подарил прекраснейший поцелуй! Ах, как же это хорошо... Мечтаю, чтобы у нас всё сложилось хорошо. Я готова отдать за это жизнь! Вот только почему-то на самом интересном месте сон прервался и потом со мной кто-то говорил…{nw}"
        "Не могу вспомнить кто, опять какие-то провалы.»"
        window hide
        stop music fadeout 2
        $ set_mode_adv()
        scene bg int_house_of_un_day with dissolve
        window show
        "Спрятав дневник, в очередной раз поправила причёску и пошла к Сёме."
        window hide
        play sound [sfx_open_dooor_campus_1, sfx_close_door_campus_1]
        play ambience ambience_camp_center_day fadeout 1 fadein 2
        pause 1
        scene bg ext_house_of_un_day with dissolve
        pause 1
        scene bg ext_houses_day with dissolve
        pause 1
        scene bg ext_house_of_mt_day with dissolve
        window show
        "Вот и он. Я ощутила легкое волнение, стоя перед дверью." 
        "Собралась с духом, постучала и вошла, совсем забыв спросить разрешения."
        th "Блин."
        window hide
        play sound [sfx_open_dooor_campus_1, sfx_close_door_campus_1]
        play ambience ambience_int_cabin_day fadeout 1 fadein 2
        pause 1
        scene bg int_house_of_mt_day with dissolve
        show pi normal aonl_pioneer with dissolve
        window show
        un "Доброе утро…"
        show pi upset aonl_pioneer with dspr
        me "Доброе…"
        "Сёма смутился, словно не рад меня видеть."
        me "Ольгу Дмитриевну ищешь, наверное?"
        un "Да нет…{w} То есть да…"
        th "Блин, что я несу!"
        "Я смутилась и опустила глаза."
        th "Он мне не рад?"
        show pi normal aonl_pioneer with dspr
        me "А её нет."
        un "А, ну, ладно тогда…{w} Я пойду."
        me "Угу…"
        window hide
        play sound [sfx_open_dooor_campus_1, sfx_close_door_campus_1]
        play ambience ambience_camp_center_day fadeout 1 fadein 2
        pause 1
        scene bg ext_house_of_mt_day with dissolve
        window show
        "Закрыв дверь, я отправилась в столовую, погружённая в свои мысли."
        th "Неужели мне всё это приснилось? Да нет, мы танцевали и наяву." 
        th "И казалось, он тоже рад." 
        th "Но сейчас Сёма ведёт себя так, будто ему танец абсолютно безразличен."
        th "Может, я просто выдала желаемое за действительное и на самом деле совсем не нравлюсь юноше?"
        window hide
        
    scene bg ext_dining_hall_near_day with fade2
    window show
    play music music_list ["into_the_unknown"] fadein 2
    "У входа меня встретила толпа пионеров, о чём-то возбуждённо перешёптывающаяся."
    show el normal pioneer with dissolve
    el "Доброе утро Лен, ты Шурика не видела?"
    un "Доброе утро Серёж, нет, не видела. А он пропал?"
    show el sad pioneer with dspr 
    el "Видимо да, с утра его найти не могу, сначала думал он в клубе, но там его нет."
    un "Может, Саша просто гуляет?"
    el "Нет Лен. Ладно, я побегу."
    hide el with dissolve
    th "Конечно печально, внезапное исчезновение товарища, и всё же нельзя делать такие скоропалительные выводы." 
    th "Времени прошло совсем мало." 
    th "Может, Саша просто гуляет в лесу, а к завтраку или обеду найдётся."
    window hide
    play sound [sfx_open_door_1, sfx_close_door_1]
    pause 1
    play ambience ambience_dining_hall_full fadeout 1 fadein 2
    scene bg int_dining_hall_people_day with dissolve
    show mi sad pioneer with dissolve
    window show
    "Стоило сесть за мой любимый угловой столик, как на свободное место тут же приземлилась обеспокоенная Мику."
    mi "Лен, а ты Сашу не видела? Серёжа говорит, он с утра пропал, даже в клуб свой не заходил. Я так беспокоюсь, вдруг с ним, что-то случилось, а мы сидим тут и ничем ему не помогаем. Нужно как можно скорее его найти!"
    un "Меня уже спрашивал Серёжа, я не знаю, где он."
    mi "Жаль, я надеялась, ты в курсе или сможешь помочь. Я так боюсь за Сашу, Серёжа говорит так исчезать для него неестественно."
    un "Мику, но ведь прошло совсем мало времени. Возможно, он просто упал в пыль, сейчас стирает свою одежду в умывальнике, переоденется и придёт к концу завтрака."
    show mi upset pioneer with dspr
    mi "Ты так считаешь?"
    un "Да."
    show mi normal pioneer with dspr
    mi "Верно, я подожду до конца завтрака."
    "Дальше мы ели, что удивительно для Мику, молча."
    "Каждый раз, когда открывалась дверь столовой подруга вздрагивала и устремляла обеспокоенный взгляд туда."
    show mi sad pioneer with dspr    
    "И чем ближе приближался конец завтрака, тем грустнее становилась девушка."
    show bg int_dining_hall_day with dissolve
    play ambience ambience_dining_hall_empty
    stop music fadeout 2
    "Наконец все пионеры разошлись, а Мику всё так же продолжала смотреть в сторону входа."
    "Я осталась с ней из женской солидарности."

    mi "Он так и не пришёл."    
    "Казалось, подруга сейчас заплачет."
    un "Мику."
    "Я положила руку на её ладонь, стараясь успокоить."
    un "Может он уже в клубе с Серёжей, пойдём туда и проверим."
    "Мику шмыгнула носом."
    mi "Хорошо."
    window hide
    play ambience ambience_camp_center_day fadeout 1 fadein 2
    scene bg ext_square_day with fade2
    show mi sad pioneer at left
    show el sad pioneer at right
    with dissolve
    window show
    "Далеко мы не ушли, навстречу выскочил обеспокоенный Электроник. Его вид говорил сам за себя, но спросить стоит."
    un "Серёж, а… Шурик нашёлся?"
    el "Нет. Вожатая уже всех отправила на поиски, пока глухо."
    show mi cry pioneer with dspr
    "Мику совсем пригорюнилась."
    th "Она девушка впечатлительная. Нужно срочно её отвлечь, пока дров не наломала."
    un "Мику, ты можешь помочь в поиске?"
    show mi serious pioneer with dspr 
    mi "Конечно могу, что нужно делать Лен?"
    un "Давай так, ты сейчас пойдёшь в музыкальный клуб, вдруг Шурик к тебе зайдёт. Перед обедом сходишь на остановку, проверишь там." 
    un "А я пойду на спортплощадку. Если не найдёшь Сашу, то возвращайся в клуб и продолжай дежурить, вдруг он к тебе заглянет после обеда." 
    un "Я пойду дальше искать, а как найду сразу прибегу к тебе."
    show mi normal pioneer with dspr
    mi "Леночка, ты такая добрая, спасибо."
    show mi upset pioneer with dspr
    mi "Вот только что я всё это время буду делать в клубе, пока ты не придёшь?"
    un "Ну… Ты можешь попеть песню и поиграть на гитаре."
    show mi cry_smile pioneer with dspr
    extend  " А Шурик, проходя мимо услышит и зайдёт."
    mi "Леночка!!!"
    "Мику аж подпрыгнула, захлопав в ладоши."
    mi "Ты такая умничка, спасибо тебе за идею!" 
    show mi upset pioneer with dspr
    extend " Вот только я не умею одновременно петь и играть."
    un "Придумай что-нибудь!"
    show mi smile pioneer with dspr
    mi "Хорошо, я побежала."
    hide mi with dissolve
    stop music fadeout 2
    "Мику скрылась в направлении клуба."
    th "Ух, теперь можно хоть немного расслабиться."
    el "Спасибо Лен, я в лесу тогда посмотрю."
    un "Хорошо."
    window hide
    play ambience ambience_soccer_play_background fadeout 1 fadein 2
    scene bg ext_playground_day with dissolve 
    window show
    "Я отправилась на площадку, как и обещала."
    "По полю бегали пионеры из младших отрядов и гоняли мячик, вряд ли Шурик здесь."
    "Для очистки совести решила сходить на пляж."
    window hide
    play ambience ambience_lake_shore_day fadeout 1 fadein 2
    scene bg ext_beach_day with dissolve
    show mt angry swim panama far at center with dissolve
    window show
    "Шурика так же не наблюдалось, лишь несколько пионеров плескались в воде, да Ольга Дмитриевна разговаривала с каким-то юношей в плавках."
    show pi normal aonl_swim at left with easeinbottom
    "Когда юноша приподнялся с земли, пожимая своими обгоревшими на солнце плечами... {w} Я узнала Семёна!"
    th "Какое у него стройное, подтянутое тело! Наверняка, спортом занимается…"
    "Я увлеклась любованием полуобнажённым парнем, выпав на некоторое время из реальности."
    "Семён направился в мою сторону, на ходу одеваясь."
    "Придя в себя, я резко развернулась и побежала в домик."
    window hide
    play ambience ambience_int_cabin_day fadeout 1 fadein 2
    scene bg int_house_of_un_day with dissolve
    
    if aonl_sl_story:
        window show
        "Я легла на кровать раскинув руки в стороны и стараясь отключиться от происходящего."
        "Шурик пропал." 
        "Печально, но надеюсь мальчик скоро найдётся." 
        "Остаётся лишь посидеть до конца дня и лечь на боковую, чтобы день прошёл быстрее, и я наконец поехала домой."
        show blink 
        "Сама не заметила, как глаза закрылись. {w} Предобеденный сон взял своё."
        window hide
    
    if aonl_un_story:
        window show
        "Я легла на кровать раскинув руки в стороны, раздумывая:" 
        "Что значу для Сёмы? {w} Кто я для него?"
        show blink 
        "За своими размышлениями совершенно не заметила, как веки сомкнулись."
        window hide
    
    stop ambience fadeout 2
    scene bg int_mine
    show prologue_dream
    with fade2
    $ prolog_time()
    $ persistent.sprite_time = "night"
    window show
    play music music_list ["torture"] fadein 2
    "Иду по подземному тоннелю." 
    "Повсюду деревянные опоры, а под ногами рельсы."
    th "Похоже на шахту. Как я сюда попала?"
    show sh rage pioneer at center behind prologue_dream with dissolve
    "Вдруг передо мной появился Шурик. {w} В руке он держал арматуру!"
    th "Что с ним?"
    "Саша направился ко мне размахивая арматурой."
    sh "Где вы?! Хватит издеваться!"
    un "Саша ты что? {w} Это я!"
    "Попыталась попятиться, но тело осталось на месте."
    sh "Хватит меня гонять налево, направо, налево, направо! Вы у меня получите!"
    "Он подошёл вплотную, размахивая арматурой, я закрыла глаза и голову руками."
    un "Он же меня убьёт! Спасите!!!"
    "Арматура просвистела над головой..."
    "И Саша, судя по звуку, прошёл дальше."
    hide sh with dissolve
    "Открыла глаза и увидела, что юноша прошёл сквозь меня, продолжая размахивать своим оружием."
    th "Я что, призрак?"
    aonl_un25 "Он заблудился и напуган."
    show aonl_un25 normal future_winter behind prologue_dream with dissolve
    "Обернувшись, увидела старую знакомую."
    un "Где я? {w} Как попала сюда?"
    aonl_un25 "Шахты."
    
    if aonl_sl_story:
        un "Зачем всё это рассказываешь?"
        show aonl_un25 serious future_winter with dspr
        aonl_un25 "В другой раз поймёшь."
        window hide

    if aonl_un_story:
        un "Ему нужна помощь?!"
        show aonl_un25 serious future_winter with dspr
        aonl_un25 "Да!"
        un "Тогда нужно идти!"
        aonl_un25 "Одна не справишься."
        window hide
    
    scene bg int_mine 
    show prologue_dream
    with dissolve
    pause 0.5
    scene bg int_catacombs_living
    show prologue_dream
    with dissolve
    pause 0.5
    scene bg int_catacombs_entrance
    show prologue_dream
    with dissolve
    pause 0.5
    scene bg aonl_ext_old_building_day
    show prologue_dream
    with dissolve
    pause 0.5
    scene bg ext_path2_day
    show prologue_dream
    with dissolve
    pause 0.5
    scene bg ext_square_day
    show prologue_dream
    with dissolve
    pause 0.5
    scene bg ext_houses_day
    show prologue_dream
    with dissolve
    pause 0.5
    scene bg ext_house_of_un_day
    show prologue_dream
    with dissolve
    pause 0.5
    scene bg int_house_of_un_day
    show prologue_dream
    with dissolve
    pause 0.5
    play ambience ambience_int_cabin_day fadein 2
    stop music fadeout 2
    scene bg int_house_of_un_day with flash    
    play sound sfx_body_bump
    with vpunch
    $ day_time()
    $ persistent.sprite_time = "day"
    window show
    "Меня швырнуло на кровать, от чего я упала на пол."
    th "Фух, это уже что-то новое. {w} Какой-то ужастик приснился, только не могу его вспомнить!"
    "Встав с пола, я отряхнулась и посмотрела на часы."
    "Обед закончился."
    th "Ну ничего, стройнее буду."
    "Голова раскалывалась, словно по ней били чугунной сковородкой."
    "Схожу к Виоле попрошу таблетку."
    window hide
    play ambience ambience_medstation_inside_day fadeout 1 fadein 2
    scene bg int_aidpost_day with fade2
    show pi normal aonl_pioneer with dissolve
    window show
    play music music_list ["everyday_theme"] fadein 2
    "Однако, в медпункте меня ждала вовсе не Виола."
    th "Сёма! Что он забыл у медсестры?" 
    th "Не хочу снова краснеть перед ним, как томат в теплице!" 
    th "Нужно держать себя в руках, сохранять спокойствие…"
    un "А медсестры здесь нет? Тогда попозже зайду…"
    show pi smile aonl_pioneer with dspr
    me "Я за неё!"
    me "На что жалуетесь?"
    "Сёма постарался улыбнуться, от чего мне стало спокойнее."
    un "Да ничего такого… Голова немного болит просто."
    me "Сейчас исправим."
    "Сёма начал рыться в шкафчиках, заняло это довольно много времени, но я решила дождаться."
    me "Нашёл!"
    "Юноша протянул таблетку анальгина."
    un "Спасибо…"
    "От его заботы я невольно улыбнулась."
    "После этого Сёма как-то странно уставился на меня, от чего я сильно смутилась."
    un "Что?"
    me "Слушай, а вот интересно, тебе понравилось бы такое?"
    "Он показал журнал моды на странице, где девушка носила кофточку и юбку. Довольно красивые."
    un "Да, наверное…"
    me "А сейчас это… Модно?"
    "Лично мне очень понравилось, но язык опять отказался нормально повиноваться."
    un "Наверное…"
    "Я смутилась ещё сильнее."
    un "А почему ты спрашиваешь?"

    if aonl_sl_story:
        show pi normal aonl_pioneer with dspr
        me "Да просто так."
        "…"

    if aonl_un_story:
        me "Мне кажется, на тебе это бы смотрелось прекрасно."
        # $ day4_un_compl = 1
        # $ lp_un = lp_un + 1
        window show
        th "Он считает меня красивой?! Я всё-таки ему нравлюсь?!"
        un "Спасибо…"
        me "Да не за что, я же правду говорю!"
        "От смущения уже не знала, куда прятать глаза."
        th "Он такой милый."
        
    show pi smile aonl_pioneer with dspr
    me "Как голова?"
    un "Лучше, спасибо."
    "Я улыбнулась и снова смогла нормально говорить."
    un "Я пойду."
    me "Удачи."
    stop music fadeout 2
    window hide
    play sound [sfx_open_door_1, sfx_close_door_1]
    play ambience ambience_camp_center_day fadeout 1 fadein 2
    pause 1
    scene bg ext_aidpost_day with dissolve

    if aonl_sl_story:
        window show
        "Выйдя наружу, облегчённо выдохнула."
        th "Какая же я дрянь." 
        th "Чужой парень, а смотрю на него как Надежда Крупская на Ленина." 
        th "Так хотелось с ним пообщаться подольше, но флиртовать с парнем подруги, дело подлое."

    if aonl_un_story:
        window show
        "Выйдя наружу, я буквально в припрыжку пошла по улице."
        th "Он такой классный! Такие комплименты красивые делает и главное искренне!"
        "Казалось, за спиной выросли крылья, и я вот-вот улечу к небесам!"
        window hide
        scene bg ext_square_day with dissolve
        show dv normal pioneer with dissolve
        window show
        "Встретив Алису, я поумерила шаг и опустила глаза к земле."
        "Рыжая проводила меня настороженным взглядом, но ничего не сказала."
        th "Обошлось."
    
    th "Схожу проверить, как там Мику в клубе."
    window hide
    scene bg ext_musclub_day with dissolve
    window show
    play music perebor fadein 3
    th "Судя по звуку гитары, подруга по-прежнему там."
    window hide
    play sound [sfx_open_door_1, sfx_close_door_1]
    play ambience ambience_music_club_day fadeout 1 fadein 2
    pause 1
    scene cg d4_mi_guitar with dissolve
    window show
    "Когда я зашла внутрь, девушка сидела, закрыв глаза и перебирая струны."
    "Я решила не мешать и тихонько присела, послушать музыку."
    "Подруга играла какую-то душевную мелодию, от которой по сердцу разливалось тепло."
    #play sound звук удара по струнам
    stop music
    play sound ydar_gitara
    "Вдруг Мику резко ударила по струнам и затихла, словно собираясь с мыслями."
    pause 2
    "Секунд 10 висела тишина, но вот девушка снова заиграла и начала петь!"
    $ renpy.movie_cutscene("art_of_new_life/video/Miku.ogv")
    #Тут вставить клип песню Мику с канала voicy chanel. Думаю, договоримся. (Песня о любви).
    "Когда подруга закончила, я не удержалась и зааплодировала."
    window hide
    scene bg int_musclub_day
    show mi surprise pioneer
    with dissolve
    window show
    play music music_list ["so_good_to_be_careless"] fadein 3
    #Вариант временный, не уверен
    mi "Лена, ты тут! Я совсем не заметила, как ты вошла. Давно сидишь?"
    un "С того момента, как ты петь начала. Очень понравилось."
    show mi smile pioneer with dspr
    mi "Спасибо, Лен."
    "Мику аж вся зарделась."
    un "Сама придумала?"
    show mi grin pioneer with dspr
    mi "Да, когда в лагерь приехала, придумала."
    un "Потрясающе. Я знала о твоих талантах, но не думала, что можешь настолько красиво петь и играть."
    show mi smile pioneer with dspr
    mi "Это благодаря Сёме."
    un "Сёме?" with vpunch
    "Я пошатнулась от этой новости."

    if aonl_sl_story:
        th "Неужели, Мику так изъяснялась в любви Семёну?" 
        th "Сначала Славя, теперь и Мику?" 
        th "Нет, только не это!" 
        th "А как же они будут делить его?" 
        th "Неужели, подругам придётся ссориться из-за парня!?"

    if aonl_un_story:
        th "Неужели, Мику так изъяснялась в любви Семёну?" 
        th "Нет, только не это!" 
        th "А как же мы будем делить его?" 
        th "Неужели, подругам придётся ссориться из-за парня?!"
        
    un "Д-давно ты к нему так относишься?"
    mi "К кому?"
    un "К Семёну, песня о любви ведь… для него?"
    "Я почувствовала, как на глаза стали наворачиваться слёзы."
    th "Ну почему судьба ко мне так не справедлива?"
    show mi shocked pioneer with dspr
    mi "Нет-нет-нет Лен ты что, с чего такие выводы? Одумайся!"
    un "Но… Но ты ведь сказала это всё благодаря ему."
    show mi laugh pioneer with dspr 
    mi "Ах вот ты про что!"
    "Девушка хохотнула."
    mi "Нет, я имела ввиду совсем другое."
    mi "Он помог мне с песней." 
    mi "Когда пошла на остановку там встретила Сёму и попросила, чтобы он сыграл на гитаре. А я спела, у меня одновременно не получалось. А как он ушёл, я попробовала уже сама всё исполнить и как видишь, вышло хорошо."
    un "А… Вот ты о чём."
    mi "Ага."
    "Девушка снова хохотнула."
    un "Мику, а для кого ты тогда её придумала в лагере?"
    show mi shy pioneer with dspr
    mi "Ну это… {w} Это для одного хорошего человека. Для друга."
    "Девушка сильно смутилась, пряча глаза."
    th "Наверно, не стоит развивать тему."
    play sound sfx_dinner_horn_processed
    un "Пойдём?"
    show mi smile pioneer with dspr
    mi "Да конечно, а то я совсем не обедала."
    un "Почему?"
    mi "Ну я же ждала Сашу, вдруг он придёт!"
    un "Но ведь нельзя себя морить голодом!"
    show mi normal pioneer with dspr
    mi "Ничего страшного, я же, как раз похудеть хотела. К тому же спасение товарища гораздо важнее. Ах да…"
    "Мику встрепенулась."
    mi "Сашу нашли?"
    show mi sad pioneer with dspr
    un "Вроде нет, пойдём в столовую узнаем точно."
    mi "Хорошо."
    "Девушка снова сникла."
    th "Неужели она так сильно переживает за товарища?" 
    "Лучше отвлечь её от грустных мыслей." 
    "Вот только как?"
    window hide
    play ambience ambience_camp_center_day fadeout 1 fadein 2
    scene bg ext_square_day
    show mi normal pioneer
    with fade2
    window show
    th "Генда?"
    "Что-то кольнула в памяти."
    th "А вот если…"
    un "Мику?"
    mi "Что?"
    un "А это правда, что памятник установили по инициативе твоего папы?"
    "Я кивнула в сторону Генды."
    show mi smile pioneer with dspr
    mi "Да, это мой папа постарался."
    "Девушка заметно оживилась."
    un "А что он за деятель?"
    mi "Не знала, что ты таким интересуешься! {w} Рассказать?"
    un "Конечно."
    show mi upset pioneer with dspr
    mi "С чего бы начать…"
    show mi normal pioneer with dspr
    extend " Ага, мой папа знал лично Генда-сана, застал его уже в преклонном возрасте… Он коммунист был, представляешь?" 
    mi"Советский Союз же воевал с Японией, причём дважды, еще, будучи Российской империей! И вряд ли подобные ему были в чести…"
    "Я не припомню всего, что мне рассказала Мику. Но с каким, же упоением можно было наблюдать за огоньком в раскосых глазках — её волновала и занимала тема, о которой она говорила."
    show mi serious pioneer with dspr 
    mi "…у него ещё жена погибла из-за ядерных бомбёжек в Хиросиме, но остался сын. То ли Синтъиро, то ли Синдзи его звали — не помню уже. В общем, они долго не виделись, но, когда наступили времена Карибского кризиса…" 
    mi "Генда-сан тогда возглавлял секретную службу по борьбе с пиратами и боевиками в Тихом океане, вот и зачислил сына в военно-воздушный подростковый отряд."
    un "Ужас! Неужели так можно с собственным ребёнком?"
    show mi upset pioneer with dspr
    mi "А что поделать? Такая работа была, что взрослым выполнять было не впору. Всего не упомню, но на фронте мальчик отвоевал около пяти лет и, ни в одном бою не проиграл. Когда ему было девятнадцать, он с невестой, тоже партизанкой, нападал на штаб крупной мафии где-то в Полинезии." 
    show mi smile pioneer with dspr
    mi "Силы были неравны, обоих серьёзно ранили, но те пали смертью храбрых, направив собственные аэропланы на вражескую базу. А Генда-сан вырастил их внебрачную дочку, написал мемуары и, кажется, четыре года назад помер."
    un "Очень интересно и трагично. Жаль, что всё так кончилось."
    "Мне стало очень горько от этой истории, возникло желание её изменить, чтобы она не была так пессимистична. Но ведь жизнь человека — никакая не сказка, а зачастую трагедия в несколько тысяч актов."
    th "О чём же ты думаешь, Генда, когда стоишь с этим лицом на площади?" 
    th "Тебе было стыдно за что-то в твоей биографии?" 
    th "Или ты устал от стольких событий?"
    window hide
    scene bg ext_dining_hall_away_day 
    show mi smile pioneer
    with dissolve
    pause 1
    scene bg ext_dining_hall_near_day
    show mi smile pioneer
    with dissolve
    window show
    un "И как ты можешь такие печальные истории рассказывать со спокойным видом?"
    mi "Я же наполовину японка, Лена! Наш народ, ютящийся на двух скромных островах, столько всего пережил, столько из этого воспел в фольклоре…" 
    mi "Я знала боевую подругу тех двух: её звали Сора Аски, после увольнения она стала учительницей и преподавала в моей начальной школе русский язык. В бою она потеряла глаз и потом носила протез…"
    un "Бедная женщина."
    mi "Согласна, ей тяжело пришлось. Но она не унывала, а продолжала помогать другим, стальная дама."
    stop music fadeout 2
    window hide
    play sound [sfx_open_door_2, sfx_close_door_1]
    pause 1
    play ambience ambience_dining_hall_full fadeout 1 fadein 2
    scene bg int_dining_hall_people_day 
    show mi smile pioneer at left
    with dissolve
    show mt normal pioneer at center behind mi
    with dissolve
    window show
    "Мы встретили вожатую, Мику тут же подскочила к ней."
    mi "Оленька, вы нашли Сашу? Я была на остановке, но его там нет, а ещё Сёма туда ходил. Потом дежурила в музыкальном клубе, надеялась, он зайдет, услышав, песню, если будет рядом, но Сашенька так и не пришёл. Я совсем расстроилась, но Лена сказала…"
    show mi sad pioneer with dspr
    mt "Пока не нашли!"
    "Вожатая прервала Мику."
    mt "Мне надо идти."
    hide mt with dissolve
    "Женщина скрылась из виду." 
    "Похоже, она не привыкла подолгу выносить Мику."
    mi "Лен, ты слышала, опять ничего."
    un "Да, слышала. Пока нужно найти место. {w} Чем быстрее поедим, тем раньше вернёмся к поискам."
    show mi normal pioneer with dspr 
    mi "Лена, давай сюда! Смотри – целых три стула!"
    "Она потянула меня в сторону Семёна."
    th "Судьба, словно целенаправленно сталкивает нас."
    show pi normal aonl_pioneer at center behind mi with dissolve
    un "Тут свободно?"
    me "Да, садитесь."
    un "Спасибо…"
    show mz normal pioneer glasses at right with easeinright 
    "Не успели мы расположиться, как за столик приземлилась Женя."
    mz "Я сяду тут. Больше некуда."
    show pi upset aonl_pioneer with dspr
    me "Конечно, располагайтесь…"
    th "Как-то грустно он это сказал."
    mz "Что?!"
    me "Ничего…"
    "Пока они обменивались любезностями, незаметно оправила юбку."
    un "Ой, я ключ, кажется, забыла…"
    show mi smile pioneer with dspr
    mi "Ничего страшного, возьми мой!"
    show pi normal aonl_pioneer with dspr
    me "А вы… вместе живёте?"
    mi "Да, конечно! А ты не знал? {w} Наш домик самый крайний. То есть самый дальний от столовой. Ну, то есть самый последний."
    mz "Нашли своего Шурика?"
    show mi sad pioneer with dspr
    me "Нет."
    show mz bukal pioneer glasses with dspr
    mz "Небось, в деревню убежал за сигаретами. Или за водкой."
    show pi surprise aonl_pioneer with dspr
    me "В деревню?"
    mz "А что такого?"
    me "Значит, здесь есть поблизости деревня?"
    mz "Наверное…"
    show pi normal aonl_pioneer with dspr
    me "То есть, ты точно не знаешь?"
    show mz angry pioneer glasses with dspr
    mz "Да какое мне дело?"
    me "Но здесь же должны быть какие-то населённые пункты поблизости?"
    show mz normal pioneer glasses with dspr
    mz "Слушай…"
    me "Слушаю."
    show mz bukal pioneer glasses with dspr
    mz "Не знаю я! Дай спокойно поесть."
    "На этой феерической ноте диалог закончился."
    "Оставшееся время пришлось слушать, как Мику говорит о каких-то малозначительных вещах."
    "Я попыталась доесть побыстрее, чтобы сбежать от Сёмы. Уж слишком сильно смущалась в его компании, не хватало, чтобы девочки заметили."
    window hide

    if aonl_sl_story:
        $ sunset_time()
        $ persistent.sprite_time = "sunset"
        play ambience ambience_camp_center_day fadeout 1 fadein 2
        scene bg ext_square_sunset with fade2
        window show
        th "И почему судьба постоянно сводит нас вместе? Славя явно заинтересована Семёном, парень тоже оказывает ей внимание, а меня совсем не замечает."
        th "Вот и пусть будут счастливы без моего присутствия. Зачем нам постоянно видеться, друзьями быть?"
        window hide
        scene bg ext_houses_sunset with dissolve
        window show
        th "Только душу мне бередить. Кто-то однажды сказал, любовь не пятнают дружбой. {w} Видимо, этот человек был в моём положении."
        window hide

    if aonl_un_story:
        $ sunset_time()
        $ persistent.sprite_time = "sunset"
        play ambience ambience_camp_center_evening fadeout 1 fadein 2
        scene bg ext_square_sunset with fade2
        window show
        th "Блин!" 
        th "Я так хочу с ним провести время, но либо рядом находится кто-то посторонний, либо теряю дар речи и мысли разбегаются."
        window hide
        scene bg ext_houses_sunset with dissolve
        window show
        th "Эх, вот бы мы остались наедине!"
        window hide
    
    
    
    play sound sfx_muffled_explosion
    with vpunch
    window show
    play music music_list ["into_the_unknown"] fadeout 2
    th "Что это?"
    th "Как будто взрыв на площади." 
    th "Неужели здесь могло, что-то случиться?"
    show sl serious pioneer with dissolve
    "Мимо пробежала Славя."
    sl "Лена, бежим, может потребоваться помощь!"
    un "Да."
    window hide
    scene bg ext_square_sunset with dissolve
    window show
    "Прибежав на место, мы увидели копоть на памятнике." 
    "Видимо, взрывали его, но Генда устоял."
    show mt rage pioneer panama with dissolve
    mt "Ну, и кто это сделал?"
    "Вожатая начала допрос прибежавших пионеров. По толпе пошло перешёптывание."
    show mt angry pioneer panama with dspr
    mt "Вы двое, ко мне!"
    th "Кому это она?"
    show dv normal pioneer at left 
    show us dontlike pioneer behind dv at fleft
    with dissolve
    th "Логично."
    us "А что сразу я?"
    dv "Если вы считаете…"
    mt "Двачевская! Покажи-ка руки!"
    dv "А что с ними не так?"
    "Приглядевшись, увидела, что они в саже."
    mt "Теперь понятно… {w} Из чего бомбу делала?!"
    "После раздумья Алиса гордо выпалила."
    show dv laugh pioneer at left with dissolve
    dv "Активированный уголь, сера, селитра!"
    mt "И почему именно памятник? Чем тебе помешал уважаемый, заслуженный человек? Борец за права…"
    show el smile pioneer at right with easeinright
    el "Нашёл, нашёл…"
    show dv normal pioneer at left with dissolve
    "Экзекуцию прервал Электроник, прибежавший на площадь, размахивая ботинком."
    el "Вот!"
    el "Это ботинок Шурика!"
    show mt normal pioneer panama with dspr
    mt "Так успокойся! Расскажи подробно, где ты его нашёл!"
    show el sad pioneer with dspr
    el "В лесу. На тропинке в старый лагерь!"
    th "Тот самый старый лагерь?"
    "По толпе прошёл ропот."
    all "Старый лагерь… Старый лагерь…"
    mt "Ты уверен?"
    show el normal pioneer with dspr
    el "Абсолютно!"
    show pi normal aonl_pioneer at fright with dissolve
    me "А что такого в этом старом лагере?"
    th "Ой и Сёма здесь!"
    mt "Да ничего такого на самом деле…"
    show el sad pioneer with dspr 
    el "Одна из легенд «Совёнка» гласит, что там живёт привидение молодой вожатой, которая влюбилась в пионера, но, не найдя взаимности, покончила с собой…"
    show us grin pioneer with dspr
    us "Сделала харакири кухонным ножом. А мальчика этого на следующий день сбил автобус!"
    show pi surprise aonl_pioneer with dspr
    me "Автобус?"
    show el serious pioneer with dspr
    hide dv with dissolve
    hide us with dissolve
    show sl sad pioneer at left with dissolve
    el "Но наука не допускает существования привидений, поэтому опасаться там нечего!"
    mt "Всё равно кто-то должен туда пойти!"
    "Люди стали быстро расходиться."
    sl "Ольга Дмитриевна, ночь уже почти! Может, завтра."
    show mt angry pioneer panama with dspr
    mt "А если ночью… ночью с ним что-нибудь случится… Нет! Сегодня! Сейчас!"
    show pi normal aonl_pioneer with dspr
    me "Кстати, а где это?"
    "Серёжа примерно объяснил."
    hide el with dissolve
    "Вожатая перевела взгляд на Семёна."
    show pi upset aonl_pioneer with dspr
    me "Если вы думаете, что я…"
    mt "Ты один здесь остался из мужчин."
    th "Действительно, даже Серёжа ушёл."
    "Сёма явно занервничал, и это понятно. Любому будет страшно."
    "Он перевёл взгляд на девчат, словно раздумывая кого из нас попросить о помощи."

    if aonl_un_story:
        window hide
        menu: 
            "Пойти с Семёном": 
                $ aonl_un_story = True

            "Опустить глаза и не встречаться взглядом":
                $ aonl_sl_story = True
                $ aonl_un_story = False
            #Катапульта на одиночку рут Слави. Если до этого проиграли в карты продолжение рута Слави без выбора.
        window show

    if aonl_sl_story:
        th "А если он выберет меня? Тогда будет неудобно перед Славей. И всё же я бы пошла с ним."
        show sl serious pioneer with dspr
        sl "Я пойду с ним!"
        "Пока Сёма размышлял, Славя сама вызвалась."
        th "Эх, наша активистка. По крайней мере буду уверена, что с ним ничего не случится. Славя не допустит. Она сильная девушка."
        show mt smile pioneer panama with dspr
        mt "Вот и отлично! Вдвоём веселее."
        show pi normal aonl_pioneer with dspr
        me "Ты уверена?"
        show sl smile pioneer with dspr
        "Девушка лишь улыбнулась."
        "Сёма смотрел на неё восхищённым взглядом. Я отвернулась, прикусив губу."
        mt "Отлично! Тогда удачи вам."
        me "Она нам пригодится…"
        stop music fadeout 3
        window hide
        scene bg ext_houses_sunset with dissolve
        window show
        "Все стали расходиться по домикам, я старалась не оборачиваться."
        th "Если бы он только позвал… Тогда что?"
        "Мотнула головой, отгоняя лишние мысли."
        th "Всё уже случилось, нет смысла гадать, если бы да кабы."
        stop music fadeout 2
        window hide
        play ambience ambience_int_cabin_evening fadeout 1 fadein 2
        scene bg aonl_int_house_of_un_sunset
        show mi normal pioneer
        with fade2 
        window show
        mi "Лена! Ты слышала? Говорят, Шурик в старом лагере! {w} Я побегу его искать, а то вдруг ему нужна помощь, а он там совсем один!"
        "Говоря, Мику активно размахивала фонариком."
        th "Если она в таком состоянии пойдёт в старый лагерь, нам и её придётся искать."
        un "Мику, подожди."
        show mi upset pioneer with dspr
        mi "Что?"
        un "Вожатая уже отправила Славю и Семёна на поиски."
        show mi shocked pioneer with dspr
        mi "Давно? Может я ещё догоню!"
        un "Уже давно."
        "Я закрыла ей проход."
        un "Всё будет хорошо. Они найдут Сашу."
        show mi dontlike pioneer with dspr
        mi "Всё же побегу за ними, вдруг успею!"
        "Мику оббежала меня и рванула со вех ног."
        un "А ты знаешь дорогу?"
        show mi upset pioneer with dspr
        "Девушка резко остановилась и начала метаться из стороны в сторону, словно думая остаться или нет."
        th "В этом вся Мику. {w} Действует быстрее, чем думает."
        un "Если пойдёшь сейчас, то можешь сама потеряться."
        show mi sad pioneer with dspr
        "Мику остановилась пригорюнившись."
        un "Не переживай."
        "Я взяла её за руку."
        un "Пойдём."
    
    if aonl_un_story:
        "Я хотела вызваться, но смогла лишь посмотреть на Сёму."
        th "Прошу догадайся, выбери меня."
        "Сёма, поймав мой взгляд призадумался."
        me "Я же не пойду туда один?!"
        th "Так меня позови!"
        show mt normal pioneer at left with dspr
        "Ольга Дмитриевна призадумалась."
        mt "Пожалуй, ты прав… Тогда завтра с утра пойдём все вместе."
        window hide
        hide dv
        hide sl
        hide mt
        hide us
        with dissolve
        pause 2
        scene bg ext_houses_sunset with dissolve
        stop music fadeout 2
        window show
        "Все стали расходиться по домикам."
        th "Если бы он только позвал… Тогда что?"
        th "Тогда бы пошла не задумываясь, но Сема, кажется, не уверен в своих силах." 
        th "Хотя я чувствую, он справится." 
        th "Он гораздо сильнее, чем думает."
        window hide
        play ambience ambience_int_cabin_evening fadeout 1 fadein 2
        scene bg int_house_of_un_day # sunset
        show mi normal pioneer
        with fade2 
        window show
        mi "Лена! Ты слышала? Говорят, Шурик в старом лагере!" 
        mi "Я побегу его искать, а то вдруг ему нужна помощь, а он там совсем один!"
        "Говоря, Мику активно размахивала фонариком."
        th "Если она в таком состоянии пойдёт в старый лагерь, нам и её придётся искать."
        un "Мику, подожди."
        show mi upset pioneer with dspr
        mi "Что?"
        un "Вожатая завтра отправит людей на поиски. Ночью искать опасно."
        show mi normal pioneer with dspr
        mi "Это не проблема, у меня есть фонарик."
        "Я перекрыла проход и выхватила фонарик из рук."
        show mi upset pioneer with dspr
        un "Успокойся, завтра вместе пойдём за Сашей, а сегодня ты сама можешь потеряться." 
        un "Легче ему от этого не станет, даже наоборот."
        show mi sad pioneer with dspr
        "Мику заколебалась."
        un "Не переживай. Всё будет хорошо."
        "Я взяла её за руку."
        un "Пойдём."

    window hide
    scene bg aonl_int_house_of_un_sunset
    show mi sad pioneer close
    with fade
    play sound sfx_bed_squeak2
    window show
    play music music_list ["memories"] fadein 2 
    "Усадив девушку на кровать, расположилась рядом."
    un "Тебе страшно за Сашу?"
    mi "Очень Лен. Мне так страшно за него. Он такой хороший, такой добрый, такой умный, такой красивый…"
    show mi surprise pioneer close with dspr
    "Девушка осеклась."
    "Впрочем, я и так всё поняла."
    un "Давно?"
    "Повисло короткое молчание, что для нашего домика равносильно чуду."
    show mi shy pioneer close with dspr
    mi "Во второй день лагеря, когда мы выгребали запчасти из муз клуба и к кибернетикам переносили. Меня тогда чуть ящиками не завалило, а Саша кинулся меня спасать." 
    mi "Он все ящики принял на себя, закрыв собой. Я тогда сильно-сильно испугалась." 
    mi "А ему ящик на голову упал, но он сказал голова крепкая ничего страшного."
    "Девушка шмыгнула носом."
    "Я обняла её и положила голову подруги себе на плечо, поглаживая волосы, как маленькой."
    show mi cry pioneer close with dspr
    mi "Он такой смелый, такой отзывчивый, когда у меня сломался микрофон, он сам вызвался его починить. До сих пор деталь искал и обещал занести." 
    mi "Мне как-то неудобно, что я ничем ему в ответ не помогла."
    un "А он знает, что ты о нём думаешь?"
    mi "Нет, я… Не сказала, никак. Каждый раз, когда он рядом я словно дар речи теряю. С ним всё иначе не так как с другими. Я хочу сказать, но боюсь."
    un "Чего?"
    show mi sad pioneer close with dspr
    mi "А вдруг он лишь посмеётся надо мной? {w} А вдруг у него в городе есть другая? {w} А вдруг я ему не нравлюсь?"
    un "Значит, так и будешь молчать?"
    mi "Я… Я не знаю. {w} А ты как бы поступила на моём месте?"

    if aonl_sl_story:
    
        "Вопрос поставил в тупик. Окажись сама в такой ситуации, сказала бы? Конечно, сейчас стоит молчать. Он уже нашёл девушку, но если бы был свободен…?"
    
    if aonl_un_story:
    
        "Вопрос поставил в тупик. Окажись сама в такой ситуации, сказала бы?" 
        "Не знаю. Самой страшно, вдруг Сёма отвергнет, и я снова останусь одна."

    un "Сама не знаю, подруга. Но точно знаю одно."
    mi "Что?"
    un "У нас осталось всего 3 дня в лагере. {w} Если и говорить, то, как можно скорее."
    "Мику надолго замолчала."
    show mi happy pioneer close with dspr
    mi "Да."
    mi "Лен, ааааааа…"
    "Девушка протяжно зевнула."
    un "Что?"
    mi "А у тебя… У тебя есть, за кем бы так пошла?"
    "Я молчала пару минут думая над ответом."
    un "Есть."
    "Сказала шёпотом, но Мику никак не отреагировала."
    th "Не услышала?"
    mi "Мику?"
    stop music fadeout 2
    "Молчание."
    "Я заглянула девушке в лицо. Спит. Неудивительно, сильно перенервничала за сутки."
    hide mi with dissolve
    "Аккуратно переложила голову на подушку, а ноги на кровать, предварительно сняв обувь, и укрыла своим одеялом."
    "Какое-то время сидела напротив, сочувственно рассматривая подругу."
    th "Бедняжка, я знаю, как это тяжело. Держись, родная."
    
    if aonl_sl_story:
        window hide 
        $ night_time()
        $ persistent.sprite_time = "night"
        window show
        "Легла на кровать и попыталась заснуть."
        scene bg int_house_of_un_night with fade2 
        play ambience ambience_int_cabin_night fadeout 1 fadein 2
        "Бесполезно."
        "Вышла из домика."
        window hide
        scene bg aonl_ext_houses_night with fade2
        window show
        th "Погуляю, сна всё равно ни в одном глазу."
        window hide
        scene bg ext_playground_night with dissolve
        window show
        "Сама не знаю, почему пришла сюда."
        window hide
        scene stars with dissolve
        play music aonl_stars fadein 3
        window show
        "Расположившись поудобнее подняла взгляд к звёздам." 
        th "Миллионы миров, мои старые друзья одинокими вечерами." 
        th "Возможно, там тоже есть жизнь, и кто-то такой же одинокий смотрит на меня через тысячи световых лет." 
        th "Возможно, где-нибудь там найдётся место и мне?"
        th "А с другой стороны, может я, уже нашла своё место?" 
        th "У меня есть настоящие друзья, а большего и не надо."
        th "Ещё немного погуляю и баиньки."
        stop music fadeout 3
        window hide
        play ambience ambience_lake_shore_night fadeout 1 fadein 2
        scene bg ext_beach_night with dissolve2
        window show
        th "Красивая Луна и никого на горизонте."
        sl "А что ты здесь делаешь?"
        show sl surprise swim with dissolve
        play sound sfx_bodyfall_1
        with vpunch
        un "Ой!"
        "Девушка подошла так неожиданно, что я подскочила от страха."
        sl "Извини, не хотела пугать."
        un "Да ничего… Почему ты не с Семёном?"
        show sl normal swim with dspr
        sl "Так мы уже вернулись. {w} Нашёлся Шурик."
        un "А… С ним всё хорошо?"
        show sl smile swim with dspr
        sl "Всё нормально не переживай. Уже спит."
        un "Ух, гора с плеч. А что ты здесь делаешь?"
        show sl smile2 swim with dspr
        sl "Купаться пришла. {w} Разве не видно, хи-хи?"
        un "Э… Ну да, вижу."
        sl "Присоединишься?"
        un "Нет. Я пойду."
        show sl smile swim with dspr
        sl "Хорошо. Спокойной ночи."
        un "Спокойной ночи."
        window hide
        play ambience ambience_int_cabin_night fadeout 1 fadein 2
        scene bg int_house_of_un_night with fade2
        play music music_list ["a_promise_from_distant_days"] fadein 2
        play sound sfx_bed_squeak1
        window show
        "Я легла на кровать и спокойно закрыла глаза."
        th "Завтра обрадую Мику. Встречусь с Сёмой..."
        th "У нас есть ещё три дня, после которых мы навсегда расстанемся, а значит надо провести их с пользой."
        show mi sad pioneer with dissolve
        mi "Лен."
        un "А?"
        "Мику заспано приоткрыла глаза."
        mi "Думаешь, они смогут его найти?"
        un "Уже нашли, Шурки спит в домике."
        show mi surprise pioneer with dspr
        mi "Правда?!"
        play sound sfx_bed_squeak2
        "Мику резко вскочила!"
        mi "Я к нему!"
        un "Стой!"
        mi "А?"
        un "Он устал, подруга. {w} Дай ему отдохнуть."
        mi "Но я…"
        un "Завтра, всё завтра."
        mi "Эх."
        play sound sfx_bed_squeak1
        hide mi
        "Мику легла обратно."
        mi "Спокойной ночи."
        un "Спокойной ночи."
        window hide
        stop music fadeout 3
        stop ambience fadeout 2
        scene bg black with fade2
        pause 3
        jump aonl_day5_alt

    if aonl_un_story:
        window hide
        play ambience ambience_camp_center_evening fadeout 1 fadein 2
        scene bg aonl_ext_house_of_un_sunset with fade2
        window show
        "Тихонько выйдя из домика, я направилась на площадь." 
        "Сергей объяснил, как дойти оттуда до старого лагеря."
        "Конечно, я не великий детектив, но бросить товарища и уж тем более подругу в такой сложной ситуации не хочу." 
        "Мику помогала все эти дни, порой жертвуя своими интересами." 
        "А значит, настал мой черёд ей помочь." 
        "Если потребуется, сама отыщу Сашу..." 
        "Чего бы это ни стоило."
        window hide
        scene bg ext_square_sunset with dissolve
        show pi normal aonl_pioneer with dissolve
        window show
        "Выйдя на площадь, я увидела Семёна, сидящего на лавочке."
        th "Что он здесь делает? Хотя…"
        th "А вдруг это судьба!"
        un "Привет…"
        "Сёма удивлённо повернулся. Видимо не сразу меня заметил."
        me "Привет… Не спится?"
        "Глупый вопрос."
        me "Ну да, ещё рано, конечно."
        un "Можно я присяду?"
        me "Да, конечно, садись."
        "Он подвинулся, буквально вжавшись в край лавки."
        un "Спасибо."
        "Я присела и посмотрела на небо, толком не зная с чего начать."
        play music music_list ["into_the_unknown"] fadeout 5
        un "Грустно…"
        me "Что грустно?"
        un "Что Шурик пропал."
        show pi upset aonl_pioneer with dspr
        me "Да, неприятно получилось."
        "Мы снова замолчали, Сёма о чём-то усиленно размышлял, это читалось на лице, а вот я вообще не знала, как продолжить разговор."
        me "Уверен, что он найдётся! Ну, в самом деле, куда ты денешься с подводной лодки?"
        un "Я надеюсь."
        me "Завтра Ольга Дмитриевна в милицию позвонит. Найдут они его, обязательно найдут!"
        un "А если за ночь…"
        me "Да что с ним может случиться!"
        th "Неужели он действительно думает, что всё так просто и совсем не беспокоится за Сашу."
        un "Наверное, ему там одиноко."
        show pi angry aonl_pioneer with dissolve 
        me "Как будто его кто-то заставлял туда идти!"
        un "А если он просто потерялся?"
        me "Ну так не надо по лесам шастать одному."
        th "Сёма такой безразличный, может я в нём ошибалась."
        un "Тебе его совсем не жалко. Вдруг Шурик сидит там, совсем один…"
        show pi upset aonl_pioneer with dspr
        me "Жалко, конечно…"
        "Он смутился."
        un "И за ночь что угодно может случиться…"
        me "Не пойдём же мы сейчас его искать?"
        "Я отвернулась, провожая взглядом закатное солнце."
        me "Ты, правда, думаешь, что на ночь, глядя бродить по лесу – это хорошая идея?"
        un "Нет, наверное."
        th "Но разве есть другой выбор? Сёма соберись, ты же можешь."
        "Я продолжала молчать, не зная, как ещё его подтолкнуть."
        show pi normal aonl_pioneer with dspr
        me "Да и тем более днём искали уже."
        un "Везде?"
        "Я посмотрела ему прямо в глаза."
        me "Не знаю. Вроде бы везде."
        th "Ты же знаешь, что нет."
        un "А как же старый лагерь?"
        "Впервые мои слова прозвучали не отвлечённо-безразлично, а, кажется, даже уверенно."
        me "А где он? Я вот не знаю."
        un "Электроник рассказывал."
        me "Ну, ему верить…"
        "Он глупо усмехнулся, пытаясь свести всё к шутке, но я продолжала всё так же серьёзно смотреть на парня."
        th "Сейчас не до игр Сёма. Видимо, это бесполезно, придётся идти одной."
        me "Конечно, если он не так далеко…"
        un "Значит, ты хочешь пойти?"
        th "Неужели..."
        me "Можно, если только быстро и сразу назад…"
        th "Ну наконец-то! {w} Ох Сёма, хороший ты мальчик, вот только, немного тормозишь порой. Ничего, это поправимо."
        un "Хорошо."
        "Я улыбнулась и протянула ему фонарик, отобранный у Мику."
        me "Да, полезная штука…"
        "Осёкшись, Сёма настороженно на меня посмотрел, словно, что-то заподозрил, но ничего не сказал. Лишь обречённо вздохнул и направился в лес со мной."
        th "Да ты мой умничка."
        "Он обречённо вздохнул и направился вместе со мной в сторону леса."
        stop music fadeout 2
        window hide
        play ambience ambience_forest_night fadeout 1 fadein 2
        scene bg ext_path2_night with dissolve
        $ night_time()
        $ persistent.sprite_time = "night"
        show pi normal aonl_pioneer with dissolve
        play music music_list["door_to_nightmare"] fadein 3
        window show
        "Ночь вступила в свои права."
        "Из-за этого шли медленно, стараясь держаться рядом друг с другом."
        "В каждом кусте мерещилось чудовище, отовсюду раздавался шелест листвы и скрип веток, но я не показывала страха. Сёма наверняка тоже боится хоть и старается держаться молодцом, не стоит его отвлекать своим нытьём, он мужчина пусть ведёт."
        "Мы двигались, вроде бы в верном направлении, но минут через 10 возникло чувство, будто заблудились."
        "Незаметно покосилась на Сёму. Его челюсть плотно сжата, а взгляд сосредоточен."
        "Он повернулся ко мне, а я тут же изобразила на лице хладнокровие."
        "Не стоит отвлекаться на пустые страхи, нужно идти."
        "Вскоре я увидела просвет между деревьев."
        un "Смотри."
        "Сёма повёл в том направлении."
        window hide
        play ambience ambience_old_camp_outside fadeout 1 fadein 2
        play music music_list["sunny_day"] fadeout 1 fadein 5
        scene bg ext_old_building_night with dissolve
        window show
        "Через минуту мы вышли к старому обветшалому зданию."
        "Краска со стен давно осыпалась, в крыше и стенах зияли провалы, стёкла в большинстве окон выбиты и смотрят на нас своими тёмными глазами, словно дом живой и вот-вот сожрёт неосторожных путников."
        "Сёму передёрнуло."
        show pi upset aonl_pioneer with dissolve
        me "Да уж, жутковато…"
        "Я тоже вся сжалась от страха."
        un "Думаешь, он там?"
        me "Не знаю…"
        "Юноша заколебался."
        un "Пойдём?"
        window hide
        scene bg ext_old_building_night_moonlight with dissolve2
        window show
        "Сёма не успел ответить. Луна вышла из-за туч, осветив здание могильно-белым светом, словно склеп на кладбище. {w} Да и температура, кажется, упала."
        "Я не знала точно, так как мурашки могли быть от страха, а не холода."
        show pi upset aonl_pioneer with dissolve
        "Посмотрев на Сему, поняла, что он сам не в лучшем состоянии."
        un "Боишься?"
        "Я постаралась придать голосу спокойный тон."
        me "Тебе честно или соврать?"
        th "Дурашка."
        "Я слегка улыбнулась и взяла его за руку."
        "Сёма слегка сжал мою ладонь и повёл к зданию."
        window hide
        with fade
        play sound sfx_carousel_squeak
        pause(1)
        window show
        "Проходя детскую площадку, я услышала рядом резкий скрип от чего в панике вцепилась в руку Сёмы."
        show pi upset aonl_pioneer with dissolve
        me "Прости… Наверное, просто детство вспомнил."
        "Я пригляделась. Он толкнул карусель рукой, фух. "
        un "Любил карусели?"
        me "Да… То есть не знаю, не помню. Наверное. Все дети любят."
        un "А я не любила."
        me "Почему?"
        un "От них голова кружится."
        me "Если быстро крутиться – конечно."
        un "Мне больше качели нравятся."
        me "Так и на качелях можно раскачаться не хуже, чем на центрифуге!"
        un "Но зачем?"
        me "Не знаю…"
        "За разговором о детстве мы совершенно не заметили, как подошли к входу."
        window hide
        stop ambience fadeout 2
        scene bg int_old_building_night with dissolve
        window show
        "Внутри старый лагерь выглядел как обычный детский сад."
        show pi normal aonl_pioneer at center with dissolve
        me "Шурик!"
        un "Шурик!"
        "В ответ тишина."
        me "Похоже, нет тут никого."
        un "Надо всё равно проверить."
        "Сёма как-то странно на меня посмотрел, но протестовать не стал."
        me "Конечно, давай…"
        window hide
        hide pi with fade
        window show
        "Проверили все комнаты, Сёма даже на чердак слазил."
        "Нашли бумажки, бутылки, след костра, старые газеты, – но не Шурика."
        "Мы снова спустились в холл, откуда начинали поиски."
        show pi normal aonl_pioneer with dissolve
        me "Что будем дальше делать?"
        un "Не знаю…"
        "Я села на ступеньки и уставилась себе под ноги. Почему-то знаю, что проверили не всё, не могу объяснить."
        me "Думаю, стоит вернуться…"
        me "Всё-таки уже поздно и… Не будем же мы по всем лесам его искать!"
        un "Наверное, ты прав."
        "Ну, правда!"
        me "Ну правда!"
        "Он обречённо всплеснул руками и сел рядом."
        me "В конце концов, стоит подумать и о худшем сценарии…"
        un "Ты хочешь сказать…"
        me "Нет, но… Здесь водятся дикие звери?"
        un "Вряд ли."
        th "Значит, Шурик жив, и мы его найдём."
        me "Ну, может, он спит где! Утром проснется и вернётся в лагерь."
        un "Да, конечно…"
        "Я осталась на месте."
        "Сёма резко встал и принялся ходить из стороны в сторону."
        "Видно он очень нервничает."
        "Вдруг Сёма так же резко остановился и куда-то указал рукой."
        me "Смотри."
        "В полу оказался люк, причём его недавно открывали."
        un "Думаешь, Шурик там?"
        "Я присела на корточки и аккуратно протёрла ручку."
        me "Может, и не Шурик, но кто-то точно туда лазал за последнее время."
        th "Хорошо, что мы остались."
        un "Посмотрим?"
        play sound sfx_open_metal_hatch
        "Сёма без проблем открыл люк и осветил фонариком лестницу."
        me "Похоже, подвал…"
        un "Спустимся?"
        "Он посмотрел на меня как на умалишённую, но ничего не сказав, спустился вниз."
        hide pi with dissolve
        me "Нормально всё!"
        window hide
        play ambience ambience_catacombs fadeout 1 fadein 2
        scene bg int_catacombs_entrance with dissolve
        show pi normal aonl_pioneer with dissolve
        window show
        "Я спустилась следом."
        "Внизу оказался не подвал, а длинный тоннель, словно из фильмов про шпионов."
        "На стенах приколоты провода, металлическими крюками, под ногами валяются куски бетона и прочая грязь."
        th "Фу! Надеюсь не сильно испачкаюсь."
        un "Пойдём?"
        me "Куда? Туда?"
        un "Ну да. Вдруг Шурик там?"
        me "И что ему там делать?"
        th "Он серьёзно? Неужели каждый раз придётся подталкивать?"
        "Сёма потоптался на месте, но пошёл. "
        th "Видимо придётся."
        window hide
        scene cg d4_catac_un
        with dissolve
        window show
        "Сёма шёл впереди, я, чуть отстав, держалась за его руку."
        "Долгое время слышался лишь звук наших шагов, да луч фонарика бегал по одинаковым стенам."
        "В остальном царила полная тишина."
        me "Скажи что-нибудь."
        un "Дверь."
        me "Что?"
        un "Дверь."
        "Я показала вперёд."
        window hide
        scene bg int_catacombs_door
        show pi normal aonl_pioneer
        with dissolve
        window show
        "Дорогу преграждала металлическая дверь."
        #Можно взять дверь из летомана
        me "Значит, бомбоубежище…"
        un "Да, я что-то слышала."
        me "Зачем оно тут?"
        un "Не знаю. Может быть, Карибский кризис?"
        me "Карибский?"
        "Сёма почесал лоб, прикидывая, что-то в голове. Затем махнул рукой и, с трудом провернув штурвал, открыл дверь."
        play sound sfx_open_door_mines_metal
        stop ambience fadeout 3
        window hide
        scene bg int_catacombs_living with dissolve
        $ persistent.sprite_time = "night"
        window show
        "Внутри обнаружили приборы и две кровати со шкафчиками."
        "Я порылась в одном из них."
        un "Смотри."
        "Протянула Сёме пистолет."
        show pi surprise aonl_pioneer with dspr
        me "Зачем мне это?"
        un "От чудовищ защищаться."
        show pi normal aonl_pioneer with dspr
        me "Но тут нет никаких чудовищ."
        un "Как скажешь…"
        th "Глупенький, нам же может это пригодиться. Да и мужчина с оружием выглядит внушительнее."
        me "Гарантирую!"
        "Хоть и упирался, но все, же засунул пистолет за пояс."
        "Окинула взглядом оценивая новый образ."
        th "Красавчик! Даже плечи, кажется, стали шире, а в глазах впервые вместо страха появился азарт. Блин как классно!"
        "Я даже немного засмотрелась."
        "Изучив помещение, нашли другую металлическую дверь, но она оказалась закрыта, штурвал не поддавался."
        un "Может быть, этим?"
        "Я подала ломик."
        me "Да нет, давай сначала так попробую."
        play sound sfx_metal_door_handle_rattle
        "Кроме скрипа ручки ничего не вышло."
        me "Ладно, давай."
        play sound sfx_insert_crowbar_door
        hide pi with dissolve
        "Поддев ломиком, Сёма выломал дверь."
        window hide
        play sound sfx_fall_metal_door
        pause(1)
        $ persistent.sprite_time = "sunset"
        scene bg int_catacombs_living_nodoor
        with vpunch
        window show
        "Видимо, петли проржавели."
        "За дверью оказался такой же коридор."
        un "Пойдём?"
        show pi normal aonl_pioneer with dissolve
        me "Куда ты так спешишь?"
        un "Я? Я не спешу…"
        "От вопроса я снова смутилась."
        me "Тебе как будто совсем не страшно."
        un "Не знаю, а чего бояться?"
        un "Ты же меня защитишь…"
        "Добавила еле слышно."
        show pi surprise aonl_pioneer with dspr
        "Сёма удивлённо на меня посмотрел. Кажется, услышал."
        show pi normal aonl_pioneer with dspr
        me "Пойдём!"
        window hide
        scene cg d4_catac_un with dissolve
        play ambience ambience_catacombs fadeout 1 fadein 2
        window show
        "На этот раз Сёма двигался намного быстрее, я бы даже сказала с воодушевлением."
        scene black
        show cg d4_catac_un:
            linear 0.1 pos (0,5)
            linear 0.1 pos (0,0)
            linear 0.1 pos (5,0)
            linear 0.1 pos (0,0)
            repeat
        "Свет фонаря прыгал по стенам из стороны в сторону, пока из темноты не выхватил большую дыру…"
        window hide
        $ persistent.sprite_time = "night"
        scene bg int_catacombs_hole
        with dissolve
        window show
        "Внизу отчётливо виднелись рельсы."
        un "Что там?"
        me "Шахта, похоже."
        un "Посмотрим?"
        me "А почему не дальше?"
        un "Не знаю, мне кажется, нам туда."
        "Сама не знаю, откуда это чувство, но место казалось до боли знакомым."
        stop ambience fadeout 3
        me "Ну ладно, давай проверим."
        window hide
        $ persistent.sprite_time = "night"
        scene bg int_mine
        with dissolve
        play ambience ambience_catacombs_stones fadeout 1 fadein 2
        play sound sfx_jump_into_hole_2
        pause(1)
        window show
        "Спрыгнув, Сёма помог мне спуститься."
        th "Он такой заботливый."
        show pi normal aonl_pioneer at center with dissolve
        me "А какие полезные ископаемые бывают в этих краях?"
        un "Не знаю."
        me "Ну да, глупый вопрос. Сейчас-то уже, похоже, никаких…"
        hide pi with dissolve
        "Мы медленно двинулись во тьму, постоянно спотыкаясь о шпалы."
        window hide
        scene bg int_mine_crossroad with dissolve
        window show
        "Вскоре появилась развилка."
        show pi normal aonl_pioneer at center with dissolve
        me "Ну вот, этого ещё не хватало."
        un "Куда пойдём?"
        me "Куда? Не факт, что мы вообще выберемся отсюда, а уж если будем играть в пакмана…"
        un "Во что?"
        me "Неважно. Заблудимся, в общем."
        un "А вдруг там тоже есть выход?"
        me "Даже если есть… А если нет?"
        un "Значит, назад?"
        "Сёма со всей силы закричал:"
        scene black
        show bg int_mine_crossroad:
            linear 0.1 pos (0,5)
            linear 0.1 pos (0,0)
            linear 0.1 pos (5,0)
            linear 0.1 pos (0,0)
            linear 0.1 pos (0,5)
            linear 0.1 pos (0,0)
            linear 0.1 pos (5,0)
            linear 0.1 pos (0,0)
            linear 0.1 pos (0,5)
            linear 0.1 pos (0,0)
            linear 0.1 pos (5,0)
            linear 0.1 pos (0,0)
        show pi normal aonl_pioneer at center
        me "Шурик!"
        "Ответило нам лишь эхо, а с потолка посыпалась пыль."
        me "Видишь…"
        "Он не хочет идти."
        show pi surprise aonl_pioneer with dspr 
        un "Ладно, тогда я одна пойду."
        me "Что?"
        "Сёма скептически улыбнулся."
        me "Как это одна? Куда?"
        un "Но Шурика надо найти, вдруг он там…"
        "Я смутилась и опустила взгляд в пол, но продолжала стоять на своём."
        show pi normal aonl_pioneer with dspr
        me "Не-не-не, так не пойдёт, если идти, то вместе."
        un "Хорошо. Значит, пойдём."
        "Я улыбнулась и снова взяла его за руку."
        th "Какой же ты у меня умница, так и надо."
        "Сема в очередной раз посмотрел на меня подозрительно, но опять ничего не сказал."
        me "Только сначала…"
        
        # Взять фон с крестиком из «продолжение истории»
        
        "Он нацарапал камнем крестик на одной из деревяшек."
        me "Теперь хотя бы будем знать, откуда начинали."
        window hide
        $ mine_route = "un"
        jump aonl_mine

label aonl_mine:

    $ point = "1"
    $ previous_point = "1"
    $ halt_visited = False
    $ coalface_visited = False
    $ back_to_start = False
    $ first_turn = True
    jump aonl_mine_crossroad

label aonl_mine_crossroad:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad
    with fade

    if not first_turn:
        "Похоже, ещё одна развилка."

    menu:
        "Налево":
            $ first_turn = False
            $ aonl_mine_eval("left")
        "Направо":
            $ first_turn = False
            $ aonl_mine_eval("right")

label aonl_mine_coalface:

    scene bg int_mine_coalface with fade

    if coalface_visited:
        window show
        "Здесь мы уже были."
        window hide
        jump aonl_mine_crossroad

    window show
    "Вскоре показалось помещение с рублеными стенами и высоким потолком."
    "Внутри властвовал мрак, но в свете фонаря Сёма заметил пионерский галстук."
    show pi normal aonl_pioneer with dspr 
    me "Шурик! Шурик!"
    un "Шурик! Шурик!"
    "Снова ответило лишь эхо."
    un "Раз мы нашли галстук, значит, он где-то рядом."
    "Сёма ничего не ответил, и мы пошли дальше."
    window hide
    $ coalface_visited = True
    jump aonl_mine_crossroad

label aonl_mine_halt:

    $ persistent.sprite_time = "night"
    scene bg int_mine_halt
    with fade

    if halt_visited:
        window show
        "Здесь мы уже были."
        window hide
        jump aonl_mine_crossroad

    window show
    "Мы вышли к некоему подобию шахтёрского привала."
    "Везде валялись кирки, каски, в углу – ржавая вагонетка."
    "Все предметы были настолько старыми, что относились скорее к началу века, чем к середине."
    th "Получается, это действительно шахта…{w} А значит, тут бродить можно бесконечно."
    "Но я чувствовала, что выход где-то рядом, поэтому мы отправились дальше."
    window hide

    $ halt_visited = True

    jump aonl_mine_crossroad

label aonl_mine_return_to_start:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad
    with fade

    window show
    "Мы вернулись к тому месту, с которого и начинали."
    th "Значит, где-то не там повернули."
    th "Надо искать дальше."
    window hide

    menu:
        "Налево":
            $ aonl_mine_eval("left")
        "Направо":
            $ aonl_mine_eval("right")

label aonl_mine_exit:
    scene bg int_mine_door with fade
    window show
    "За очередным поворотом в свете фонаря появилась деревянная дверь."
    show pi normal aonl_pioneer at center with dissolve
    me "Хоть что-то…"
    un "Что?"
    me "Хотя бы не очередная развилка."
    un "А что там?"
    me "Сейчас у нас уже точно выбора нет – проверим."
    hide pi with dissolve
    play sound sfx_open_door_mines
    stop ambience fadeout 3
    "Он с силой дёрнул ручку и открыл дверь."
    window hide
    scene bg int_mine_room with dissolve
    window show
    "За ней обнаружили комнату с бутылками, окурками и исписанными стенами."
    th "Фу! Неужели нельзя убрать за собой."
    "Я шла аккуратно, стараясь не наступить в мусор."
    show pi upset aonl_pioneer at center with dissolve
    me "Эх…"
    "Сёма обессилено сполз по стене на пол."
    me "Вот теперь мы точно всё обошли."
    un "Не всё."
    "Я показала на металлическую дверь в углу, как и две предыдущие."
    me "Там, наверное, выход, как ты и говорила."
    un "Пойдём?"
    show pi normal aonl_pioneer with dspr
    me "Давай отдохнём немного."
    un "Хорошо."
    "Я села рядом, прижавшись всем телом и взяла его за руку."
    un "Ничего страшного."
    me "В смысле?"
    un "Что мы не нашли Шурика."
    me "Нам бы теперь самим выбраться…"
    un "Выберемся."
    me "Да, наверное, я дорогу запомнил."
    un "Мне совсем не страшно."
    me "Это хорошо."
    un "Потому что я с тобой."
    "Сама не понимаю, почему призналась. В этот момент это показалось уместным. "
    hide pi with dissolve
    play sound_loop sfx_shurik_mines_far
    "Неожиданно за дверью в шахту послышались громкие шаги."
    "Семён тут же вскочил и принялся шарить глазами по комнате."
    "Шум – тяжёлые шаги – приближался."
    window hide
    stop sound_loop fadeout 2
    play sound sfx_shurik_opens_door
    pause(1)
    show sh rage pioneer far at center 
    show pi surprise aonl_pioneer close at right 
    with dissolve
    window show
    "Дверь распахнулась, и на пороге появился Шурик."
    "Мы все застыли от удивления."
    sh "Вот вы где! Думали, сможете спрятаться?"
    me "Что?"
    sh "Думали, я вас не найду? А я нашёл!"
    "Лицо Саши исказила гримаса ярости, глаза под очками дьявольски сверкали, а в руках он сжимал арматуру."
    show pi angry aonl_pioneer with dspr
    me "Ты что, совсем сдурел, что ли?! Это же мы!"
    sh "Я вижу, что вы!"
    show sh rage pioneer at center with dissolve
    "Он сделал несколько шагов в нашу сторону."
    "Я испуганно смотрела на невменяемого Сашу."
    stop music fadeout 3
    sh "Думали, можно из меня дурака делать? Водить туда-сюда?! «Направо, налево, направо, налево»?! А я ведь ходил, всё ходил…"
    window hide
    scene cg d4_sh_stay with dissolve
    play music music_list["pile"] fadein 1
    window show
    "Саша бросился на нас с арматурой, а Сёма оттолкнул меня в сторону выставив фонарь."
    window hide
    play sound sfx_break_flashlight
    with vpunch
    pause(1)
    window show
    "... рука с фонарём, взметнувшаяся вверх..."
    window hide
    scene black with dissolve
    window show
    "Мир погрузился во мрак, я услышала, как Саша сбегает в шахту."
    "Зашарила руками в темноте и неожиданно, поймала руку Сёмы, который, видимо, делал тоже самое."
    un "Не бойся."
    me "Ты где, чёртов псих?!"
    "В крике Семёна отчётливо слышалась ярость."
    un "Он ушёл."
    me "Как ушёл? Куда ушёл?"
    un "Успокойся."
    "Я нежно обняла его и прижалась всем телом."
    th "Какой же он смелый. С ним так спокойно."
    "Сёма продолжал взволновано дышать."
    "Грудь юноши продолжала яростно подниматься и опускаться."
    stop music fadeout 3
    me "И что теперь делать?"
    un "У тебя же есть пистолет."
    me "Да? И в кого мне стрелять?"
    un "В нём же ракета осветительная."
    play sound sfx_signal_pistol
    "После заминки Сёма достал пистолет и выстрелил в стену."
    window hide
    scene bg int_mine_room_red
    with flash_red
    show pi normal aonl_pioneer red at center with dissolve
    window show
    "Комната озарилась красным светом."
    "Ракета светилась в углу, как фейерверк."
    un "Пойдём скорее, она долго гореть не будет."
    me "Куда?"
    "Я показала на вторую дверь."
    "Сёма довольно легко её открыл, и мы побежали во тьму…"
    window hide
    scene bg int_catacombs_entrance_red 
    show pi normal aonl_pioneer
    with dissolve
    play ambience ambience_catacombs fadeout 1 fadein 2
    window show
    "Ракета угасала с каждой секундой."
    "Мы спотыкались и несколько раз чуть не упали, но продолжали бежать."
    window hide
    scene bg int_mine_exit_night_nolight with dissolve
    window show
    "К счастью вскоре показался свет." 
    "Мы вышли к лестнице, упирающейся под потолком в решётку, ракета как раз погасла."
    me "Слава богу…"
    play sound sfx_break_grid
    stop ambience fadeout 3
    "После нескольких ударов остатками фонаря Сёма выломал решётку и вылез наружу. {w} Следом вылезла я."
    window hide
    play ambience ambience_camp_center_night fadeout 1 fadein 2
    scene bg ext_square_night
    show pi normal aonl_pioneer
    with dissolve
    window show
    "Выбравшись на поверхность, Сёма измотанный упал на траву, рядом с памятником."
    me "Ужас какой-то…"
    "Дышал он по-прежнему тяжело."
    window hide
    scene cg aonl_cl_d4_un_knees with dissolve
    window show
    "Я села рядом, стараясь помочь."
    me "Жуть просто…"
    stop ambience fadeout 2
    play music music_list["what_do_you_think_of_me"] fadein 3
    "Я нежно погладила его по волосам и улыбнулась."
    un "Всё закончилось."
    me "Не знаю даже… По лесу бродит свихнувшийся пионер! Маньяк-убийца, можно сказать!"
    un "Думаю, с ним всё будет в порядке."
    me "В порядке? Нет, не уверен!"
    un "Главное, что с нами всё хорошо."
    "Я снова улыбнулась."
    me "Как ты можешь быть такой спокойной?"
    th "Какой же он всё таки дурашка."
    un "Я же говорила, что с тобой мне бояться нечего."
    me "Спасибо за комплимент."
    un "Пожалуйста."
    me "Но всё-таки не стоило никуда ходить."
    un "Да, наверное."
    "Его глаза закрылись, и он мирно засопел."
    th "Как же он устал, мой герой. За меня ещё ни разу мальчик не заступался. Это… так приятно."
    "Я переложила его голову себе на колени, чтобы Сёме было удобнее, и погладила волосы юноши."
    un "Ты молодец."
    "Прошептала ему на ухо."
    un "Отдыхай мой хороший."
    window hide
    scene bg ext_square_night
    show pi normal aonl_pioneer
    with dissolve
    window show
    "Прошло довольно много времени. {w} Вскоре Сёма открыл глаза и приподнял голову."
    me "Долго я спал?"
    un "Не знаю, у меня же нет часов."
    "Рассмеялась я."
    me "Ну примерно!"
    un "Нет. Может быть, минут двадцать."
    me "Ааа… Ну ладно тогда."
    "Он снова лёг на колени и блаженно закрыл глаза."
    th "Он такой милый, когда отдыхает. Ах да, его же нужно предупредить!"
    stop music fadeout 3
    play ambience ambience_camp_center_night fadeout 1 fadein 2
    un "Шурик вернулся."
    show pi surprise aonl_pioneer with dspr
    me "Что?!"
    "Он подскочил как ошпаренный."
    un "Вон он, на лавочке спит."
    "Я показала на скамейку."
    me "И ты что…"
    un "Ты так мирно спал, я не хотела тебя будить."
    un "Ничего страшного – похоже, он просто был немного не в себе…"
    "Я опять смутилась."
    th "Неужели поступила неправильно, ведь Сёма спал, ему требовался отдых или всё же стоило разбудить?"
    un "Да и шёл он так, шатаясь, в нашу сторону не смотрел. А если бы я начала шуметь…"
    "На мои глаза навернулись слёзы."
    th "Сёма, прости, я больше не буду."
    show pi normal aonl_pioneer with dspr
    me "Ладно, ничего страшного."
    "Сёма подошёл к Саше и ударил его по щеке."
    show sh scared pioneer at cright
    show pi angry aonl_pioneer
    with dissolve
    sh "Ай!"
    sh "Что такое?!"
    me "Ты что творишь, скотина?!"
    sh "Что?"
    "Саша испуганно уставился на Семёна."
    me "Что это было там внизу?!"
    sh "Что? Где?"
    me "В подземелье, в шахте, в бомбоубежище! Совсем крыша поехала?"
    sh "Я тебя не понимаю…"
    "Он осмотрелся."
    sh "И почему я здесь?"
    me "А где же тебе надо быть ещё, по-твоему?! Хотя нет, подожди, я знаю – в дурдоме тебе надо быть!"
    sh "Я утром пошёл в старый лагерь за деталями, а потом…"
    un "А потом ты ничего не помнишь?"
    sh "Да, и я…"
    show pi normal aonl_pioneer with dspr
    me "Не прикидывайся."
    "Семён вроде успокоился и сел рядом с ним."
    show sh upset pioneer at cright with dspr
    sh "Ничего не понимаю… Всё это антинаучно!"
    me "Как угодно. Только не думай, что я тебе поверю."
    sh "Ведь провалы в памяти просто так…"
    "Саша, что-то бубнил себе поднос, не обращая на нас внимания."
    un "Пойдём."
    "Тихонько прошептала я Сёме."
    me "И что, вот так просто его оставим тут?"
    un "Он не в себе – ему надо выспаться."
    me "Да этого психопата вообще опасно одного оставлять! {w}  Может, он Электроника ночью катушкой индуктивности удавит!"
    un "Всё будет нормально, поверь."
    me "Ладно…"
    hide sh
    hide pi
    with dissolve
    "Мы оставили Шурика, продолжающего что-то бубнить, наедине с собой."
    window hide
    scene bg ext_house_of_mt_night_without_light with dissolve2
    window show
    show pi normal aonl_pioneer at center with dissolve
    un "Пришли."
    me "Что? Куда?"
    un "Пришли, а мне дальше."
    "Я улыбнулась."
    "Он совсем не заметил, как мы оказались возле домика Ольги Дмитриевны."
    me "Да…"
    un "Спасибо тебе… За сегодня."
    me "Да не за что тут благодарить; хорошо хоть живы остались. {w} И посмотрим ещё, что завтра Шурик скажет!"
    un "Всё равно спасибо…"
    "Глупенький даже не понимает, какой он герой!"
    show pi smile aonl_pioneer with dspr
    me "Ну, тогда, пожалуйста."
    un "Ладно, мне пора!"
    hide pi with dissolve
    "Я резко развернулась и быстро зашагала в сторону своего домика. Хотелось большего, какого-то продолжения, ведь не может принц, спасший принцессу от дракона, тут же с ней расстаться." 
    "Но Сёма сейчас, кажется не в том состоянии, он где-то далеко в своих мыслях. {w} Да и я не готова…"
    "При мысли о том, чем это должно закончиться... {w} Покраснела как помидор и быстрее побежала к домику."
    window hide
    play ambience ambience_int_cabin_night fadeout 1 fadein 2
    scene bg int_house_of_un_night with fade2
    play sound sfx_bed_squeak1
    window show
    play music music_list ["a_promise_from_distant_days"] fadein 2
    "Я легла на кровать и спокойно закрыла глаза."
    show blink
    th "Завтра обрадую Мику. Встречусь с Сёмой..."
    th "У нас есть ещё три дня, я обязательно ему скажу."
    mi "Лен."
    un "А?"
    hide blink
    show unblink
    show mi upset pioneer with dissolve
    "Мику заспано приоткрыла глаза."
    mi "Думаешь, его смогут найти?"
    un "Мы с Сёмой уже нашли, Шурки спит в домике."
    show mi surprise pioneer with dspr
    mi "Правда?!"
    play sound sfx_bed_squeak2
    "Мику резко вскочила!"
    mi "Я к нему!"
    un "Стой!"
    show mi upset pioneer with dspr
    mi "А?"
    un "Он устал подруга, дай ему отдохнуть."
    show mi sad pioneer with dspr
    mi "Но я…"
    un "Завтра, всё завтра."
    mi "Эх."
    play sound sfx_bed_squeak1
    "Мику легла обратно."
    mi "Спокойной ночи."
    un "Спокойной ночи."
    show blink
    "Глаза закрылись, и я увидела Сёму, закрывающего меня от Шурика."
    
    # Есть арт где семён на площади закрывает собой Лену.
    
    th "Я люблю тебя. Мой герой."
    window hide
    stop music fadeout 3
    stop ambience fadeout 2
    pause 2
    jump aonl_day5_alt
