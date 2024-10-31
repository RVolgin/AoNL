label aonl_miku:
    call aonl_new_chapter(666, "???", "В себе храним терзаний бездну\nКалечат душу изнутри\nМы внешне остаёмся те же\nИ лишь во сне приходят демоны души")

    #Начало Мику рута!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #Фон полёт через облака и звёзды и фон домик лены внутри в конце
    
    $ night_time()
    $ persistent.sprite_time = "night"
    
    play music aonl_over_the_sky fadein 2
    show bg aonl_sky with fade2    
    "Меня словно подняло воздух над кроватью..." 
    "И резко швырнуло через облака..." 
    scene stars with fade2
    "Я пролетала через звёзды и планеты..." 
    "А потом, словно камень, полетела вниз..."
    window hide
    stop music fadeout 3
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day fadein 2
    scene bg int_house_of_un_day with fade2
    window show
    play sound [sfx_blanket_off_stand, sfx_bed_squeak1]
    "Выскочила из-под одеяла."
    "Часы показывали 5 утра."
    th "Неужели уже утро?" 
    th "Как же меня сильно отключило!"
    play music aonl_strange fadein 3    
    th "А куда делась Мику?"
    "Соседка в поле зрения отсутствовала."
    th "Спать уже не хочется пойду умоюсь, возможно и Мику там найду."
    window hide
    play ambience ambience_camp_center_day fadeout 1 fadein 2
    scene bg ext_washstand2_day with fade2
    play sound sfx_open_water_sink
    pause 1
    window show
    "Кран ответил гудением, а не водой."
    th "Сломался?"
    play sound sfx_open_water_sink
    "Включила другие. То же самое."
    play sound sfx_close_water_sink
    th "Блин! Что теперь делать?"
    window hide
    play ambience ambience_forest_day fadeout 1 fadein 2
    scene bg ext_path2_day with dissolve
    window show
    "Я осмотрелась в поисках источника воды и мой взгляд зацепился за лес."
    th "Вроде недалеко есть лесное озеро. Нужно проверить."
    "Двинувшись по тропинке довольно быстро почувствовала влагу в воздухе."
    window hide
    scene bg aonl_ext_forest_lake_day with dissolve
    window show
    "Ориентируясь по принципу горячо-холодно вышла к лесному озеру." 
    "Вода оказалась намного приятнее, чем с крана." 
    "Нужно как-нибудь искупаться при случае."
    "Закончив водные процедуры, направилась назад."
    "Но стоило на секунду моргнуть…"
    window hide
    stop ambience fadeout 1
    play sound ["<silence 0.5>", sfx_scary_sting]
    scene cg d1_rena_sunset with flash
    with hpunch
    with hpunch
    window show
    "Я вздрогнула…"
    window hide
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_house_of_un_day with flash
    window show
    "Открыла глаза и оказалась возле своего домика!"
    th "Что за..."
    "Судя по солнцу, прошло несколько часов, но как?!"
    th "Почему ничего не помню? Что происходило всё это время? И что за девушка пригрезилась?"
    "Осмотрев свою одежду, не заметила ничего не обычного."
    th "Может, я просто не выспалась и на пару часов провалилась в забытье?"
    th "Ага! Отличное объяснение. Пока ничего не ясно. Схожу на линейку, может тогда станет яснее."
    window hide
    play ambience ambience_int_cabin_day fadeout 1 fadein 2
    play sound [sfx_open_dooor_campus_1, sfx_close_door_campus_1]
    pause 1
    scene bg int_house_of_un_day with dissolve
    show mi upset pioneer with dissolve
    window show
    "Зайдя в домик положить умывальные принадлежности, я встретила Мику."
    mi "Что ты здесь делаешь?"
    "Я удивлённо уставилась на соседку."
    un "Мику, я тут живу. Ты что, забыла?"
    show mi shocked pioneer with dspr
    mi "Мику?"
    "Глаза девушки расширились от ужаса."
    th "Да что с ней?"
    un "Я не знаю, что с тобой, но нужно идти на линейку затем убрать территорию, помочь в библиотеке, да и тебе нужно привести в порядок музыкальный клуб. Скоро конец смены ты забыла? Требуется сдать помещения."
    "Девушка побелела как смерть и продолжила смотреть на меня затравленным взглядом."
    th "Что с ней? Наверно тоже плохо спала. Оставлю её пока одну."
    window hide
    stop music fadeout 3
    play sound [sfx_open_dooor_campus_1, sfx_close_door_campus_1]
    pause 1
    play ambience ambience_camp_center_day fadeout 1 fadein 2
    scene bg ext_house_of_un_day with dissolve
    window show
    "Оставив подругу одну, я направилась на линейку."
    window hide
    scene bg ext_square_day with dissolve
    show mt normal pioneer panama at center with dissolve
    window show
    #музыка временная, я без понятия, что тут ставить
    play music music_list ["into_the_unknown"] fadein 3
    "Там собралась уже изрядная часть лагеря, Ольга Дмитриевна пыталась всех построить в ряд по отрядам."
    mt "Лена, становись в строй."
    un "А… Да."
    show mt angry pioneer panama with dspr
    mt "И где твоя соседка Мику?"
    un "Она в домике, наверно, скоро придёт."
    show mt sad pioneer panama with dspr
    mt "Ладно, потом с ней разберёмся. Вы меня, дети, до инфаркта доведёте. Сначала Семён пропал на всю ночь…"
    un "Семён пропал?"
    "Я не на шутку испугалась, он конечно плохо со мной поступил вчера, но исчезновение человека — это серьёзно."
    mt "Утром нашёлся, сказал, что всю ночь с какой-то Машей провёл. Позже своё получит."
    th "С какой ещё Машей, ему что Алисы мало?"
    show pi normal aonl_pioneer at cright behind mt
    show mi upset pioneer at fright behind pi
    with dissolve
    "Пока пыталась понять, кого ещё этот кобель добавил в свой список, явился сам виновник торжества вместе с Мику." 
    "Выглядели они как-то напугано."
    "Сёма направился прямо к вожатой, Мику затравлено пряталась за ним."
    me "Ольга Дмитриевна, знаете ли…"
    show mt smile pioneer panama at center with dspr
    mt "А, вот и Мику нашлась!"
    mt "Отлично! Поговорим после линейки."
    me "Какой линейки ещё…{w} Может, хватит дурью маяться. Не смешно уже, ей-богу!"
    show mt surprise pioneer panama at center with dspr
    "Вожатая опешила с такого поворота, впрочем, как и все мы."
    show mt surprise pioneer panama with dspr
    mt "Ты о чём?"
    me "О том!"
    show pi normal aonl_pioneer behind mi at cright
    show mi normal pioneer at fright
    with dspr
    # show mi normal pioneer at left with dissolve # копипаста из оригинала?
    "Из-за спины робко выглянула Мику."
    mi "Ольга Дмитриевна, ведь правда уже не смешно…"
    mt "Я вас не понимаю…"
    th "Да и я тоже, о чём они говорят?"
    show pi angry aonl_pioneer with dspr
    me "Давайте уже вернёмся к съёмкам, в конце концов!"
    mt "Каким съёмкам?"
    me "Ладно, предположим…{w} Расскажите нам свою версию."
    mt "Версию чего?"
    "Вожатая удивлённо хлопала глазами, как и я."
    me "Всё ясно."
    "Он схватил Мику за руку и направился прочь с площади."
    show mi shocked pioneer with dspr
    mi "Эй, подожди! Ты куда?"
    me "Надо найти кого-нибудь более адекватного."
    show mt angry pioneer panama with dspr
    mt "Стойте, вы куда собрались? Немедленно вернитесь, я родителям сообщу!"
    hide mi
    hide pi
    with dissolve
    "Пара бывших образцовых пионеров полностью проигнорировали вожатую."
    "Вся линейка буквально уронила челюсти."
    "Ольга бросила бесполезные попытки вернуть распоясавшихся пионеров и переключила внимание на нас."
    show mt normal pioneer panama with dspr
    mt "Так строимся, ты левее стань… Младший отряд вперёд… Сейчас придёт Славя и начнём."
    "Мы выстроились в ряд по отрядам, но помощница вожатой так и не появилась."
    "Дмитриевна совсем растерялась. Она то и дело поглядывала нам за спины, но мало, что изменилось."
    "В конце концов, не дождавшись Слави, рассказала план мероприятий на день и напомнила о скором конце смены, после чего отпустила всех кроме Жени."
    "Видимо, хочет спросить её о Славе."
    "Я лишь пожала плечами."
    th "У меня и своих проблем полно." 
    th "Может к обеду найдётся, если не пропала как Шурик ранее." 
    th "Надеюсь, её не придётся по катакомбам искать."
    th "С Сёмой я туда больше не пойду, его слову грош цена!"
    window hide
    play ambience ambience_dining_hall_full fadeout 1 fadein 2
    scene bg int_dining_hall_people_day with dissolve2
    show mi upset pioneer at right
    show pi normal aonl_pioneer at left
    with dissolve
    window show
    "Придя на завтрак, я увидела Мику с Сёмой, сидящих отдельно ото всех."
    "Парочка явно чем-то встревожена, сидят мрачнее тучи уткнувшись в тарелки."
    "Ладно Сёма, наверно не отошёл после нашего вчерашнего скандала, но подруга с чего такая поникшая?"
    un "Можно?.."
    "Тихонько спросила я."
    show mi smile pioneer with dspr
    mi "Да, пожалуйста!"
    "Подруга отодвинула мне стул."
    un "Ты утром сама не своя была..."
    "Встревоженно начала я."
    # show mi shocked pioneer at cleft with dspr # копипаста?
    show mi shocked pioneer with dspr
    mi "Ну… Не с той ноги встала…"
    "Мику нервно засмеялась."
    th "Что-то она темнит."
    "Встретилась взглядом с Семёном..." 
    "Но после вчерашнего общаться с ним нет никакого желания, и я тут же отвела глаза."
    show mi normal pioneer with dspr
    me "Как отдых проходит?"
    un "Хорошо."
    th "Не считая вчерашнего, мудак."
    me "Ясно…"
    un "А вы ничего про Славю не слышали?"
    show pi surprise aonl_pioneer with dspr
    me "А что такое?"
    un "Ну, её со вчерашнего дня никто не видел…{w} Сначала вы пропали… Но вы нашлись… А вот Славя…"
    me "Нет."
    mi "Не видели."
    un "Ну, я надеюсь, найдётся."
    show pi normal aonl_pioneer with dspr
    me "Да, и мы надеемся."
    show mt angry pioneer at center behind mi, pi with dissolve
    "Мы продолжили есть, как вдруг в столовую влетела Ольга Дмитриевна, размахивая руками и бешено ища кого-то взглядом."
    show mt rage pioneer at center with dspr
    stop music fadeout 3
    mt "Ах, вот вы где! Пойдём-ка поговорим!"
    "Тихо прошипела она прямо в лицо Семёну."
    "Немного поколебавшись, я незаметно пошла за ними."
    window hide
    play sound [sfx_open_door_2, sfx_close_door_1] 
    pause 1
    play ambience ambience_camp_center_day fadeout 1 fadein 2
    scene bg ext_dining_hall_near_day
    show mt scared pioneer at right
    show mi upset pioneer at center
    show pi upset aonl_pioneer at left
    with dissolve
    window show
    play music music_list ["no_tresspassing"] fadein 3
    "Отойдя от входа, Ольга о чём-то заговорила с ребятами и едва не разрыдалась." 
    "После чего повела их в лес."
    th "Ольга плачет?"
    "Меня пробрали мурашки." 
    "Если всесильная лагеря сего рыдает в страхе, то дело ОЧЕНЬ плохо."
    window hide
    play ambience ambience_forest_day fadeout 1 fadein 2
    scene bg ext_path_day with dissolve
    # play sound крик Мику. И в каких, Майн Гот, ебенях нам его искать я в душе не имею! 
    window show
    "Последовав за ними, я поначалу потеряла всех из виду, но крик Мику точно указал направление."
    th "Да что происходит в конце концов?! Почему у всех истерика?!"
    window hide
    scene bg ext_polyana_day with dissolve
    show mt scared pioneer at left
    show mi cry pioneer at center
    show pi surprise aonl_pioneer at right
    with dissolve
    window show
    "На поляне стояла плачущая Мику, в объятиях Ольги Дмитриевны и Семён смотрящий за дерево."
    "Когда он повернулся к девушкам, лицо юноши стало белее снега." 
    "Казалось, его вот-вот стошнит."
    mt "Кто это сделал?.."
    mt "Мне откуда знать!"
    "Сказала Ольга Дмитриевна, удивительно спокойным голосом."
    mt "Во всём лагере алиби нет только у вас."
    "Мику продолжала плакать, теперь уже у Сёмы на плече."
    show pi angry aonl_pioneer with dspr
    mt "Вы что, серьёзно думаете, что мы способны на… {w} Такое?!"
    "Он с ненавистью посмотрел на вожатую."
    mt "Ну, нет…"
    "Замялась Ольга."
    mt "Но кто-то же это сделал!"
    me "Я бы сказал, что это дикие животные какие-то. Возможно, волки."
    mt "Тут отродясь волков не водилось…"
    me "То есть вы думаете, что это мог сделать человек?!"
    mt "Ну, а больше некому…"
    me "Нет, это полный бред… Не может такого быть…"
    "Сёма крепче обнял Мику."
    "Её рыдания стали тише."
    mt "В общем, надо звонить в милицию."
    show mt normal pioneer at left with dspr
    me "Конечно надо! Пойдёмте!"
    stop music fadeout 3
    "Вся троица спешно удалилась с поляны."
    "Выждав немного я подошла к дереву, за которое заглядывал Семён."
    th "Что они там увидели?"
    window hide
    scene cg epilogue_mi_2 with dissolve
    play music music_list ["scarytale"] fadein 3
    window show
    "На поляне лежало тело мёртвой девушки, точнее того, что от неё осталось."
    "Куски рук вырваны с корнем из плеч, груди истерзаны в клочья, голова оторвана и порвана на куски, земля и трава насквозь пропитаны кровью. На меня уставился безжизненный голубой глаз, выглядывающий из куска черепа со светлыми волосами."
    th "Светлые волосы?"
    "Я вздрогнула от осознания."
    "Это не просто девушка, это Славя! Наша дорогая, милая Славя!"
    un "Н-нет, н-нет, н-нет…"
    "Глаза застилали слёзы, я начала заикаться, к горлу подкатил ком."
    "Попятившись, зацепилась за корень и рухнула на траву."
    "Перевернувшись и встав на четвереньки, я блеванула утренним завтраком обжигая пищевод и рот."
    th "Нет, нет, этого не может быть, только не Славя!"
    "Случившееся не укладывалось в голове, но безжизненный глаз, смотрящий прямо на меня, не оставлял сомнений, это Славя, моя подруга Славя!"
    show blink
    "Меня снова стошнило на траву, и я попыталась отползти в сторону, чтобы не испачкать одежду, но спустя пару метров снова блеванула и рухнула, потеряв сознание."
    window hide
    stop music fadeout 3
    stop ambience fadeout 2
    scene bg black
    pause 3
    hide blink
    play ambience ambience_forest_evening fadein 2
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    scene bg ext_polyana_sunset
    play music music_list ["into_the_unknown"] fadein 3    
    show unblink
    pause 1
    window show
    "Пришла в себя, когда солнце клонилось к горизонту."
    "Сначала не поняла, где нахожусь и что происходит."
    "Но, увидев траву, испачканную рвотой, всё вспомнила и меня едва не стошнило снова. {w} Благо, уже было нечем."
    "Вытерев рот платком на шатающихся ногах, я направилась к умывальникам."
    window hide
    play ambience ambience_camp_center_evening fadeout 1 fadein 2
    scene bg ext_washstand2_day with fade2
    play sound sfx_open_water_sink
    pause 1
    play sound_loop sfx_water_sink_stream
    window show
    "Благо, в этот раз кран работал."
    "Умыв лицо и прополоскав рот, я смогла мыслить более-менее адекватно."
    th "Кто-то убил девушку. Явно не зверь, а человек... Иначе бы её съели." 
    th "Но кто, а самое главное зачем? А вдруг этот монстр рядом?"
    "Вздрогнув осмотрелась по сторонам."
    stop sound_loop
    play sound sfx_close_water_sink
    # pause 1
    "Вроде всё тихо, но это ещё ничего не значит."
    "Я направилась в домик." 
    "Лучше посидеть там с Мику, вдвоём не так страшно."
    window hide
    play ambience ambience_int_cabin_evening fadeout 1 fadein 2
    scene bg aonl_int_house_of_un_sunset with fade2 # un house sunset
    window show
    "Подруги дома не оказалось."
    th "Где она бродит в такое время? А если…"
    "Я вздрогнула от ужаса."
    un "Нет-нет, неужели ещё и Мику!"
    window hide
    play ambience ambience_camp_center_evening fadeout 1 fadein 2
    play sound [sfx_open_dooor_campus_1, sfx_close_door_campus_1]
    pause 1
    scene bg ext_house_of_un_day with dissolve # ext un house sunset
    show sh surprise pioneer close  with dissolve
    window show
    "Я бросилась на поиски Мику, но у самого входа столкнулась с Шуриком."
    sh "Ай!"
    "Мы плюхнулись на землю в обнимку."
    un "Саш, Саш…"
    "Я пыталась угомонить колотящееся сердце."
    show sh surprise pioneer with dissolve 
    "Шурик аккуратно вылез из-под меня."
    un "Ты видел… Видел Мику?"
    show sh normal pioneer with dspr
    sh "Видел Лен, она в домике вожатой спит."
    un "Фух!!!!!!"
    th "Гора с плеч."
    un "Ты уже знаешь?"
    show sh upset pioneer with dspr
    sh "Все в лагере знают. Вожатая позвонила в милицию, велела всем ждать её распоряжений."
    show sh normal pioneer with dspr
    extend "А ты где была?"
    un "Я…?"
    un "Я спала в лесу…"
    "От осознания, случившегося снова вздрогнула."
    "Спала в лесу рядом с местом убийства и со мной могли сделать, что угодно!"
    "В ужасе схватилась за голову."
    th "Какая же я дура!"
    show sh serious pioneer with dspr
    sh "Вижу ты и сама всё поняла, ругать не буду. Ладно, я пойду к Серёге."
    un "Стой!"
    "Я схватилась за Сашу как утопающий за соломинку."
    un "Не оставляй меня одну, мне страшно!"
    show sh normal pioneer with dspr
    sh "Лен, Серёгу тоже не могу оставить одного, сейчас все сидят по домикам..." 
    sh "А ты, раз Мику спит, посиди на площади с Семёном. Он всё равно к ней потом собирался."
    un "Хорошо."
    "Не то чтобы меня это успокоило, но звучало вполне разумно."
    window hide
    stop music fadeout 3
    scene bg ext_square_sunset with dissolve
    show pi normal aonl_pioneer with dissolve
    window show
    "Попрощавшись, на площади я и вправду увидела со спины Семёна на лавочке."
    "Сгорбленная спина и напряжённые плечи выдавали крайнее беспокойство."
    "Я тихонько подошла ближе."
    show pi surprise aonl_pioneer with dspr
    "Сёма резко обернулся и вздрогнул."
    un "Ой, я не хотела тебя напугать…"
    th "Не лучший способ подойти выбрала. Дура. Сейчас же все на взводе."
    me "Ничего…"
    un "Можно я присяду?"
    show pi normal aonl_pioneer with dspr
    me "Да, садись, пожалуйста."
    "Я аккуратным движением разгладила юбку, и села рядом."
    un "Как всё это грустно…"
    show pi upset aonl_pioneer with dspr
    me "Да, весёлого мало."
    un "Как думаешь, кто это мог сделать?"
    me "Откуда же мне знать? Точно – не я."
    un "Нет-нет! Я тебя ни в коем случае не подозреваю!"
    "Я замахала руками."
    show pi normal aonl_pioneer with dspr 
    me "И на том спасибо."
    "Грустно ухмыльнулся он."
    un "Но это сделал очень жестокий, очень злой человек."
    me "Ну, необязательно…"
    th "Он о чём?"
    me "Может быть, разовое помутнение. Маньяки же в обычной жизни – милейшие люди."
    un "То есть ты хочешь сказать…"
    "Я открыла рот от удивления и посмотрела на парня."
    un "Что это мог сделать любой из нас?.."
    me "Ну, я не утверждаю, конечно… Но круг подозреваемых достаточно широк."
    un "Нет… Не мог это сделать никто из ребят… Не мог…"
    me "В любом случае, в этом разбираться милиции…"
    "Повисло тягостное молчание. Я смотрела на закат, а Семён изучал плитку под ногами."
    window hide
    play ambience ambience_int_cabin_night fadeout 1 fadein 2
    $ night_time()
    $ persistent.sprite_time = "night"
    # скример - что это?
    scene bg int_house_of_un_night with flash
    window show
    "Последний луч света закатного солнца попал в глаз" 
    "И я на секунду ослепла и вновь увидела фигуру с ножом..."
    "А когда проморгалась, оказалось, что сижу дома и уже ночь!"
    un "Что это!"
    "В панике начала осматриваться."
    "Ничего не изменилось. Это мой домик, вот только не ясно как сюда попала?"
    th "Мику нет, а значит я абсолютно одна!"
    window hide
    play sound [sfx_open_dooor_campus_1, sfx_close_door_campus_1]
    play ambience ambience_camp_entrance_night fadeout 1 fadein 2
    pause 1
    scene bg aonl_ext_house_of_un_night with dissolve
    play music music_list ["into_the_unknown"] fadein 3
    window show
    "Задрожав от страха, я выскочила наружу." 
    "Почувствовала, что вот-вот зареву на всю округу, но сглотнув ком в горле." 
    "Сжала зубы и медленно направилась к вожатой, надеясь, что там меня защитят."
    "Со всех сторон раздавалась громкая трель сверчков, а впереди показалась какая-то тень."
    th "Кто это, убийца?"
    # Спрайт Семёна
    me "Ты что тут так поздно делаешь?"
    "На дороге показался Семён с обрезком трубы."
    th "Слава Богу!"
    un "Я… Я…"
    "Он ласково приобнял меня, а я вцепилась в его рубашку заплакав сильнее."
    me "Пойдём."
    window hide
    scene bg ext_house_of_mt_night with dissolve
    show pi normal aonl_pioneer at cleft
    show dv sad pioneer at cright
    with dissolve
    window show
    "Он отвёл к Алисе."
    "Рыжая тоже оказалась на грани паники."
    un "Я сидела одна и… Уже поздно было и… А Мику всё нет…."
    un "И я… А тут же ещё такое со Славей… И я…"
    me "А ты случайно не знаешь, где Ульяна и Ольга Дмитриевна?"
    "Я удивлённо посмотрела на Сёму."
    un "Нет, а что… Они тоже пропали?"
    me "Ну, мы этого пока не знаем…"
    dv "Семён…"
    me "Да?"
    dv "Тебе не кажется, что в лагере слишком тихо?"
    show pi upset aonl_pioneer with dspr
    me "Так ночь же, спят все…"
    "Я прислушалась. {w} Раздавался лишь стрекот кузнечиков и больше ничего."
    me "А как здесь обычно?"
    un "Тихо…"
    "Шёпотом произнесла я."
    dv "Тихо, но не так."
    me "Ладно, давайте мыслить рационально."
    show dv surprise pioneer at cright with dspr
    th "Что он задумал."
    me "Люди же просто так не исчезают!"
    un "Значит…"
    play sound sfx_bush_leaves
    show pi surprise aonl_pioneer at cleft
    show dv scared pioneer at cright
    with dspr
    "За домиком зашелестели кусты."
    show el normal pioneer at center # сзади или спереди Семёна и Алисы?
    show pi surprise aonl_pioneer at left
    show dv scared pioneer at right
    with dissolve
    "Мы даже не успели испугаться, как из темноты выскочил Серёжа."
    el "Ах, вот вы где!"
    show pi normal aonl_pioneer with dspr
    me "Господи, не надо так пугать! Девочек инфаркт хватит!"
    show el sad pioneer with dspr
    el "Извините, да…"
    me "Чего пришёл?"
    el "Вы не видели Шурика?"
    me "Нет…"
    th "Неужели и он пропал?!"
    el "Да и слишком тихо как-то тут…"
    me "Мы уже заметили!"
    el "Нигде не горит свет, тишина…"
    me "Ладно, не надо атмосферу нагнетать! Без тебя тошно!"
    show el smile pioneer at center with dspr
    el "А что? Я ничего…"
    "Он загадочно улыбнулся от чего по мне забегали мурашки."
    me "Ладно, я обойду лагерь, а вы оставайтесь здесь!"
    un "Один?"
    "Да, пожалуй, не лучшая идея…{w} Надо сначала думать, а потом говорить."
    me "Ну…"
    show dv normal pioneer at right with dspr
    dv "Я пойду с тобой!"
    me "Ладно, тогда вы оставайтесь тут! И не забывайте, что в домике Ма… Мику спит."
    show el normal pioneer with dspr
    el "Так точно!"
    stop music fadeout 3
    hide dv
    hide pi
    with dissolve
    "Сёма и рыжая ушли, оставив меня с Сергеем."
    "Электроник сел на ступеньки, оперся локтями о колени, опустил голову на руки и, кажется, задремал."
    "Я опёрлась спиной о стенку домика. Пытаясь осмыслить случившееся."
    th "Вокруг творится какой-то кошмар. Ещё вчера лагерь казался приветливым и дружелюбным, а теперь превратился в тюрьму с убийцей. Моя подруга убита, вероятно другие пионеры исчезли, и убийца возможно среди нас, но кто?"
    th "Мику? Бред! Семён? Та же песня. Вообще любой человек из лагеря может быть убийцей, хоть пионеры, хоть повариха."
    "Я незаметно покосилась на Серёжу."
    "Он продолжал сидеть на месте полностью уйдя в себя."
    th "Может он? Нет, невозможно, Серёжа добрейший парень, мухи не обидит. Убийца точно не среди нашей компании."
    th "Но кто же тогда и почему именно сейчас? Ведь прошло почти две недели, он мог давно начать действовать, а не ждать столько времени."
    play sound sfx_bush_leaves
    play music music_list ["orchid"] fadein 3
    "Слева зашелестели кусты."
    "Я вздрогнула, вжавшись в стенку домика."
    th "Мамочки, верните меня домой, пожалуйста, молю!" 
    th "Я не хочу знать кто, зачем и что сделал, я просто девочка, которая хочет к родителям, отпустите меня домой прошу!"
    th "Убийца мог напасть откуда угодно, казалось я даже слышу чужое дыхание и меня вот-вот разорвут в клочья."
    th "Затравленным взглядом осматривала округу боясь упустить момент нападения и сильнее вжималась в стену, надеясь хотя бы защитить спину." 
    th "Серёжа тем временем продолжал изучать пол, как будто просто сидит дома."
    th "Не знаю, сколько так простояла, может час, может 5 минут, но через некоторое время из темноты послышались какие-то разговоры."
    show pi upset aonl_pioneer at right
    show dv sad pioneer at left
    with dissolve
    "Из мрака сгустились две фигуры я вздрогнула, но это оказались Сёма с Алисой."
    el "Ну как?"
    me "Никого."
    un "Как это… Никого?"
    show dv cry pioneer at left with dspr
    dv "Все исчезли…"
    "Сквозь слёзы сказала Алиса."
    play sound sfx_drop_pipe
    "Она бросилась мне в объятия и зарыдала в голос, я тоже заплакала, перестав сдерживаться."
    th "Как это ВСЕ исчезли?! За что, за что с нами так?!"
    "Из истерики меня вывел крик Электроника."
    el "Кто?"
    "Юноша сердито смотрел на Семёна."
    me "Не знаю! Может, ты!"
    "Сёма сжал кулаки."
    show el angry pioneer at right with dspr
    el "Может, ты!"
    show pi angry aonl_pioneer with dspr
    me "Уж точно не я."
    el "И чем докажешь?"
    me "С какой стати я должен перед тобой оправдываться?"
    el "Только у тебя нет алиби!"
    me "А у тебя, значит, есть?"
    el "Я был у себя в домике – Шурик подтвердит!"
    me "Да, только вот Шурик временно недоступен…"
    "Серёжа скрипнул зубами и отвернулся."
    el "В любом случае у меня-то алиби есть. Да что я перед тобой оправдываюсь? Я полностью в себе уверен!"
    me "Хорошо быть уверенным в себе… Я тоже в себе уверен! Да и Мику может подтвердить – я всё время был с ней."
    el "Плохой свидетель…"
    me "Не хуже твоего!"
    "Да они же сейчас набросятся друг на друга!"
    un "Мальчики, хватит…"
    "Ребят осеклись, посмотрев на меня."
    stop music fadeout 3
    show pi upset aonl_pioneer with dspr 
    me "Ладно, извини…"
    show el upset pioneer at right with dspr
    el "Да…"
    me "В общем, нам стоит держаться вместе…"
    th "Разумная мысль."
    show dv sad pioneer at center with dspr
    dv "Это поможет нам не исчезнуть?"
    "Робко спросила Алиса."
    show pi normal aonl_pioneer with dspr
    me "Не знаю, как насчёт не исчезнуть, но остаться в живых должно помочь!"
    "Сёма глянул на часы!"
    "По моим ощущениям была часа 4 утра."
    me "Ладно, отряд! Пора спать, а то совсем без сил останемся."
    un "Но…"
    me "Никаких но!"
    "Никто не стал больше возражать, и мы все тихо зашли в домик."
    window hide
    play ambience ambience_int_cabin_night fadeout 1 fadein 2
    scene bg int_house_of_mt_night with dissolve
    $ persistent.sprite_time = "sunset"
    show pi normal aonl_pioneer at right with dissolve
    window show
    mi "А? Что такое?.."
    show mi sad pioneer at center with dissolve
    "Мы разбудили Мику."
    me "Ничего, спи…"
    "Но она уже села на кровати и непонимающе смотрела на собравшихся."
    show el upset pioneer at left with dissolve
    el "Понимаешь, тут…"
    un "Они все исчезли! Пропали! Их больше нет!"
    "Я в слезах бросилась на шею Мику."
    show mi shocked pioneer at center with dspr
    mi "Что? Что случилось-то? Можешь внятно объяснить?"
    me "В общем…"
    me "Похоже, нас в этом лагере осталось пятеро…"
    el "То есть все присутствующие в этой комнате!"
    me "Спасибо, капитан! Будешь первым дежурить!"
    show el shocked pioneer at left with dspr
    el "Что?"
    me "Ничего! Или ты думаешь, безопасно всем сразу спать?"
    show el upset pioneer at left with dspr
    el "Ну, нет… Но…"
    me "Вот и всё!"
    "Сёма протянул ему металлическую трубу и медленно подошёл к кровати, на которой сидели мы с Мику."
    me "Если вы не возражаете…"
    hide el
    hide pi
    hide mi
    with dissolve
    "Парень, перелез через нас и отвернулся к стене."
    mi "Но как же…"
    me "Никак… Спать!"
    "Меньше чем через минуту он засопел."
    "Мику погладила меня по волосам и шёпотом посоветовала тоже прилечь."
    "Я так сильно измоталась морально и физически, что даже не стала спорить." 
    "Мы легли рядом с Сёмой и вскоре заснули."
    window hide
    stop ambience fadeout 2
    scene black with fade2
    pause 1
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day fadein 2
    scene bg int_house_of_mt_day
    with dissolve2
    window show
    "Сёма разбудил нас, когда основательно рассвело."
    show el normal pioneer at fleft with dissolve
    el "Уже?.."
    show pi angry aonl_pioneer at center with dissolve 
    me "Ты только и дрыхнешь! Пока я всю ночь… Сидел здесь…"
    show el upset pioneer at fleft with dspr
    el "Извини…"
    "Серёжа опустил голову."
    show pi normal aonl_pioneer with dspr
    me "Да ничего…"
    show mi smile pioneer at cleft with dissolve
    mi "Ох, как есть хочется."
    "Маша потянулась и мило улыбнулась."
    show mi surprise pioneer at cleft with dspr
    mi "А почему вы все здесь?"
    un "Ты не помнишь?"
    mi "Нет, а что такое?"
    show dv sad pioneer at fright with dissolve
    dv "Все исчезли…"
    "Мрачно сказала Алиса."
    show mi shocked pioneer at cleft with dspr
    mi "Что?"
    dv "Все исчезли… Испарились…"
    show mi normal pioneer at cleft with dspr
    "Маша посмотрела в окно и ничего не сказала.{w} Похоже, она вспомнила…"
    me "Ладно… Поесть – действительно отличная идея!"
    "Никто не стал возражать."
    window hide
    play ambience ambience_dining_hall_empty fadeout 1 fadein 2
    scene bg int_dining_hall_day with fade2
    play music music_list["just_think"] fadein 3
    window show
    "Вскоре мы сидели в столовой и молча уплетали кто что нашёл."
    show mi normal pioneer at cleft
    show el normal pioneer behind mi at fleft
    show pi upset aonl_pioneer at cright
    show dv sad pioneer at fright
    with dissolve
    mi "Может, мне что-нибудь приготовить?"
    "Тихо поинтересовалась Маша."
    me "Давай в обед. Сейчас и так сойдёт."
    show mi upset pioneer with dspr
    "Девушка погрустнела."
    el "Хорошо, и что будем делать?"
    show pi normal aonl_pioneer with dspr
    me "Надо выбираться отсюда."
    un "Но ведь милиция…"
    me "Надо выбираться отсюда!"
    "Упрямо повторил Семён."
    dv "Но как?"
    me "Автобус."
    dv "Но ведь он редко ходит…"
    me "Должно же у него быть расписание."
    me "Тогда пешком! Всё лучше, чем сидеть здесь!"
    un "Но ведь далеко…"
    me "Может, попутку поймаем."
    show el upset pioneer with dspr
    el "Здесь-то? Навряд ли…"
    me "Хватит уже драматизировать!"
    el "Я не драматизирую, но…"
    me "Ну вот и всё."
    show dv sad pioneer with dspr
    dv "И что скажем, когда доберёмся до города?"
    me "Как есть, так и скажем – приехали снимать фильм, а тут…"
    show el surprise pioneer
    show dv surprise pioneer
    with dspr
    el "Какой фильм?"
    play music_list ["doomed_to_be_defeated"] fadein 2
    show pi angry aonl_pioneer with dspr
    me "Хватит придуриваться уже, а?"
    th "Про что это он?"
    me "Если вчера это ещё было смешно, то сегодня уже хватит!"
    el "Я тебя не понимаю…"
    me "Ты опять будешь утверждать, что приехал сюда не снимать фильм, а притворяться пионером?"
    dv "Ничего не понимаю…"
    "Алиса удивлённо окинула всех взглядом."
    dv "Но ведь мы и есть пионеры…"
    show mi rage pioneer with dspr
    mi "Какие мы к чёртовой матери пионеры?!"
    "Вмешалась в разговор молчавшая до этого Мику."
    mi "На дворе XXI век! Пионеры, ага!"
    dv "Двадцать…"
    el "Первый?"
    show pi normal aonl_pioneer
    show mi dontlike pioneer 
    with dspr
    me "Ладно, то есть вы хотите сказать, что все вы…" 
    me "Ладно, мы… Обычные пионеры, которые вот так просто приехали сюда на недельку-другую отдохнуть?"
    "Повисло тягостное молчание."
    dv "Ну… Да…"
    me "Мы на секундочку…"
    play sound [sfx_open_door_2, sfx_close_door_1]
    stop music fadeout 3
    hide mi
    hide pi
    with easeoutright 
    "Мику и Семён покинули столовую."
    "Мы с ребятами переглянулись."
    "В наших глазах читался один и тот же вывод."
    "Они, что-то скрывают."
    show dv sad pioneer with dspr
    play music music_list ["orchid"] fadein 3
    el "А если это они?"
    show dv angry pioneer with dspr
    dv "Ты рехнулся?"
    el "Нет, рехнулись Семён и Мику! Вы их слышали? Кино, XXI век, мы не пионеры, а кто тогда блин!"
    "Юноша ударил кулаком по столу."
    un "Серёж, успокойся пожалуйста."
    show el angry pioneer with dspr
    el "Да какой успокойся Лен?!" 
    el "Славю убили, толпа людей исчезла бесследно, мой друг пропал!" 
    el "Ты это понимаешь?! МОЙ ДРУГ ПРОПАЛ?!"
    "Казалось, у Серёжи сейчас начнётся истерика."
    dv "Отставить панику!"
    "Грозно сказала Алиса."
    show dv sad pioneer with dspr
    "Электроник чуть притих."
    el "Я не паникую, но согласись эти двое ведут себя странно."
    el "Оба обеспечивают друг другу алиби, а если они действуют сообща?"
    un "Мику и Семён не могли это сделать."
    show dv guilty pioneer with dspr
    dv "Почему так уверена?"
    un "Я… Случайно видела, как вожатая приводила их на место гибели Слави." 
    un "У Мику тут же началась истерика, а Семён побелел от страха..." 
    un "Убийцы так себя не ведут."
    dv "Ты за ними шпионила?"
    un "Это получилось случайно, я не специально!"
    "Под пристальным взглядом ребят опустила глаза к тарелке."
    show el normal pioneer
    show dv normal pioneer
    with dspr
    el "Ладно Лен, проехали. И всё же даже, если они не виновны, то ведут себя странно. Одна Мику чего стоит."
    show dv sad pioneer with dspr
    dv "А что с ней?"
    el "Ты не заметила?"
    dv "Что именно?"
    "Кажется, я догадалась."
    un "Она молчит."
    dv "И что с т…"
    show dv shocked pioneer with dspr
    "Алиса осеклась на полуслове, осознав смысл слов."
    dv "Невероятно!"
    show el serious pioneer with dspr
    el "Вот именно! Девочка, способная потоком слов замучит кого угодно, теперь большую часть времени помалкивает!" 
    el "Это нифига не нормально!"
    show dv guilty pioneer with dspr
    dv "Не спеши ботаник, может она такая после случившегося. Любой на её месте будет ходить как пришибленный."
    un "Она… Она и на линейке была такой и на завтраке и утром вела себя странно..." 
    un "Спрашивала, что я делаю в нашем домике, будто там не живу." 
    un "Да и вместе с Сёмой постоянно. Раньше Семён избегал Мику, а теперь чуть ли не за ручку ходят, о чём-то шушукаются."
    el "Да что же творится, блин!"
    "Серёжа схватился за голову."
    show dv normal pioneer 
    show el normal pioneer
    with dspr
    dv "Думаю стоит их припереть к стенке и всё разузнать. Вернуться берём за глотку и допрашиваем. Хотя бы часть вопросов закроем."
    el "Согласен!"
    "Я промолчала, продолжая изучать содержимое тарелки."
    window hide
    stop music fadeout 3
    show dv shocked pioneer
    show el serious pioneer
    with fade
    show mi scared pioneer at cleft behind el
    show pi upset aonl_pioneer at cright behind dv
    with dissolve
    window show
    mi "Ребята, помогите!"
    "На пороге показалась Мику, тянувшая за руку Семёна." 
    "Лицо парня побелело от страха, а сам он пошатывался, едва держась на ногах."
    el "Держитесь!"
    "Сергей с Алисой подхватили Семёна и помогли ему сесть на стул. Мику принесла стакан воды."
    dv "Что случилось?"
    "Напившись, Семён вдохнул поглубже и произнёс."
    play music music_list ["into_the_unknown"] fadein 3
    me "Я видел Ульяну."
    show dv angry pioneer with dspr
    dv "Где?! Почему её не привёл?!"
    "Алиса сорвалась с места, но её схватила за руку Мику."
    mi "Стой!"
    dv "Что ещё!?"
    mi "Дослушай."
    me "Это была не Ульянка…" 
    me "То есть, что-то похожее на Ульянку… Или мёртвая Ульянка."
    show dv shocked pioneer    with dspr 
    dv "Чего?!"
    "Стакан в руках Семёна заметно подрагивал, он часто проглатывал слова. Чтобы парень ни увидел его это сильно напугало."
    me "ЭТО БЫЛ ЗОМБИ!"
    "Выкрикнул Семён."
    me "У Ульяны частично оторвана челюсть, она буквально гнила заживо при этом ходила и даже могла говорить!"
    "Мы выпучили глаза по 5 рублей."
    me "Я не шучу так всё и было. Это существо ходит по лагерю!"
    window hide
    show mi scared pioneer
    show el scared pioneer
    show dv scared pioneer
    with fade
    window show
    "Поведение Сёмы не оставляло сомнений, он говорит правду!"
    el "Офигеть!"
    "Я закрыло лицо руками и заплакала."
    th "Пожалуйста, заберите меня отсюда кто-нибудь!"
    window hide
    play ambience ambience_camp_center_day fadeout 1 fadein 2
    scene bg ext_dining_hall_near_day with dissolve
    show mi normal pioneer at cleft
    show el normal pioneer behind mi at fleft
    show pi upset aonl_pioneer at cright
    show dv sad pioneer at fright
    with dissolve
    window show
    el "Одно понятно – тут творится что-то, что наука пока не может объяснить!"
    dv "Да чертовщина здесь творится самая настоящая! Бесовщина! В церковь бы… Свечку бы…"
    "Я лишь тихо всхлипывала."
    show pi normal aonl_pioneer with dspr
    me "Теперь точно понятно, что надо выбираться отсюда!"
    show el normal pioneer with dspr
    el "Я, конечно, не учёный… Тем более не экстрасенс, но, насколько я знаю, всякие демоны и духи обитают в одном месте. Следовательно, если мы уйдём подальше от этого места…"
    show mi grin pioneer with dspr
    mi "Да, отличное решение!"
    "Скептически ухмыльнулась Мику."
    me "Согласен."
    "Воскликнул Сёма!"
    show dv normal pioneer with dspr
    dv "Да!"
    "Я лишь кивнула."
    me "Значит, решено!"
    "Сёма ударил кулаком по столу и вскочил."
    show mi dontlike pioneer with dspr
    mi "Подожди! Ничего ещё не решено…"
    show pi angry aonl_pioneer with dspr
    me "Чего тормозить-то?! Я больше с подобными штуками встречаться не хочу!"
    mi "И куда мы пойдём? Ты хоть представляешь, сколько пешком до города?"
    me "Да что, по этой дороге никто не ездит, что ли? Машина, автобус – что-нибудь, да увидим!"
    show el upset pioneer with dspr
    el "Не факт…"
    me "Значит, лучше сидеть здесь?"
    el "Ну, я этого не говорил…"
    un "Здесь страшно… Особенно ночью…"
    "Тихо прошептала я."
    mi "Это ещё не значит, что надо куда-то идти!"
    "Громко сказала Мику."
    show pi normal aonl_pioneer with dspr
    me "Хорошо, давайте проголосуем!"
    mi "Ладно…"
    "Она пожала плечами."
    me "Уходим!"
    show mi normal pioneer with dspr
    mi "Остаёмся."
    show dv sad pioneer with dspr
    dv "Давайте попробуем – может, правда встретится попутка."
    el "Уходим…"
    "Все посмотрели на меня."
    "Все повернулись ко мне."
    un "Я не хочу здесь оставаться…"
    me "Ну что же!"
    "Сёма вскочил со стула. Остальные сидели, понурив головы."
    show mi dontlike pioneer with dspr
    me "Раз решили…"
    mi "Ну, раз решили…"
    "Мику тоже поднялась."
    show dv sad pioneer with dspr
    dv "А вещи?"
    "Неуверенно спросила Алиса."
    el "Думаешь, сейчас это самое главное?"
    "Грустно сказал Серёжа."
    dv "Ну да, пожалуй…"
    "Больше никто не спорил."
    stop music fadeout 3
    window hide
    play ambience ambience_camp_entrance_day fadeout 1 fadein 2
    scene bg ext_no_bus with fade2
    window show
    "Через пару минут мы вышли на автобусную остановку."
    show mi normal pioneer at center
    show el normal pioneer at right
    show dv sad pioneer at left
    show pi normal aonl_pioneer at fright
    with dissolve
    mi "Город – туда."
    "Мику указала рукой."
    me "Он был там позавчера…"
    "Ухмыльнулся Сёма."
    el "Да-да, туда."
    "Подтвердил Серёжа."
    "Мы некоторое время постояли молча, собираясь с силами, затем медленно двинулись в путь."
    window hide
    play ambience ambience_day_countryside_ambience fadeout 1 fadein 2
    scene bg ext_road_day with dissolve
    window show
    "Летнее солнце нестерпимо палило, плавя асфальт."
    "Дорога, деревья, трава, небо на расстоянии дальше ста метров сливались в яркое марево, больше похожее на горящий туман."
    "Солнце нестерпимо жгло мои волосы, словно к голове приложили утюг."
    "Ребята находились не в лучшем положении. Они вели нас за собой, но сами обливались потом и едва держались на ногах."
    "Мы совсем не взяли воды и никак иначе не подготовились. Просто ломанулись из лагеря как можно быстрее."
    "В какой-то момент меня замутило, голова стала тяжёлой, а непрерывный стрёкот кузнечиков давил на уши, лишая последних сил."
    show blink
    "Глаза закрылись буквально на секунду."
    scene bg black
    dv "АААААААААААААААА!!!!!!"
    "Сквозь закрытые веки, я услышала крик Алисы, но сил посмотреть, что случилось уже не осталось."
    me "Что такое?"
    dv "Она потеряла сознание!"
    "Кажется меня куда-то несут, но я не уверена, тело горело от нестерпимой жары, а голова раскалывалась."
    "Не уверена, но похоже меня обмахивали платком."
    "Какое-то время ничего не происходило, но вдруг я услышала голоса."
    mi "Нашли что-нибудь?"
    me "Нашли… Лагерь…"
    mi "Какой?"
    me "Наш…"
    mi "Что?"
    mi "Вы же шли вперёд, а не назад."
    me "Вперёд… И там Совёнок."
    mi "Хватит прикалываться!"
    "Вскрикнула Мику."
    me "Я серьёзно…"
    dv "Но…"
    me "Вот так…"
    mi "Ладно, значит, пойдём туда!"
    me "Слушай, что с тобой такое?"
    mi "В смысле?"
    me "Вчера ты боялась, а сегодня выглядишь так, как будто с тобой каждый день происходит что-то подобное."
    mi "Ну а какой смысл паниковать?"
    me "Если бы не знал тебя…"
    mi "Идём в лагерь! Ну или туда, где вы были… Если это тот же лагерь…"
    me "Хорошо…"
    mi "Но её придётся нести."
    me "Понимаю… Сейчас придумаем что-нибудь."
    "Кажется брежу."
    "Меня куда-то переложили и понесли, я попыталась встать, но ничего не вышло."
    "Далее слышала лишь обрывки фраз."
    dv "Надо отнести её в домик."
    mi "Не смотри!"
    me "Да что я там не видел…"
    me "Опасно одним…"
    mi "Хочешь составить компанию?"
    me "Тогда… будьте осторожны…"
    "Долгое время ничего не происходило, казалось в мире не осталось ничего кроме тьмы."
    "Но вдруг сквозь тишину мира прорвался душераздирающий крик Мику."
    window hide
    hide blink
    #скример
    $ night_time()
    $ persistent.sprite_time = "sunset"
    play ambience ambience_int_cabin_night fadeout 1 fadein 2
    play music music_list ["into_the_unknown"] fadein 3
    scene bg int_house_of_mt_night
    show el scared pioneer at left
    show mi sad pioneer at center
    show pi upset aonl_pioneer at right
    show unblink
    pause 1
    window show
    "С трудом разлепила глаза и увидела рыдающую Мику и ошеломлённых мальчиков."
    th "Так, а почему мы в домике Ольги Дмитриевны?"
    un "Что такое?.."
    "Спросила я шёпотом."
    me "Не… Выходи… Наружу…"
    "Простонал Семён."
    "Мику лежала на коленях Семёна, Саша трясся в углу кровати, а напротив сидела я, сжавшись от ужаса."
    th "Что же там такого случилось от чего ребята белее снега, а Мику без сознания? И где Алиса?"
    "Повисло тягучее молчание, такое густое и ощутимое что его можно было резать ножом, даже кузнечики прекратили своё стрёкот."
    "Мы продолжали сидеть, боясь шевельнуться, пока Мику не заворочалась."
    play ambience ambience_music_club_night fadein 3
    show mi scared pioneer close at right with dissolve
    mi "Мне такой кошмар снился…"
    me "Это был не сон…"
    "Она широко открыла глаза и с ужасом посмотрела на Сёму."
    show mi cry pioneer close at right with dspr
    mi "Тогда… там?!"
    me "Не смотри!"
    "Вскричал он и крепко обнял девушку."
    "Я, бросилась к Семёну на шею и зарыдала, дрожа всем телом."
    "Сейчас парень казался единственным островком безопасности."
    "Долгие минуты проходили в мучительной тишине."
    mi "И что… Нам теперь делать?"
    "Сквозь слёзы спросила Маша."
    "После непродолжительного молчания Семён тихо сказал."
    me "Нам надо идти…"
    show pi upset aonl_pioneer close at right
    show mi cry pioneer close at center
    with dissolve
    "Мы с мику ещё крепче прижались к парню."
    show el upset pioneer behind mi with dspr
    el "Надо…"
    "Серёжа перестал трястись и слез с кровати."
    me "Как ты себя чувствуешь?"
    "Я не сразу поняла, что обращаются ко мне."
    me "Идти можешь?"
    show pi normal aonl_pioneer close at left with dspr
    un "Наверное…"
    show pi normal aonl_pioneer at right
    show mi cry pioneer at center
    with dissolve
    "Он бережно освободился от наших объятий и встал."
    me "Надо бежать! Ночью будет проще идти."
    show mi sad pioneer with dspr
    mi "Но мы же…"
    "Робко возразила Мику."
    me "Да, решили пока оставаться здесь, но… В общем, надо бежать!"
    "Он повернулся к Серёже."
    me "Ты понимаешь, что там… Им не надо этого видеть."
    "Юноша кивнул."
    me "Возьмёмся за руки и пойдём. Я первый, поведу вас, потом Маша, потом Лена, потом ты."
    me "Готовы?"
    "Мы с Мику и Серёжей сидели тише воды ниже травы. Почему он назвал её Маша?"
    "Семён взял Мику за руку, обернулся и внимательно посмотрел на меня и Сергея."
    me "Закройте глаза и ни в коем случае не открывайте, поняли?"
    el "Да…"
    window hide
    stop music fadeout 3
    show blink
    pause 1
    window show 
    "Я кивнула и закрыла глаза."
    "Судя по звуку Сёма открыл дверь и повёл всех наружу."
    stop ambience fadeout 2
    me "Осторожно, ступеньки!"
    window hide
    play sound [sfx_open_dooor_campus_1, sfx_close_door_campus_1]
    play ambience ambience_camp_entrance_night fadeout 1 fadein 2
    $ renpy.pause(1)
    play music music_list ["orchid"] fadein 3
    hide blink
    scene bg ext_square_night
    show el scared pioneer at left
    show mi sad pioneer at center
    show pi upset aonl_pioneer at right
    show unblink
    pause 1
    window show
    "Сёма разрешил открыть глаза только на площади."
    mi "Она… Всё ещё там?"
    "Спросила Мику, не отпуская мою руку."
    "Семён лишь кивнул."
    un "Кто?! Алиса?!"
    "Я снова и разрыдалась."
    "Мику обняла меня и попыталась успокоить."
    el "Что с ней?"
    "Заплетающимся языком спросил Серёжа."
    me "Думаю, ты не хочешь этого знать."
    "Некоторое время мы просто стояли на площади."
    show mi cry pioneer with dspr
    "Я рыдала, Серёжа ходил вокруг нас кругами, а Мику села на скамейку и закрыла лицо руками."
    "В глазах окружающих читалась она и та же мысль – это конец."
    "Чтобы мы ни делали судьба уже предрещена."
    me "Пора…"
    "Тихо сказал Семён, но никто не шелохнулся."
    me "Здесь оставаться нельзя!"
    "Он подошёл к Мику, наклонился и взял её за руку."
    "Она подняла на него заплаканные глаза и кивнула."
    "Мы медленно пошли в сторону автобусной остановки, словно приговорённые к смерти, пытающиеся отсрочить неизбежное…"
    stop ambience fadeout 2
    window hide
    scene bg black
    with dissolve
    window show
    "На лагерь опустилась ночь и тишина, даже кузнечики замолчали."
    "Но вдруг они снова затянули свою песню, только уже иначе."
    window hide
    scene bg ext_no_bus_night
    with dissolve
    play ambience ambience_camp_entrance_night fadein 3
    show mi scared pioneer at center
    show pi normal aonl_pioneer at right
    show el scared pioneer at left
    with dissolve
    window show
    "Мы вышли на автобусную остановку и остановились в нерешительности."
    show mi sad pioneer with dspr
    mi "В какую сторону?"
    "Спросила Маша, вытирая слезы."
    me "Направо мы уже ходили… Пойдём налево."
    show mi sad pioneer with dspr
    mi "Но там ведь нет города…"
    me "А направо ещё пару дней назад не было такого же лагеря…"
    un "Может, не надо…"
    "Тихо всхлипнула я."
    me "У нас нет выбора… Я больше здесь ни секунды не останусь!"
    "Мы уже собирались двинуться в путь, как вдруг вдалеке послышались какие-то звуки."
    stop music fadeout 3
    "По дороге кто-то шёл."
    show el shocked pioneer at left with dspr
    el "Автобус!"
    "Радостно вскричал Серёжа."
    me "Тихо, дурень! Какой автобус! Это люди!"
    "Зашипел на него Сёма."
    show mi shocked pioneer at center with dspr
    mi "Много людей…"
    "Испуганно сказала Маша."
    "Стало понятно, что здесь оставаться нельзя."
    stop ambience fadeout 2
    play sound_loop sfx_hell_crickets_1 fadein 5
    "С другой стороны дороги к нам тоже кто-то приближался.{w} Шум всё усиливался."
    "Стрекотание кузнечиков... Но не обычное, а гораздо громче, искажённое,."
    me "Бежим!"
    "Крикнул Семён, но все остались на месте."
    stop sound_loop fadeout 5
    play music music_list["scarytale"] fadein 3
    me "Да вашу мать!"
    "Он схватил Мику и меня за руки и бросился назад в лагерь."
    window hide
    scene bg ext_square_night
    with dissolve
    show mi scared pioneer at cright
    show pi upset aonl_pioneer at cleft
    with dissolve
    window show
    "Мы едва поспевали, он буквально тащил нас за собой."
    "Выбежав на площадь, мы остановился, чтобы отдышаться, и только тогда поняли, что Серёжа остался там."
    show mi shocked pioneer at cright with dspr
    mi "Надо вернуться за ним!"
    "Закричала Мику и дёрнулась по направлению к автобусной остановке."
    me "Куда?!"
    "Семён потянул её на себя и удержал на месте."
    me "Хочешь, чтобы мы все там легли?!"
    "Я ничего не говорила, лишь дрожала от страха вцепившись в Семёна."
    me "Бежим дальше!"
    mi "Куда?!"
    me "Не знаю, в лес!"
    "Мы метнулись по направлению к лесу."
    window hide
    $ persistent.sprite_time = "night"
    scene bg ext_path2_night with dissolve:
        pos (0,0)
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (5,5)
        pos (0,0)
        linear 0.1 pos (0,-5)
        linear 0.1 pos (0,5)
        repeat
    window show
    "Сёма держал нас за руки, я с трудом поспевала за ребятами, несколько раз падала, но парень поднимал меня и подстёгивая криками тянул дальше."
    "Мы с трудом продирались через заросли. Хоть на небе и светила полная луна, но мы всё равно в темноте постоянно натыкались на коряги, ветки, попадали в ямы."
    "По ногам хлестала крапива, а по лицу били листья, оставляя болезненные царапины."
    "Сердце тяжело колотилось, из груди вырывался хриплый свист при каждом выдохе, а кровь в голове стучала так сильно, что, казалось, черепная коробка была готова разорваться от давления в любую секунду."
    "Я уже ничего не хотела, лишь бы это закончилось."
    window hide
    scene bg ext_polyana_night with dissolve
    window show
    "Наконец мы выбежали на поляну и остановились."
    "Семён присел на поваленное дерево, а мы с Мику повалились на землю."
    "Что это были за существа?"
    "И откуда эти звуки, стрекотание?"
    "Через некоторое время к нам, шатаясь, подошёл Семён. Мне уже было всё равно, я лишь остекленевшим взглядом смотрела на небо пытаясь угомонить колотящееся сердце."
    "Мику сидела рядом, обхватив руками колени, и раскачивалась из стороны в сторону."
    show mi sad pioneer at center 
    show pi upset aonl_pioneer at left
    with dissolve
    me "Нам надо что-то делать…"
    "Сказал Сёма, сев рядом."
    mi "Уже поздно… Мы умрём…"
    "Отсутствующим голосом прошептала подруга."
    me "Мы ещё живы, значит, надежда есть."
    mi "Нет, уже ничего нету… Всё кончено…"
    "Он обнял её и прижал к себе."
    me "Нет, не кончено…"
    window hide
    stop music fadeout 3
    play ambience ambience_forest_night fadein 3
    with fade
    show mi normal pioneer close at center with dissolve
    window show
    mi "Прости меня…"
    "Тихо прошептала Мику."
    me "За что?"
    mi "За всё… За то, что я была такой… За то, что не получилось…"
    me "Сейчас не самое подходящее время…"
    "Нежно сказал парень."
    th "С чего они так воркуют."
    mi "Нам осталось жить совсем чуть-чуть… Поэтому сейчас – самое время."
    show mi smile pioneer close at center with dspr
    mi "Прости меня, если бы я не была такой эгоистичной…"
    me "Нет, это ты меня прости…"
    "Кажется Сёма плачет."
    me "Знаешь, я всегда тебя любил…"
    mi "Я знаю…"
    "Тихо сказала подруга и тоже заплакала."
    show mi cry pioneer close at center with dspr
    "Мику вновь улыбнулась, её лицо задрожало, и по нему потекли слёзы."
    me "И сейчас люблю…"
    mi "Я знаю…"
    th "Любит?! Знает?! Да что творится?! Сначала Сёма со Славей ворковал, затем за Алисой подглядывал. Теперь оказывается Мику любил, и она знает, и сама с ним воркует, в то же время уверяла меня ранее, что любит Сашу. Да что здесь твориться?!"
    "Если бы не усталость я бы поднялась на ноги и влепила ему такую увесистую оплеуху, что он до конца жизни перестал бы вешать лапшу девочкам. Но меня хватило лишь на то, чтобы повернуть голову и увидеть, как они целуются в слезах."
    "Несмотря на моральную и физическую опустошённость в груди больно кольнуло, и я отвернулась."
    th "Сёма… Сёма… а я ведь тебя любила и сейчас люблю. За что ты со мной так?"
    "Я уставилась в небо полностью потеряв связь с миром."
    window hide
    hide mi
    hide pi
    with fade
    window show
    me "Вставай!"
    th "Что кто здесь?"
    "Ай."   
    "Кто-то влепил мне несколько пощёчин."
    me "Вставай! Вставай!"
    "Семён поднял меня на ноги."
    me "Бежим!"
    "Он снова схватил нас за руки и бросился вперёд."
    window hide
    scene bg ext_path2_night with dissolve:
        pos (0,0)
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (5,5)
        pos (0,0)
        linear 0.1 pos (0,-5)
        linear 0.1 pos (0,5)
        repeat
    window show
    "Мы снова бежали, падали, вставали, продирались сквозь чащу."
    "Вдалеке показался просвет."
    window hide
    play ambience ambience_old_camp_outside fadeout 1 fadein 2
    scene bg ext_old_building_night with dissolve
    window show
    "Вскоре мы выбежали на небольшую полянку, со всех сторон окружённую деревьями, на которой стояло здание, больше напоминающее детский сад."
    show pi normal aonl_pioneer with dissolve
    me "Что это?"
    "Пробормотал Сёма."
    un "Старый корпус лагеря…"
    "Еле слышно сказала я."
    "Он что забыл, как мы вместе искали Шурика."
    "Сёма сделал несколько неуверенных шагов по направлению к зданию, как вдруг сзади послышался шорох, и он застыл на месте."
    play sound_loop sfx_hell_crickets_3 fadein 5
    "Шорох становился всё громче, и вдруг послышалось дьявольское стрекотание."
    window hide
    scene cg epilogue_mi_5 with dissolve
    play music music_list["scarytale"]
    window show
    "Мы повернулись и..."
    "Сзади стояла толпа…{w} Толпа маленьких девочек."
    "Точнее, толпа Ульян…"
    "Все они изувечены, как описывал Сёма утром – с оторванным лицом и ужасной искривлённой улыбкой."
    "И все они издавали эти адские звуки – стрекотание кузнечиков, дьявольское, от которого душа уходила в пятки."
    "Я замерла на месте, не веря глазам."
    window hide
    scene cg epilogue_mi_6 with dissolve
    window show
    "Вдруг из толпы вышла одна из «Ульян» и достала из-за спины…{w} оторванную голову Серёжи."
    "На лице юноши застыла предсмертная гримаса ужаса."
    us "Привет, Семён! Как твои дела?"
    "Проскрежетало существо."
    "Сёма словно очнулся от её голоса, громко заорал от ужаса и потянул нас за собой."
    "Я так и не могла оторвать взгляд от этих чудишь."
    window hide
    scene bg ext_old_building_night with dissolve
    stop sound_loop fadeout 2
    pause 1
    stop ambience fadeout 2
    scene bg int_old_building_night with dissolve
    window show
    "Вдруг почва ушла у нас из под ног и меня потащило вниз."
    window hide
    play music music_list["sunny_day"] fadeout 1 fadein 3
    scene bg black with fade
    play ambience ambience_catacombs fadein 3
    window show
    "Вокруг кромешная темнота. Я словно провалилась в омут тьмы и никого нет рядом."
    me "Маша… Лена…"
    "Послышался голос рядом."
    mi "Мы ещё живы?.."
    me "Похоже на то…"
    "Послышалось копошение."
    window hide
    scene bg int_catacombs_entrance
    with dissolve
    window show
    "Порывшись в карманах я достала фонарик."
    show mi scared pioneer at cright
    show pi upset aonl_pioneer at cleft
    with dissolve
    me "Где ты его взяла?.."
    "Я подошла к ним хромая. Нога очень сильно болела."
    un "Ещё вчера… На всякий случай…"
    "Он взял фонарь и посветил по сторонам."
    "Мы находились в том же бомбоубежище, что и пару дней назад."
    show mi sad pioneer with dspr
    mi "Где это мы?"
    me "Не знаю… Похоже на бомбоубежище какое-то…"
    th "В смысле не знает? Мы же пару дней назад вместе искали тут Шурика!"
    "Сёма посмотрел на дыру в потолке." 
    "Забраться наверх нет никакой возможности, но и монстров не слышно."
    "Наверное, от старости пол лагеря прогнил, и мы провалились сюда."
    me "А что там дальше?"
    mi "Не знаю… Но придётся проверить."
    "Сёма двинулся вперёд, я последовала за ним."
    un "Ай…"
    me "Что такое?"
    un "Кажется, ногу подвернула…"
    me "Ладно, обопрись о меня."
    "Он подошёл ко мне и подставил плечо."
    window hide
    scene bg int_mine
    show mi scared pioneer at cright
    show pi normal aonl_pioneer at cleft
    with dissolve
    window show
    "Вскоре каменные стены сменились деревянными, и мы оказались шахте как и было ранее."
    show mi sad pioneer at cright with dspr
    mi "Давайте немного передохнём!"
    "Взмолилась Мику."
    "Сёма аккуратно опустил меня на землю и сел рядом."
    me "Ну, хотя бы этих чудищь больше не видно…"
    mi "Надолго ли…"
    mi "Как думаешь, что здесь происходит?"
    "Голос Мику дрожал, но всё равно звучал более-менее уверенно."
    "Похоже, она была измотана и опустошена настолько, что уже не оставалось сил на страх."
    me "Не знаю…" 
    me "И, если честно, знать не хочу!"
    mi "Но мы же… выберемся?"
    me "Обязательно!"
    "Я закрыла глаза полностью отключившись."
    stop music fadeout 3
    window hide
    #скример
    scene bg int_mine with flash
    window show
    "Открыв глаза, не увидела ни Мику ни Семёна"
    th "Куда они делись? Я, что, теперь одна?!"
    "От страха даже не сразу заметила, что иду по шахте с факелом и тесаком в руке."
    "Попыталась остановиться, но ничего не вышло. Тело двигалось само!"
    play music music_list ["scarytale"] fadein 3
    aonl_dark_un "Проснулась наконец."
    "Сорвалось мерзкое шипение с моих губ."
    un "Ты кто?!"
    aonl_dark_un "Я это ты разве не ясно?!"
    "Существо зловеще расхохоталось."
    "Меня пробрала дрожь от безумного смеха. Будь возможность сбежала бы отсюда не оглядываясь."
    aonl_dark_un "Твоя лучшая половина, если говорить точнее. Осуществляю твои тайные желания."
    un "Какие ещё желания?"
    aonl_dark_un "Конкретно сейчас ищу этого мудака Семёна и сучку Мику, чтобы пустить их на фарш."
    "Существо подняло тесак к лицу и облизала лезвие."
    un "Зачем, что они тебе сделали?"
    aonl_dark_un "Мне?"
    "Удивлённо произнесло существо."
    aonl_dark_un "Нам дурочка, нам. Эти твари вытерли о нас ноги, крутя любовь за нашей спиной. А мы ведь любим этого гандона, верили подружке Мику. Ну ничего, потерпи скоро они получат своё."
    un "Что?! Остановись, я не хочу!"
    aonl_dark_un "Хочешь, просто не признаёшься себе, да и смелости бы не хватило, уничтожить то что причиняет боль."
    me "Маша! Маша!"
    "Послышался крик впереди."
    aonl_dark_un "А вот и сволочь!"
    "Существо побежало на голос."
    un "Нет остановись прекрати!"
    window hide
    scene bg int_mine
    with fade
    window show
    aonl_dark_un "Что, Семён, заблудился?"
    window hide
    scene cg epilogue_mi_7
    with dissolve
    window show
    "Вскоре перед нами появился напуганный Семён."
    aonl_dark_un "А я вот за тобой пришла!"
    aonl_dark_un "А я за тобой!"
    me "Ты… Ты… кто ты?.."
    "Выдавил он из себя."
    aonl_dark_un "Лена! Разве не узнаёшь?"
    "Она залилась дьявольским смехом."
    un "Сёма беги не стой."
    aonl_dark_un "Пока шашни крутил с ними, уже и забыл обо мне?"
    me "Я… Я…"
    aonl_dark_un "Ничего! Теперь уже никого нет! Остались мы вдвоём!"
    me "Значит, это ты… Ты всё?.."
    aonl_dark_un "Бинго! Ну, не всё, конечно…"
    aonl_dark_un "Сначала Славю! Она меня всегда раздражала! Мисс Непогрешимость прямо! Прилежная, старательная, всегда везде и за всех! Тьфу! А как она кричала, когда я отрывала ей руки, а? Жалко ты не видел!"
    "Её рот затрясся, и из него потекла слюна, а глаза закатились."
    aonl_dark_un "А потом Алиса… «Меня все бесят, мне никто не нужен»! Теперь вот одна спокойно висит на дереве! Правда, поднимать её туда было непросто, но для большего эффекта-то! Как вы визжали-то, а? Как свиньи на бойне!"
    aonl_dark_un "Ничего, осталось только с этой сучкой Мику разобраться – и тогда всё!"
    window hide
    scene cg epilogue_mi_8 with dissolve
    window show
    "Она достала из-за спины огромный тесак, измазанный кровью."
    aonl_dark_un "Ну, правда…"
    "Она ненадолго прервалась."
    aonl_dark_un "Я не знаю, что это за хрень была в образе Ульянки… Да и остальных пионеров не я… Но разве это сейчас важно?"
    window hide
    scene bg black with fade
    window show
    "Она махнула факелом, и он погас в ту же секунду."
    window hide
    scene bg aonl_int_mine_red with dissolve
    window show
    "Эта тварь видела в инфракрасном цвете!"
    aonl_dark_un "Подожди здесь, я быстро!"
    "Существо опять мерзки рассмеялось."
    un "Нет остановись!"
    "Я пыталась ей помешать, но тело не слушалось."
    aonl_dark_un "Расслабься, скоро тебе станет легче."
    un "Нет, не станет! Они меня обидели, но я не желала им смерти, наоборот, стало больнее! Убийства не приносят облегчения!"
    aonl_dark_un "А мне наоборот в кайф, так что заткнись!"
    "Я металась внутри тела чудовища, но всё было бесполезно."
    window hide
    scene bg int_mine with fade
    play sound sfx_match_candle
    pause 1
    scene bg int_mine_room with fade
    pause 1
    scene bg black
    with fade
    window show
    "Вскоре чудовище вбежало внутрь бойлерной, где спала Мику."
    "Тварь занесла тесак над девушкой."
    un "Нет, только не Мику, НЕЕЕЕЕЕЕЕЕЕЕЕТ!"
    "На мгновение комната осветилась, и мы увидели вбежавшего Семёна с гаснувшей спичкой."
    "Найдя в себе последние силы, я смогла парализовать мышцы твари."
    window hide
    #scene bg Красный фон
    window show
    "Свет погас и Сёма, бросившись на нас, повалил тварь на землю и начал молотить чудовище кулаками по морде."
    aonl_dark_un "Отпусти он же нас убьёт!"
    un "Ну и пусть!"
    "Я из последних сил удерживала монстра, чувствуя, как кулаки Семёна превращают морду твари в кровавое месиво."
    "Наконец, после очередного удара кулака мышцы руки, держащие тесак, дрогнули расслабившись и я потеряла сознание."
    stop music fadeout 3
    window hide
    scene bg int_mine_room
    show mi scared pioneer at left
    show pi angry aonl_pioneer
    with fade
    play sound sfx_ignite_torch
    window show
    "Голос Мику вырвал меня из забытья."
    mi "Не надо…"
    show pi surprise aonl_pioneer with dspr
    me "Но нельзя же…"
    "Возразил Семён."
    mi "Не надо…"
    hide mi 
    hide pi 
    with dissolve
    "После непродолжительного молчания Семён куда-то отошёл и начал скрежетать металлом."
    "Вскоре послышался скрип открывания металлической двери."
    "Через некоторое время шаги ребят стихли вдалеке, и я осталась одна." 
    "Из носа и челюсти текла кровь, один глаз сильно заплыл и не открывался, голова раскалывалась, но теперь в моей душе поселился покой."
    "Меня простили..." 
    "Несмотря на всё совершённое ранее, пусть это была и не совсем я..." 
    "Всё равно чувствовала себя частично виноватой."
    "Из уцелевшего глаза скользнула слеза."
    th "Славя, Алиса простите меня!" 
    th "Я не хотела, мне было очень больно, но вы не заслужили такой судьбы..." 
    th "Надеюсь, Мику и Семён спасутся и у них всё будет хорошо." 
    th "Будьте счастливы, а я останусь здесь, чтобы никогда и никому не причинить вреда..."
    window hide
    scene bg black with dissolve2
    pause 4
    # jump 
    
    #Фон полёт через облака и звёзды и фон домик лены внутри в конце
    window show
    play music aonl_over_the_sky fadein 2
    "Глаз закрылся, и я вдруг ощутила, как моё тело поднялось над землёй..."
    show bg aonl_sky with fade2
    "Меня словно подняло в воздух и швырнуло через облака." 
    scene stars with fade2
    "Я снова пролетела через звёзды и планеты..."
    scene bg black with dissolve2   
    "А потом упала в свой домик."
    
    window hide
    jump aonl_day6_alt
    