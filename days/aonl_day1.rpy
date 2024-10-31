label aonl_day1:
    $ aonl_chapter(1)
    $ persistent.aonl_day1 = True
    $ day_time()
    $ persistent.sprite_time = "day"
    
    play music music_list["no_tresspassing"]
    play ambience ambience_int_cabin_day fadein 2
    scene bg int_house_of_un_day with flash
    window show
    th "Где я?..{w} Что это за место?..{w} Ведь вчера ещё была зима, почему же здесь так тепло и солнечно?{w} Может быть, я просто сплю?"
    "Чтобы проверить, реальность это или сновидения, я как можно сильнее ущипнула себя за ногу.{w} Не заставившая себя ждать боль намекнула на реальность происходящего."
    th "Но как такое могло произойти?"
    "Я всегда была реалисткой, поэтому скептически относилась к болтовне о путешествиях во времени."
    "Но то, что я невероятным образом, ещё недавно находясь в своей квартире, окутанной теплом от батарей отопления и дуновением метели за окном, вдруг пришла в себя в небольшом летнем домике посреди цветущей лесной природы, грозило сломать мой скептицизм."
    window hide
    with fade2
    
    window show
    "Не знаю, как долго я продолжала бы размышлять о происходящем, если бы из раздумий меня не вывел звонкий голос девочки."
    show mi normal pioneer at center with dissolve
    aonl_mi "Доброе утро, Лен. Как спалось? Мне вот не очень: приснился сон, будто я выступала на сцене, как вдруг погас свет. Нет, ты представляешь, да? Я так старалась, а меня прервали…"
    "Безостановочно говорила девочка."
    "Похоже, её рассказ мог затянуться надолго, посему я перебила её вполне резонным вопросом:"
    show mi scared pioneer at center with dspr
    un "Кто ты такая?"
    "Спросила я сонным голосом."
    show mi surprise pioneer at center with dspr
    "Девушка с длинными бирюзовыми волосами сперва недоуменно посмотрела на меня, затем, вскочив из постели, принялась осматривать меня, трогать лоб, проверяя температуру."
    aonl_mi "С тобой всё в порядке? Я Мику, мы живём в одном домике уже три недели."
    mi "Почему ты смотришь на меня так, будто впервые видишь? Может, ты заболела? Давай я отведу тебя к врачу. Ох, не люблю я этих врачей с детства…"
    "Затараторила Мику."
    "И снова бесконечный поток её мыслей пришлось прервать."
    un "Послушай, я тебя впервые вижу и не намерена играть в эти игры, так что лучше оставь меня в покое!"
    un "Я должна найти выход отсюда, это не то место, где я живу на самом деле."
    "Стараясь сохранять спокойствие в тоне, сказала я."
    "Надев лежавшую рядом на полке спортивную одежду, я направилась к выходу из домика."
    window hide
    stop ambience fadeout 2
    play sound sfx_close_door_campus_1
    
    scene bg ext_house_of_un_day with dissolve
    play ambience ambience_camp_center_day fadein 2
    window show
    "Мику ещё что-то кричала мне вслед, но закрывшаяся дверь оборвала звук её голоса."
    th "И откуда она меня знает, о каких трёх неделях говорит?"
    th "Всё это выглядело так, словно я попала в параллельный привычному мир и заняла место одного из его обитателей."
    th "Но стоп — она же назвала меня по имени!{w} Может быть, это какой-то научный эксперимент по внедрению в мозг воспоминаний, как в старом фильме «Вспомнить всё»? Но тогда почему я помню всю свою привычную жизнь до мелочей?"
    th "А может, я жертва научного эксперимента и сейчас лежу в стазисе, подключённая к приборам, создающим в голове подопытного выдуманную реальность?"
    th "Так много версий происходящего, но какой смысл гадать? Ведь простыми домыслами я не смогу приблизиться к разгадке!" 
    th "Пожалуй, нужно осмотреться здесь и постараться избегать встреч с этими подростками и вообще с кем-либо.{w} Что же, этот вариант вполне подходит."
    window hide
    stop music fadeout 3

    scene bg ext_houses_day with dissolve
    window show
    "Я решила пойти прямо, минуя домики, но едва я прошла мимо некоторых, впереди увидела двух девочек."
    play music music_list["that_s_our_madhouse"] fadein 3
    show dv smile pioneer2 at cleft
    show us smile sport at cright
    with dissolve
    "Одна из них была одета в пионерскую форму, но сидела она на ней, мягко говоря, вызывающе и неправильно, а другая была в красной майке с надписью «СССР»: они оживлённо спорили о чём-то."
    th "Видимо, это был пионерский лагерь, но ведь я живу в 21 веке, пионерлагеря остались в прошлом!"
    "Теория путешествия во времени приобретала доказательства."
    "Разговаривать с ними у меня не было никакого желания. Я вообще редко общалась с людьми и в настоящем, предпочитая одиночество компаниям, поэтому решила просто пройти мимо."
    hide dv
    hide us
    with dissolve
    "Когда они уже были позади, одна из них окликнула меня."
    dvp "А ну стоять!"
    "С надменной интонацией произнесла девочка."
    "От неожиданности я замерла и несмело повернулась к позвавшей меня."
    show dv angry pioneer2 at cleft
    show us smile sport at cright
    with dissolve
    un "Что такое?"
    "Тихо спросила я."
    "Голос принадлежал рыжей девочке."
    th "Что ж, ничего удивительного!{w} В её взгляде читается высокомерие, и оно вполне соответствовует тому, как она начинает разговор с другими."
    th "Да и сомневаюсь, что это могла бы быть стоявшая рядом с ней маленькая красноволосая девочка."
    dvp "Ты чего такая дёрганая, Тихонова? Боишься меня, что ли?"
    "Спросила рыжая."
    show us grin sport at cright with dspr
    usp "А может, она влюбилась?{w} Посмотри, Алиса, витает вся себе в облаках!"
    "Весело закричала другая девочка."
    "От такого неуважительного отношения я начала впадать в ярость."
    th "Мало того, что они, похоже, все тут знали меня, хотя я не знаю никого, так ещё и при встрече одна мнит из себя не пойми кого, другая шутит так, будто ещё только вчера из детского сада сбежала."
    "Не выдержав, я закричала на них:"
    un "НЕ ВАШЕ " with vpunch
    extend "СОБАЧЬЕ " with vpunch
    extend "ДЕЛО!" with vpunch
    extend " Отстаньте от меня! Вы все здесь ненастоящие, так что не стойте у меня на пути! Я выберусь отсюда, а вам счастливо оставаться!"
    show dv surprise pioneer2 at cleft
    show us surp2 sport at cright
    with dspr
    "Похоже, они явно не ждали такой реакции, поэтому остались стоять неподвижно, открыв широко рты и глядя мне вслед."
    window hide
    stop music fadeout 3
    
    scene bg ext_houses_day with fade2
    window show
    "Как будто надоедливых наглых пионерок оказалось мало!{w} Не успела я пройти и пары сотен метров, как меня позвала молодая женщина лет двадцати пяти."
    show mt angry panama pioneer at center with dissolve
    aonl_mt "Пионер не должен без дела слоняться по лагерю!{w} Раз у тебя уйма свободного времени, как я погляжу, сходи-ка к Виоле. Ей пригодится помощница."
    "Командным голосом сказала женщина."
    "Не поняв, что она хочет от меня, я переспросила."
    un "Кто такая Виола?"
    show mt surprise panama pioneer at center with dspr
    "Женщина удивлённо посмотрела на меня, а затем нахмурив брови, строго сказала:"
    show mt angry panama pioneer at center with dspr
    aonl_mt "Не пытайся отлынивать от пионерских обязанностей! Пойди в медпункт и помоги медсестре."
    un "Нет! Я не буду играть по вашим правилам! Оставьте меня в покое! Мне не место здесь!"
    "В панике закричала я, бросившись бежать куда глаза глядят."
    th "Куда угодно, но лишь бы подальше от этого места!"
    window hide
    stop ambience fadeout 2
    
    scene bg black with fade2
    pause 1
    play ambience ambience_forest_day fadein 2
    window show
    play sound sfx_bush_body_fall
    "Бежала я до тех пор, пока не добралась до леса, где, случайно зацепившись за торчащий из земли корень, упала, потеряв сознание от удара." with vpunch
    "В темноте я слышала двоившееся эхо:"
    voice "Лена… Лен, очнись! Ты в порядке?.."
    window hide
    
    scene bg ext_polyana_day
    show sl normal pioneer at center
    play sound sfx_draw_water
    show unblink
    $ renpy.pause(1, hard=True)
    play music music_list["forest_maiden"] fadein 3
    window show
    "Окончательно я пришла в себя, когда мне в лицо полетели брызги холодной воды.{w} Открыв глаза, я увидела светловолосую девочку. Она сидела рядом на корточках, держа в руках фляжку с водой."
    slp "Наконец-то ты очнулась! Всё в порядке?"
    "Обеспокоенно спросила девочка."
    un "Что?{w} Где я?{w} Кто ты?"
    "В голове всё ещё шумело, поэтому это было всё, что я смогла спросить у неё."
    show sl surprise pioneer at center with dspr
    slp "Лен, похоже, ты всё же сильно ушиблась. Мы в пионерлагере «Совёнок», я Славя, сейчас третья неделя нашей смены, и ты здесь с самого её начала."
    "С удивлением в голосе рассказала Славя."
    un "Послушай, я не здешняя вовсе…{w} Ещё недавно была зима, а сейчас я оказалась здесь под палящим солнцем…{w} Я не понимаю, что происходит!"
    "Наверное, в этот момент я выглядела как сумасшедшая."
    show sl normal pioneer at center with dspr
    sl "Какая зима? Насколько я помню, и вчера, и позавчера, и месяц назад было лето!{w} Скажи, а в какой момент ты забыла о том, как здесь проводила время?"
    "Поинтересовалась Славя."
    un "Я проснулась в домике и…{w} не помню ни пионеров, ни этот лагерь. Помню, что сидела дома, читала книгу, а потом вдруг оказалась здесь."
    "Не знаю почему, но я чувствовала, что этой девочке можно доверять и она поймёт меня."
    sl "Кажется, тебе приснился сон. И ты, проснувшись, приняла его за настоящее."
    sl "Я могу помочь тебе. Давай я отведу тебя к нашей медсестре, она осмотрит тебя.{w} А потом я покажу тебе лагерь и заново познакомлю с другими пионерами. Они будут рады помочь тебе вспомнить."
    sl "Может, ты приняла свои сны за явь?{w} Уверена, ребята отнесутся с пониманием к тому, что ты запуталась в своих снах, ведь вместе мы все — дружный пионерский отряд! Не бросим товарища в беде, особенно когда он так нуждается в помощи!"
    show sl smile pioneer at center with dspr
    "Улыбнувшись, она подала мне руку и повела за собой в медпункт."
    un "Спасибо, что помогаешь мне."
    "Поблагодарила я Славю."
    sl "Пустяки! Я рада, что тебе стало лучше. И поскольку мы собираемся вернуть тебе забытые воспоминания о лагере, приветствую тебя в «Совёнке», Лена! Добро пожаловать в родные пенаты!"
    show sl laugh pioneer at center with dspr
    "Славя хихикнула от того официального тона в голосе, с которым она это говорила."
    window hide
    stop music fadeout 3
    stop ambience fadeout 3
    scene bg black with fade2
    
    scene anim prolog_1 with fade
    play music music_list["farewell_to_the_past_edit"] fadein 3
    $ prolog_time()
    $ set_mode_nvl()
    window show
    "Дружелюбие Слави выглядело таким естественным и приятным, что впервые с того момента, как я помню этот лагерь, мне стало так уютно и спокойно на душе, что понемногу страхи стали отступать."
    "Ведь невежливо воспринимать доброту и добровольную помощь в трудную минуту как некий злой эксперимент или мистику."
    "Наверное, виной такому моему восприятию было то, что в жизни я натерпелась достаточно зла от людей и редко встречала доброту, готовность самоотверженно помочь мне."
    "Зря я была груба с остальными! Мику ведь не желала мне ничего плохого и переживала за моё здоровье."
    "А у той рыжей девочки наверняка характер такой сам по себе. Мы с ней просто противоположности, люди разные, и это нормально."
    "А та женщина, скорее всего, вожатая, это объясняет её приказной тон."
    "В любом случае, думаю, нет причин воспринимать здешних пионеров враждебно. А если и стоит, то только тогда, когда они и правда сделают мне что-либо плохое."
    "Всё же тот странный зимний мир, моя тёплая квартира были и правда всего лишь сном. Я верю: этот мир и этот лагерь и есть мой дом."
    nvl clear

    "Такое необычное чувство. Этот лагерь, все эти люди, они ведь знают меня… Наверное, сказалось моё вечное заточение в четырёх стенах, раз уж даже сон, в котором я наедине с собой осталась в квартире, показался мне куда реальнее, чем это место."
    "Здесь тепло, и лучи восходящего солнца проникают везде, куда могут достать, согревая теплом всё, что нуждается в нём после ночи."
    "Утренняя природа — один из моих любимых пейзажей как художницы. Приятно оказаться где-то вдали от шумного города с вечно спешащими по своим делам людьми. Оказаться наедине с лёгким ветерком, утренней прохладной росой и шумом леса неподалёку…"
    "Сразу же в голову приходят идеи изобразить то, что видишь на холсте."
    "Пусть даже мои работы никогда не будут достоянием общественности и вряд ли найдут своего ценителя, но всё же я смогу сделать то, что не получается воплотить при общении с людьми."
    "А именно — выразить свои чувства, вложив их в каждое прикосновение кисти к мольберту."
    "Одно лишь останется неизменным: солнце не проникнет вглубь моего сердца и не согреет его, а я так и останусь одинокой девочкой-тихоней, которая всегда держится поодаль от компаний и какого бы то ни было общества."
    "У каждого своя судьба, и у меня тоже."
    window hide
    $ set_mode_adv()
    $ day_time()
    stop music fadeout 3

    scene bg ext_path_day with fade2
    play ambience ambience_forest_day fadein 3
    show sl normal pioneer at center with dissolve
    window show
    sl "Лен? Ты меня слышишь?"
    "Голос, который прозвучал у меня в голове, прервав уход в мысли, принадлежал Славе."
    un "Да, прости, я задумалась."
    sl "Сейчас я проведу для тебя экскурсию. Думаю, так ты сможешь быстрее вспомнить, кто ты есть."
    "Славя всё так же была добра со мной."
    sl "Для начала давай вернёмся на площадь, а оттуда уже решим, что посетить сперва.{w} Ты ведь не против?"
    "Спросила Славя, внимательно смотря на меня в ожидании ответа."
    un "Нет, всё в порядке."
    window hide
    stop ambience fadeout 1
    
    scene bg ext_square_day with dissolve
    play music music_list["get_to_know_me_better"] fadein 3
    play ambience ambience_camp_center_day fadein 3
    window show
    "Подумав, Славя всё-таки решила, что лучше всего будет пойти в сторону столовой и дальше по дороге."
    window hide
    
    scene bg ext_dining_hall_away_day with dissolve
    window show
    "Столовая находилась недалеко от площади. Это было невысокое одноэтажное здание, из окон которого доносился приятный запах готовящейся пищи."
    "Что это такое и с чем его едят, Славя объяснять не стала, верно решив, что и так можно понять."
    window hide
    
    scene bg ext_playground_day with dissolve
    window show
    "Последовав дальше, мы прошли мимо склада и вышли на спортивную площадку."
    show sl normal pioneer at center with dissolve
    sl "Лен, ты увлекаешься каким-либо спортом? Может, в школе играла во что-либо…"
    "Поинтересовалась Славя."
    un "Мне с детства нравится бадминтон."
    show sl smile pioneer at center with dspr
    sl "Я не удивлена. Судя по твоей фигуре, можно было сделать вывод, что ты занимаешься спортом.{w} Странно, что я не видела тебя за игрой в бадминтон раньше, но думаю, сейчас у тебя будет возможность наверстать упущенное."
    "Добродушно улыбаясь, говорила Славя."
    "Мне была приятна мысль о том, что я смогу уделять время любимой игре."
    un "Спасибо тебе. Ты так помогаешь мне…"
    "Поблагодарила я девочку."
    sl "Я рада помогать, ведь все мы здесь друзья, а за тобой я буду присматривать, чтобы не случилось снова ничего плохого, ты ведь не против?"
    un "Нет."
    "Робко ответила я."
    show sl normal pioneer at center with dspr
    sl "Вот и ладненько. А если кто-то маленький рыжеволосый и с хвостиками по бокам захочет поиздеваться и подтрунивать над тобой, скажи мне, я разберусь."
    "Серьёзно сказала Славя."
    un "К-конечно, но… не будет ли это неправильно — жаловаться?"
    sl "Я же хорошо знаю тебя: ты тихая и скромная, а над такими любят слегка поиздеваться бойкие девочки вроде Ульяны. Так что в том, что я отгорожу тебя от напрасных переживаний, нет ничего плохого."
    sl "Пусть над детишками из других отрядов подшучивает, они вместе неплохо спелись за эту смену."
    un "Надеюсь, всё будет хорошо."
    sl "Пока я присматриваю за тобой, ничего не случится."
    stop music fadeout 2
    play sound sfx_dinner_jingle_normal
    "Едва она успела договорить, как по территории лагеря пронёсся звук горна, зовущего, как мне объяснила Славя, на завтрак."
    window hide
    stop sound fadeout 1
    
    scene bg ext_dining_hall_near_day with dissolve
    window show
    "Мы шли вместе к столовой, минуя разрозненных в небольшие кучки пионеров, так же спешащих поскорее покушать. Хотя кто их знает: быть может, они просто торопились занять лучшие места."
    window hide
    stop ambience fadeout 1
    
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 2
    $ set_mode_nvl()
    window show
    "Взяв еду и сев за свободные места, мы приступили к трапезе."
    "При взгляде на всю эту шумную, звякающую ложками детвору, в моей памяти вдруг вырисовались воспоминания о школьных обедах."
    "Всё почти как здесь. Так же дети и подростки спешили после звонка в столовую, радуясь тому, что тихие посиделки за партой под аккомпанемент голоса учителя, дающего детишкам новую порцию знаний, а их товарищам постарше — ещё и билет в будущее, закончились и можно расслабиться."
    "Ведь только от успехов в экзаменах зависело то, будет ли ребёнок новым светилом науки или останется прозябать жизнь, работая на заводах во благо Родины, но не зная, что такое счастливая жизнь в полном достатке."
    "Ну, а кому-то было суждено потерять всё и упасть вниз по карьерной лестнице… На самое дно, где только грязь, страх, мрак и ничего человеческого. Только злоба, боль и страдания."
    nvl clear
    "Мне всегда было интересно, какова же судьба будет у тех, кому она благоволила в школьные годы."
    "Они всегда были в центре внимания, сливки школьного общества. Кто-то даже начинал упиваться этим и ради поддержания авторитета издевался над тихими ребятами, которые проигрывали ему по каким либо показателям, зачастую физическим."
    "Так могло быть, и было какое-то время со мной. В начальных классах меня либо обходили стороной и практически не общались, либо всячески пытались задеть или обидеть."
    "Наверное, так могло бы быть и до конца школы."
    nvl clear
    "Но один случай изменил мою дальнейшую жизнь в школе."
    "В старших классах у меня была настоящая любовь, которая обернулась очень плачевным исходом. После серьёзной ссоры он явно хотел мне сделать ещё больнее, с силой схватив меня за руку, когда я хотела просто убежать домой и попытаться успокоиться."
    "К сожалению, в тот момент мы были на лестнице, и, не осознав это, я постаралась изо всех сил освободить руку, после чего он споткнулся и съехал вниз по ступенькам, получив при этом сотрясение мозга."
    "В итоге всё было обставлено так, что я оказалась виноватой и якобы намеренно столкнула его. Его родители, как оказалось, были в хороших отношениях с директором нашей школы, и благодаря этому из меня сделали изгоя. Девочку, которая пыталась убить своего парня, психанув из-за обид на него."
    nvl clear
    "Никому не было дела до того, что случилось на самом деле. Чтобы официально поставить на мне клеймо ненормальной, меня затаскали по всем кругам ада: месячное разбирательство с постоянным хождением по разным кабинетам и объяснениями, как так получилось, принудительные походы к психологу, который, видимо, был назначен лишь для того, чтобы поставить диагноз, который хотели видеть руководители школы, дабы избавиться от такой проблемной девочки, которая чуть не убила человека."
    "А я просто совсем замкнулась в себе. И когда меня перевели в другую школу, слухи о произошедшем дошли и до туда, и все меня старались обходить стороной. Боялись, что я снова сорвусь и кому-то не поздоровится, хотя я и не хотела никому из них причинять вреда."
    "Наоборот — хотелось быть свободной в общении, почувствовать себя не птицей, запертой в клетке, а человеком. Но увы, я так и осталась в образе тихой девочки-динамита, которую лучше игнорировать…"
    window hide
    stop ambience fadeout 2
    $ set_mode_adv()
    
    scene bg int_dining_hall_day with dissolve2
    play ambience ambience_dining_hall_empty fadein 2
    window show
    dvp "Ну, так и будешь тут сидеть?{w} Завтрак уже закончился."
    "Я совсем не заметила, как столовая опустела, а я осталась лишь наедине со своими мыслями. Если бы не высокая рыжая девочка, которую я уже видела раньше в компании Ульяны."
    show dv normal pioneer at center with dissolve
    un "Ой, я задумалась…"
    "Тихо ответила я."
    show dv grin pioneer at center with dspr
    dvp "Странная ты! Сначала кричишь на меня, что я ненастоящая, потом пол-лагеря на уши поднимаешь своим исчезновением, а сейчас будто под гипнозом сидишь."
    "Усмехнулась девочка."
    un "Прости, что накричала, но я правда не помню никого здесь."
    "С грустью сказала я."
    show dv smile pioneer at center with dspr
    dv "Ничего, проехали, с кем не бывает. На свежем воздухе и не такое может произойти!{w} Меня Алиса зовут, будем знакомы снова, Лена."
    "Как-то странно улыбнулась Алиса."
    un "Очень приятно. Ну, я пойду, наверное."
    dv "Иди."
    "Коротко ответила она, тут же расфокусировав с меня своё внимание."
    "Похоже, на этом разговор был окончен.{w} Не знаю почему, но мне показалось, что я знаю Алису, причём знаю довольно давно, будто мы знакомы с детства."
    "Что-то в ней чувствовалось близкое мне."
    th "Кто знает, ведь, быть может, когда-то мы были подругами, и то, что я сейчас ощутила, вполне возможно, не что иное, как обрывок воспоминаний."
    th "Зря я была груба с ней — она ведь даже не стала обвинять меня в моём срыве около домиков.{w} Ладно, как она сама и сказала, проехали."
    window hide
    stop ambience fadeout 2
    
    scene bg ext_square_day with dissolve
    play ambience ambience_camp_center_day fadein 2
    window show
    "Выйдя из столовой, я не заметила ни одного пионера поблизости."
    th "Наверняка сейчас все разбрелись по делам, розданным им вожатой, и как муравьи дружно бегали по лагерю, выполняя поручения."
    "Не было рядом и Слави, несмотря на то, что она собиралась познакомить меня с лагерем."
    th "Не думаю, что такая, как она, могла просто так забыть обо всём; скорее всего, и ей досталось задание от вожатой."
    window hide
    
    with fade2
    window show
    "Как это обычно бывает, едва подумаешь о ком-то, он появляется, особенно это касается руководителей."
    "И вот вестница порядка и прилежности уже стояла рядом, строгим взглядом смотря на меня."
    show mt normal panama pioneer at center with dissolve
    mtp "Здравствуй, Лена. Тебе стало получше? Ох уж ты и напугала нас с утра!"
    "В силе этого закона подлости я успела убедиться ещё в школе на примере моих одноклассников."
    "Как это часто было, только они задумывали устроить очередное себе приключение и уже приступали к исполнению своей идеи, как появлялась учительница и с треском обрушивала их планы. Ну, а если они уже начали бедокурить, ещё и раздавала нагоняй незадачливым хулиганам."
    un "Простите, я не помню, как вас?.."
    show mt smile panama pioneer at center with dspr
    "Она хихикнула, сменив строгий взгляд на тот, каким обычно смотрит мать на дитя."
    mtp "Зови меня Ольга Дмитриевна."
    un "Хорошо, спасибо, что понимаете меня и не наказали за это."
    "Я не была уверена, как вести себя в этой ситуации, потому решила следовать своему «золотому» правилу — не снимать маску неуверенной скромницы."
    mt "Наказать?{w} За что тебя наказывать?{w} Хорошо, что у тебя все налаживается. Я думала дать тебе поручение в библиотеке, но из-за этого инцидента у тебя сегодня будет выходной."
    mt "Весь оставшийся день можешь заниматься тем, чем пожелаешь, отдыхай. Но смотри: завтра всё будет, как и прежде."
    "Всё также улыбаясь, сказала Ольга Дмитриевна."
    th "Как и прежде…{w} Хотелось бы мне знать, как здесь было прежде.{w} Интересно, как много я всего пропустила? Было ли что-то такое, о чём я помнила бы всю жизнь?"
    th "Или же и в этом лагере не произойдёт ничего такого, что повернёт мою жизнь в новое, более позитивное русло?{w} Говорят, что надежда умирает последней. А рождалась ли моя вообще когда-либо?"
    window hide
    stop ambience fadeout 1
    
    scene bg ext_beach_day with dissolve
    play music aonl_mus_samidare fadein 3
    play ambience ambience_lake_shore_day fadein 2
    window show
    "Из примечательных мест этого лагеря, которые мне уже довелось увидеть, моё внимание привлёк пляж."
    th "Думаю, это место мне вполне подойдёт."
    "Минимум внимания от окружающих и максимум умиротворения — то, к чему я постоянно стремлюсь."
    "Так я большую часть времени дома проводила, читая книги.{w} Я люблю читать: это для меня возможность окунуться в другой мир, придуманный писателем, где всё живёт по законам мысли писавшего и беспрекословно подчиняется ей."
    "Художник выражает свои чувства и мысли, изображая их на холсте, используя яркие краски там, где нужно подчеркнуть светлые эмоции или красоту жизни, а тёмные — там, где нужно создать атмосферу упадка, печали, тоски и просто выразить негативные эмоции."
    "Писатель же свои чувства передаёт нам глубоко в сознание, создавая в воображении утончённые образы его героев и мира, каждым словом подчёркивая их особенности."
    "Говорят, что лучший художник — тот, чьи образы оживают в картинах, когда ими любуешься, а хороший писатель — тот, кто сумеет полностью погрузить читателя в мир его фантазии."
    "Несколько лет назад я пыталась писать свои рассказы и стихи, но выходило скверно. Всегда чего-то не хватало, да и, видимо, это не было моим призванием."
    "Потому я и решила попробовать себя в качестве художницы. Надо признать, переносить образы из воображения на холст выходило куда лучше."
    "Хотя людей мне удавалось рисовать хуже; наш наставник в художественной школе говорил, что это от недостатка чувств, и что у меня начнёт получаться тогда, когда я полюблю другого человека искренне."
    "Но сейчас больше всего я любила изображать природу."
    "И сидя здесь, глядя на смиренное покачивание волн от лёгкого ветерка, маленькие клочки земли посреди озера, обширный пляж, на котором песчинки игриво поблёскивали, ловя собою солнечные лучи, я решила, что, пока буду здесь, должна нарисовать это место."
    "Этот образ я хочу запомнить на всю жизнь."
    window hide
    
    play music music_list["so_good_to_be_careless"] fadeout 2 fadein 3
    with fade2
    show mi normal swim at center with dissolve
    window show
    mip "Красиво здесь, правда?"
    "Я не заметила, как рядом со мной села девушка с аквамариновыми волосами."
    un "Согласна, очень живописное и приятное место."
    "Ответила ей я."
    show mi smile swim at center with dspr
    mip "Прости, что напугала тебя сегодня утром. Славя рассказала, что с тобой случилось. Меня Мику зовут. Да-да, это правда."
    mi "Честно-честно! Многие не верят, но это так. У меня мать из Японии, а отец — русский инженер. Мы сюда не так давно приехали, и меня вот взяли в этот лагерь…"
    "Мику говорила так быстро, как будто я мишень, а она пулемёт «Максим», и она собирается просто расстрелять меня словами."
    un "Да, я поняла. И ты меня прости. Надеюсь, мы поладим с тобой."
    "Ответила я, пытаясь словами отыскать у Мику предохранитель и остановить стрельбу."
    mi "Конечно, я рада снова подружиться. Нас наверняка поселили вместе потому, что мы дополняем друг друга: ты — молчаливая, а я — болтушка."
    show mi shy swim at center with dspr
    "Мику слегка покраснела."
    un "Да, не могу поспорить: у тебя любопытный стиль речи.{w} Но всё же — не могла бы ты немного снижать скорость? Я не всегда успеваю следить за смыслом всего того, что ты говоришь."
    show mi laugh swim at center with dspr
    mi "Ах, видимо, я снова не уследила и запутала тебя."
    "Рассмеялась Мику."
    show mi normal swim at center with dspr
    mi "Ладно, не буду тебе мешать, до скорого, надеюсь, у тебя всё будет хорошо. А, да, ты, кстати, музыкой не увлекаешься?  Мы могли бы вместе играть в моем клубе!"
    "Заинтересовалась Мику."
    "Музыку слушать я любила, чего нельзя было сказать об её исполнении лично."
    un "Прости, но моё призвание — это краски, кисть и холст."
    stop music fadeout 1
    play sound aonl_sfx_stahp
    show mi smile swim at center with dspr
    mi "Так ты маляр? А мой папа тоже маляр. То есть он не маляр, конечно, а просто красил. Он же инженер в Японии, я тебе не рассказывала?"
    "Заулыбалась Мику."
    un "Э-э-э-м-м-м…"
    "Такого от неё я не ожидала, поэтому несколько секунд я просто смотрела на неё, находясь в лёгком недоумении."
    un "Я художница, Мику."
    "Всё ещё находясь в состоянии, будто мне на голову упал кот, сказала я."
    play music music_list["so_good_to_be_careless"] fadein 3
    show mi shy swim at center with dspr
    mi "Прости-прости! Вот я глупая, опять всё напутала! Ай-яй-яй, какая досада!"
    "Покраснев, затараторила Мику."
    show mi smile swim at center with dspr
    mi "Ой, я же совсем забыла! Мне Славя велела поискать тебя на пляже и принести полотенце! Если ты вдруг захочешь тут посидеть подольше, возьми его, а то простудишься!"
    hide mi with dissolve
    "Она отдала мне его и, ещё раз мило улыбнувшись, направилась по своим делам."
    stop music fadeout 3
    th "Не знаю, как я должна реагировать на то, что обо мне здесь все так заботятся. С одной стороны, приятно, что я кому-то не безразлична, но всё же я не маленькая, чтобы за мной все бегали…"
    window hide
    stop ambience fadeout 2
    
    scene bg black with fade2
    window show
    "За этими мыслями я и не заметила, как уснула."
    window hide
    
    $ prolog_time()
    $ persistent.sprite_time = "day"
    scene bg bus_stop
    show prologue_dream
    with fade
    play ambience ambience_cold_wind_loop fadein 3
    play music music_list["drown"] fadein 3
    window show
    "Мне приснился зимний город."
    show pi normal aonl_coat behind prologue_dream with dissolve
    "Маленькая безлюдная остановка, к которой подходил парень лет двадцати пяти. Его глаза я не смогла разглядеть, но его походка чем-то напоминала мою."
    "Неужели ещё один человек, сторонящийся общества, для которого выход из дома равносилен испытанию?"
    "Он встал рядом с остановкой в ожидании автобуса."
    show anim intro_9 behind prologue_dream with dissolve
    "Вскоре он приехал. Странный номер «410», почему-то мне показалось это знакомым."
    show anim intro_11 with dissolve
    "Вот двери открылись. Но салон так залит ярким светом, что это не делает возможным разглядеть, есть ли кто-то внутри."
    "Парень заходит в автобус, явно не замечая этой странности."
    "Внезапно меня охватывает необъяснимая паника и я кричу в никуда, чтобы он не садился внутрь. Но, похоже, все мои призывы растворились в пустоте и он меня не услышал."
    hide pi
    hide anim with dissolve
    "Как только он зашёл внутрь, двери закрылись и автобус уехал прочь, растворившись во мраке зимней ночи."
    stop ambience fadeout 3
    show bg black behind prologue_dream with dissolve
    "Внезапно я оказалась посреди тёмного пространства, напоминающего космос, но здесь не было ни звёзд, ни света."
    "Тишину внезапно нарушает неразборчивый шёпот, а затем посреди пустоты возникают, как титры на чёрном экране в конце фильма, огромные буквы, сложившиеся в слово:"
    window hide
    $ aonl_get_out = "{size=100}ВЫБИРАЙСЯ!{/size}"
    show aonl_credits aonl_get_out at truecenter behind prologue_dream with dissolve:
        linear 5.0 xzoom 2.0 yzoom 2.0
    $ renpy.pause (5, hard=True)
    stop music fadeout 3
    scene bg black with fade
    pause 1
    
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    scene bg ext_beach_sunset with dissolve
    play ambience ambience_lake_shore_evening fadein 2
    window show
    un "НЕ-Е-Е-Т!" with vpunch
    "Я проснулась с криком."
    "Не знаю, как долго я спала, но судя по тому, что уже вечерело, явно не несколько минут и даже не час."
    "Меня колотило от страха, было тепло, но озноб и холод сковали моё тело так, что нельзя было сделать ни одного движения. Понятия не имею, что это было во сне, но я сильно перепугалась."
    "Посидев ещё несколько минут и приводя сознание в порядок, я кое-как встала и, забрав полотенце, направилась к домикам."
    play sound sfx_dinner_jingle_normal
    "Но на полпути я услышала звук горна, зовущего на ужин. Что ж, подкрепиться после таких снов будет нелишним."
    stop ambience fadeout 1
    window hide
    
    stop sound fadeout 1
    scene bg aonl_int_dining_hall_people_sunset with dissolve
    play ambience ambience_dining_hall_full fadein 2
    window show
    "Оставив полотенце на стуле, я взяла поднос с едой и вернулась на место."
    "В столовой, как и утром, было всё так же шумно. Обед я благополучно пропустила, видимо, уснув как раз перед ним."
    "Недалеко сидели Алиса и Ульяна, которая то и дело мотала головой в разные стороны, будто задумала какую-то шалость."
    th "Вот уж чьей энергии хватило бы на то, чтобы обеспечить лагерь светом на всю смену, так это Ульянкиной."
    th "Мне уж точно никогда не стать такой же…{w} Хотя кто знает, время покажет."
    "С другой стороны столов сидели Славя и Мику. Увидев, что я смотрю на них, Славя кивнула мне и направилась в мою сторону."
    show sl normal pioneer at center with dissolve
    sl "Привет, Лен, приятного аппетита, как день прошёл?{w} Всё в порядке? Ты выглядишь бледной."
    "Обеспокоенно спросила Славя."
    un "Нет, всё хорошо, просто испугалась жука на пляже…"
    sl "Будь осторожнее. На обеде я прикрыла тебя, когда Ольга Дмитриевна спрашивала, почему ты не пришла. Я сказала, что ты отдыхаешь в домике."
    un "Спасибо ещё раз за помощь."
    sl "Не за что, но постарайся в другой раз не пропускать приём пищи, ладно?"
    un "Хорошо."
    sl "Ладно, я пойду, у меня есть ещё дела."
    un "Угу."
    "Ответила я."
    hide sl with dissolve
    "Покончив с ужином, я решила, что лучше всего сейчас будет пойти домой."
    th "Поздно уже, да и бродить по лагерю нет желания."
    window hide
    stop ambience fadeout 2
    
    $ night_time()
    $ persistent.sprite_time = "night"
    scene bg int_house_of_un_night with fade
    play music music_list["a_promise_from_distant_days"] fadein 3
    show mi normal pioneer at center with dissolve
    window show
    "В домике уже была Мику."
    th "И как она только успевает всё так быстро делать? Видимо, у неё талант всё делать со скоростью метеора."
    "Весь вечер Мику то и дело рассказывала о своих концертах в Японии, о сценическом образе и ещё много о чём."
    window hide
    show blink
    $ renpy.pause(1, hard=True)
    window show
    "Спустя какое-то время я не заметила, как под звонкий голос Мику постепенно начала засыпать. Тем самым положив конец этому необычному дню, полному приключений, так нехарактерных для моей неприметной жизни."
    "Я уснула с улыбкой, радуясь тому, что нашла место, где у меня будут друзья, где меня ценят как человека, и где я нужна.{w} Это - мой дом!"
    window hide
    stop music fadeout 3
    scene anim prolog_1 with fade2
    window show
    "Яркий лунный свет проникал в окно комнаты. Воцарившуюся тишину вокруг порой нарушали вой метели за окном и то и дело повторяющийся шёпот спящей, улыбающейся во сне девушки: «Это — мой дом…»"
    window hide
    scene bg black with fade3
    pause 3
    jump aonl_day2

