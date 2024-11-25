init 2:
    ################
    # Спрайты
    ################
    
    # Семён
    #
    # Пионерская форма, close
    
    image pi angry aonl_pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_angry.png") )

    image pi grin aonl_pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_grin.png") )

    image pi normal aonl_pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_normal.png") )

    image pi serious aonl_pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_serious.png") )

    image pi shocked aonl_pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_shocked.png") )

    image pi smile aonl_pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_smile.png") )

    image pi surprise aonl_pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_surprise.png") )

    image pi upset aonl_pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_upset.png") )

    # Рубашка, close
    
    image pi angry aonl_shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_angry.png") )

    image pi grin aonl_shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_grin.png") )

    image pi normal aonl_shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_normal.png") )

    image pi serious aonl_shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_serious.png") )

    image pi shocked aonl_shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_shocked.png") )

    image pi smile aonl_shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_smile.png") )

    image pi surprise aonl_shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_surprise.png") )

    image pi upset aonl_shirt close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_upset.png") )

    # Пальто, close
    
    image pi default aonl_coat close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_default.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_default.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_default.png") )

    image pi normal aonl_coat close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_normal.png") )

    image pi surprise aonl_coat close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_surprise.png") )

    image pi smile aonl_coat close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_smile.png") )

    # Плавки, close
    
    image pi angry aonl_swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_angry.png") )

    image pi grin aonl_swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_grin.png") )

    image pi normal aonl_swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_normal.png") )

    image pi serious aonl_swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_serious.png") )

    image pi shocked aonl_swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_shocked.png") )

    image pi smile aonl_swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_smile.png") )

    image pi surprise aonl_swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_surprise.png") )

    image pi upset aonl_swim close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), aonl_imgs + "sprites/close/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/close/pi/pi_2_upset.png") )

    # Пионерская форма, normal
    
    image pi angry aonl_pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_angry.png") )

    image pi grin aonl_pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_grin.png") )

    image pi normal aonl_pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_normal.png") )

    image pi serious aonl_pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_serious.png") )

    image pi shocked aonl_pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shocked.png") )

    image pi smile aonl_pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_smile.png") )

    image pi surprise aonl_pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_surprise.png") )

    image pi upset aonl_pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_upset.png") )

    # Пионерская форма, красные версии для шахты
    
    image pi normal aonl_pioneer red = im.MatrixColor(
    im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(1, 0.1, 0.1) )
    
    # Рубашка, normal
    
    image pi angry aonl_shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_angry.png") )

    image pi grin aonl_shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_grin.png") )

    image pi normal aonl_shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_normal.png") )

    image pi serious aonl_shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_serious.png") )

    image pi shocked aonl_shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shocked.png") )

    image pi smile aonl_shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_smile.png") )

    image pi surprise aonl_shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_surprise.png") )

    image pi upset aonl_shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_upset.png") )

    # Пальто, normal
    
    image pi default aonl_coat = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_default.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_default.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_default.png") )

    image pi normal aonl_coat = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_normal.png") )

    image pi shocked aonl_coat = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shocked.png") )

    image pi smile aonl_coat = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_smile.png") )

    image pi surprise aonl_coat = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_surprise.png") )

    # Плавки, normal
    
    image pi angry aonl_swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_angry.png") )

    image pi grin aonl_swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_grin.png") )

    image pi normal aonl_swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_normal.png") )

    image pi serious aonl_swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_serious.png") )

    image pi shocked aonl_swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_shocked.png") )

    image pi smile aonl_swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_smile.png") )

    image pi surprise aonl_swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_surprise.png") )

    image pi upset aonl_swim = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/normal/pi/pi_2_upset.png") )

    # Пионерская форма, far
    
    image pi angry aonl_pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_angry.png") )

    image pi grin aonl_pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_grin.png") )

    image pi normal aonl_pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_normal.png") )

    image pi serious aonl_pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_serious.png") )

    image pi shocked aonl_pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_shocked.png") )

    image pi smile aonl_pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_smile.png") )

    image pi surprise aonl_pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_surprise.png") )

    image pi upset aonl_pioneer far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_pioneer.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_upset.png") )

    # Рубашка, far
    
    image pi angry aonl_shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_angry.png") )

    image pi grin aonl_shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_grin.png") )

    image pi normal aonl_shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_normal.png") )

    image pi serious aonl_shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_serious.png") )

    image pi shocked aonl_shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_shocked.png") )

    image pi smile aonl_shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_smile.png") )

    image pi surprise aonl_shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_surprise.png") )

    image pi upset aonl_shirt far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_shirt.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_upset.png") )

    # Пальто, far
    
    image pi default aonl_coat far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_default.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_default.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_default.png") )

    image pi normal aonl_coat far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_coat.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_normal.png") )

    # Плавки, far
    image pi normal aonl_swim far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), aonl_imgs + "sprites/far/pi/pi_2_swim.png", (0,0), aonl_imgs + "sprites/far/pi/pi_2_normal.png") )

    # ДваЧе
    #
    # Спортивная форма
    
    image dv laugh aonl_sport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_laugh.png'))
    
    image dv normal aonl_sport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_normal.png'))
    
    image dv smile aonl_sport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_sport.png', (0, 0), 'images/sprites/normal/dv/dv_4_smile.png'))
    
    image dv soft smile aonl_sport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_sport.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_soft_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_sport.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_soft_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_sport.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_soft_smile.png'))
    
    image dv soft smile pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), 'images/sprites/normal/dv/dv_4_pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_soft_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), 'images/sprites/normal/dv/dv_4_pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_soft_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), 'images/sprites/normal/dv/dv_4_pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_soft_smile.png'))
    
    image dv soft smile pioneer2 = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), 'images/sprites/normal/dv/dv_4_pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_soft_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), 'images/sprites/normal/dv/dv_4_pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_soft_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_4_body.png', (0, 0), 'images/sprites/normal/dv/dv_4_pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_4_soft_smile.png'))
    
    image dv grin aonl_sport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_2_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_2_sport.png', (0, 0), 'images/sprites/normal/dv/dv_2_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_2_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_2_sport.png', (0, 0), 'images/sprites/normal/dv/dv_2_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_2_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_2_sport.png', (0, 0), 'images/sprites/normal/dv/dv_2_grin.png'))
    
    image dv surprise aonl_sport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_surprise.png'), im.matrix.tint(0.94, 0.82, 1.0)),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_surprise.png'), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_surprise.png'))
    
    image dv shocked aonl_sport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_shocked.png'), im.matrix.tint(0.94, 0.82, 1.0)),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_shocked.png'), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_shocked.png'))
    
    image dv scared aonl_sport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_scared.png'), im.matrix.tint(0.94, 0.82, 1.0)),
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_scared.png'), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_scared.png'))
    
    image dv cry aonl_sport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_cry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_cry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_1_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_1_sport.png', (0, 0), 'images/sprites/normal/dv/dv_1_cry.png'))
    
    image dv guilty aonl_sport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_guilty.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_guilty.png'), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_guilty.png'))
    
    image dv sad aonl_sport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_sad.png'))
    
    image dv shy aonl_sport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_3_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_3_sport.png', (0, 0), 'images/sprites/normal/dv/dv_3_shy.png'))
    
    image dv angry aonl_sport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_5_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_5_sport.png', (0, 0), 'images/sprites/normal/dv/dv_5_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_5_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_5_sport.png', (0, 0), 'images/sprites/normal/dv/dv_5_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)),
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_5_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_5_sport.png', (0, 0), 'images/sprites/normal/dv/dv_5_angry.png'))
    
    image dv rage aonl_sport = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'images/sprites/normal/dv/dv_5_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_5_sport.png', (0, 0), 'images/sprites/normal/dv/dv_5_rage.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_5_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_5_sport.png', (0, 0), 'images/sprites/normal/dv/dv_5_rage.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080),  (0, 0), 'images/sprites/normal/dv/dv_5_body.png', (0, 0), aonl_imgs + 'sprites/normal/dv/dv_5_sport.png', (0, 0), 'images/sprites/normal/dv/dv_5_rage.png'))
    
    # Тёмная Лена, close
    
    image aonl_dark_un evil_smile pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), aonl_imgs + "sprites/close/dark_un/un_1_body.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_1_pioneer.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_1_evil_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), aonl_imgs + "sprites/close/dark_un/un_1_body.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_1_pioneer.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), aonl_imgs + "sprites/close/dark_un/un_1_body.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_1_pioneer.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_1_evil_smile.png") )
    
    image aonl_dark_un angry2 pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), aonl_imgs + "sprites/close/dark_un/un_3_body.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_3_pioneer.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_3_angry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), aonl_imgs + "sprites/close/dark_un/un_3_body.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_3_pioneer.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_3_angry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), aonl_imgs + "sprites/close/dark_un/un_3_body.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_3_pioneer.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_3_angry2.png") )
    
    image aonl_dark_un scared pioneer close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), aonl_imgs + "sprites/close/dark_un/un_2_body.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_2_pioneer.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), aonl_imgs + "sprites/close/dark_un/un_2_body.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_2_pioneer.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), aonl_imgs + "sprites/close/dark_un/un_2_body.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_2_pioneer.png",(0,0), aonl_imgs + "sprites/close/dark_un/un_2_scared.png") )
    
    # Славя с распущенными волосами, голая (взято из 7ДЛ)
    # Упрощённая версия, объявлена только дневная версия
    image sl normal aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/sl/sl_1_body2.png", (0,0), "images/sprites/normal/sl/sl_1_normal.png")
    image sl serious aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/sl/sl_1_body2.png", (0,0), "images/sprites/normal/sl/sl_1_serious.png")
    image sl serious aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/sl/sl_1_body2.png", (0,0), "images/sprites/normal/sl/sl_1_serious.png")
    image sl smile aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/sl/sl_1_body2.png", (0,0), "images/sprites/normal/sl/sl_1_smile.png")
    image sl happy aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/sl/sl_2_body2.png", (0,0), "images/sprites/normal/sl/sl_2_happy.png")
    image sl laugh aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/sl/sl_2_body2.png", (0,0), "images/sprites/normal/sl/sl_2_laugh.png")
    image sl shy aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/sl/sl_2_body2.png", (0,0), "images/sprites/normal/sl/sl_2_shy.png")
    image sl smile2 aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/sl/sl_2_body2.png", (0,0), "images/sprites/normal/sl/sl_2_smile2.png")
    image sl angry aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/sl/sl_3_body2.png", (0,0), "images/sprites/normal/sl/sl_3_angry.png")
    image sl sad aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/sl/sl_3_body2.png", (0,0), "images/sprites/normal/sl/sl_3_sad.png")
    image sl surprise aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/sl/sl_3_body2.png", (0,0), "images/sprites/normal/sl/sl_3_surprise.png")
    image sl scared aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/sl/sl_4_body2.png", (0,0), "images/sprites/normal/sl/sl_4_scared.png")
    image sl tender aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/sl/sl_4_body2.png", (0,0), "images/sprites/normal/sl/sl_4_tender.png")
    
    # у с распущенными волосами, голая (взято из БКРР)
    # Упрощённая версия, объявлена только дневная версия
    image mi cry aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_1_body_loo.png", (0,0), "images/sprites/normal/mi/mi_1_cry.png")
    image mi dontlike aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_1_body_loo.png", (0,0), "images/sprites/normal/mi/mi_1_dontlike.png")
    image mi laugh aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_1_body_loo.png", (0,0), "images/sprites/normal/mi/mi_1_laugh.png")
    image mi scared aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_1_body_loo.png", (0,0), "images/sprites/normal/mi/mi_1_scared.png")
    image mi shocked aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_1_body_loo.png", (0,0), "images/sprites/normal/mi/mi_1_shocked.png")
    image mi shy aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_1_body_loo.png", (0,0), "images/sprites/normal/mi/mi_1_shy.png")
    image mi surprise aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_1_body_loo.png", (0,0), "images/sprites/normal/mi/mi_1_surprise.png")
    image mi cry_smile aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_2_body_loo.png", (0,0), "images/sprites/normal/mi/mi_2_cry_smile.png")
    image mi grin aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_2_body_loo.png", (0,0), "images/sprites/normal/mi/mi_2_grin.png")
    image mi happy aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_2_body_loo.png", (0,0), "images/sprites/normal/mi/mi_2_happy.png")
    image mi sad aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_2_body_loo.png", (0,0), "images/sprites/normal/mi/mi_2_sad.png")
    image mi smile aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_2_body_loo.png", (0,0), "images/sprites/normal/mi/mi_2_smile.png")
    image mi angry aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_3_body_loo.png", (0,0), "images/sprites/normal/mi/mi_3_angry.png")
    image mi normal aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_3_body_loo.png", (0,0), "images/sprites/normal/mi/mi_3_normal.png")
    image mi rage aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_3_body_loo.png", (0,0), "images/sprites/normal/mi/mi_3_rage.png")
    image mi serious aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_3_body_loo.png", (0,0), "images/sprites/normal/mi/mi_3_serious.png")
    image mi upset aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mi/mi_3_body_loo.png", (0,0), "images/sprites/normal/mi/mi_3_upset.png")
    
    # Женя, голая (взято из Лето в библиотеке)
    # Упрощённая версия, объявлена только дневная версия
    image mz bukal aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mz/1_body.png", (0,0), "images/sprites/normal/mz/mz_1_bukal.png")
    image mz laugh aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mz/1_body.png", (0,0), "images/sprites/normal/mz/mz_1_laugh.png")
    image mz normal aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mz/1_body.png", (0,0), "images/sprites/normal/mz/mz_1_normal.png")
    image mz angry aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mz/2_body.png", (0,0), "images/sprites/normal/mz/mz_2_angry.png")
    image mz rage aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mz/2_body.png", (0,0), "images/sprites/normal/mz/mz_2_rage.png")
    image mz shy aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mz/3_body.png", (0,0), "images/sprites/normal/mz/mz_3_shy.png")
    image mz smile aonl_body = im.Composite((900,1080), (0,0), aonl_imgs + "sprites/normal/mz/3_body.png", (0,0), "images/sprites/normal/mz/mz_3_smile.png")
    
    # Лена 25
    # Зимняя одежда
    image aonl_un25 angry future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/un25/angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/un25/angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/un25/angry.png'))
    
    image aonl_un25 normal future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/un25/normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/un25/normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/un25/normal.png'))
    
    image aonl_un25 shy future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/un25/shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/un25/shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/un25/shy.png'))
    
    image aonl_un25 smile future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/un25/smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/un25/smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/un25/smile.png'))
    
    image aonl_un25 smile2 future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/un25/smile2.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/un25/smile2.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/un25/smile2.png'))
    
    # Пионерская форма
    image aonl_un25 angry future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/un25/angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/un25/angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/un25/angry.png'))
    
    image aonl_un25 normal future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/un25/normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/un25/normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/un25/normal.png'))
    
    image aonl_un25 shy future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/un25/shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/un25/shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/un25/shy.png'))
    
    image aonl_un25 smile future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/un25/smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/un25/smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/un25/smile.png'))
    
    image aonl_un25 smile2 future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/un25/smile2.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/un25/smile2.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/un25/smile2.png'))
    
    image aonl_un25 serious future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/un25/serious.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/un25/serious.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/un25/serious.png'))
    
    image aonl_un25 smile3 future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/un25/smile3.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/un25/smile3.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/un25/smile3.png'))
    
    image aonl_un25 sad future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body3.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer3.png', (0, 0), aonl_imgs + 'sprites/normal/un25/sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body3.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer3.png', (0, 0), aonl_imgs + 'sprites/normal/un25/sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/un25/body3.png', (0, 0), aonl_imgs + 'sprites/normal/un25/pioneer3.png', (0, 0), aonl_imgs + 'sprites/normal/un25/sad.png'))



    # Мику ночь
    image aonl_mi cry night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/cry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/cry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/cry.png'))

    image aonl_mi dontlike night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/dontlike.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/dontlike.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/dontlike.png'))

    image aonl_mi laugh night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/laugh.png'))

    image aonl_mi scared night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/scared.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/scared.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/scared.png'))

    image aonl_mi shocked night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/shocked.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/shocked.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/shocked.png'))

    image aonl_mi shy night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/shy.png'))

    image aonl_mi surprise night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/surprise.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/surprise.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_1_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night1.png', (0, 0), aonl_imgs + 'sprites/normal/mi/surprise.png'))

    image aonl_mi cry_smile night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_2_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night2.png', (0, 0), aonl_imgs + 'sprites/normal/mi/cry_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_2_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night2.png', (0, 0), aonl_imgs + 'sprites/normal/mi/cry_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_2_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night2.png', (0, 0), aonl_imgs + 'sprites/normal/mi/cry_smile.png'))

    image aonl_mi grin night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_2_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night2.png', (0, 0), aonl_imgs + 'sprites/normal/mi/grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_2_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night2.png', (0, 0), aonl_imgs + 'sprites/normal/mi/grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_2_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night2.png', (0, 0), aonl_imgs + 'sprites/normal/mi/grin.png'))

    image aonl_mi happy night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_2_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night2.png', (0, 0), aonl_imgs + 'sprites/normal/mi/happy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_2_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night2.png', (0, 0), aonl_imgs + 'sprites/normal/mi/happy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_2_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night2.png', (0, 0), aonl_imgs + 'sprites/normal/mi/happy.png'))

    image aonl_mi sad night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_2_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night2.png', (0, 0), aonl_imgs + 'sprites/normal/mi/sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_2_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night2.png', (0, 0), aonl_imgs + 'sprites/normal/mi/sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_2_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night2.png', (0, 0), aonl_imgs + 'sprites/normal/mi/sad.png'))

    image aonl_mi smile night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_2_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night2.png', (0, 0), aonl_imgs + 'sprites/normal/mi/smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_2_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night2.png', (0, 0), aonl_imgs + 'sprites/normal/mi/smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_2_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night2.png', (0, 0), aonl_imgs + 'sprites/normal/mi/smile.png'))

    image aonl_mi angry night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_3_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night3.png', (0, 0), aonl_imgs + 'sprites/normal/mi/angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_3_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night3.png', (0, 0), aonl_imgs + 'sprites/normal/mi/angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_3_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night3.png', (0, 0), aonl_imgs + 'sprites/normal/mi/angry.png'))

    image aonl_mi normal night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_3_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night3.png', (0, 0), aonl_imgs + 'sprites/normal/mi/normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_3_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night3.png', (0, 0), aonl_imgs + 'sprites/normal/mi/normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_3_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night3.png', (0, 0), aonl_imgs + 'sprites/normal/mi/normal.png'))

    image aonl_mi rage night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_3_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night3.png', (0, 0), aonl_imgs + 'sprites/normal/mi/rage.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_3_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night3.png', (0, 0), aonl_imgs + 'sprites/normal/mi/rage.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_3_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night3.png', (0, 0), aonl_imgs + 'sprites/normal/mi/rage.png'))

    image aonl_mi serious night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_3_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night3.png', (0, 0), aonl_imgs + 'sprites/normal/mi/serious.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_3_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night3.png', (0, 0), aonl_imgs + 'sprites/normal/mi/serious.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_3_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night3.png', (0, 0), aonl_imgs + 'sprites/normal/mi/serious.png'))

    image aonl_mi upset night = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_3_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night3.png', (0, 0), aonl_imgs + 'sprites/normal/mi/upset.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_3_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night3.png', (0, 0), aonl_imgs + 'sprites/normal/mi/upset.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi/mi_3_body_loo.png', (0, 0), aonl_imgs + 'sprites/normal/mi/night3.png', (0, 0), aonl_imgs + 'sprites/normal/mi/upset.png'))



    # Мику 25
    # Зимняя одежда
    image aonl_mi25 angry future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/angry.png'))
    
    image aonl_mi25 normal future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/normal.png'))
    
    image aonl_mi25 rage future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/rage.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/rage.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/rage.png'))
    
    image aonl_mi25 serious future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/serious.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/serious.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/serious.png'))
    
    image aonl_mi25 upset future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/upset.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/upset.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/upset.png'))
    
    image aonl_mi25 cry_smile future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/cry_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/cry_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/cry_smile.png'))
    
    image aonl_mi25 grin future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/grin.png'))
    
    image aonl_mi25 happy future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/happy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/happy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/happy.png'))
    
    image aonl_mi25 sad future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/sad.png'))
    
    image aonl_mi25 smile future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/smile.png'))
    
    # Пионерская форма
    image aonl_mi25 angry future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/angry.png'))
    
    image aonl_mi25 normal future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/normal.png'))
    
    image aonl_mi25 rage future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/rage.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/rage.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/rage.png'))
    
    image aonl_mi25 serious future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/serious.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/serious.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/serious.png'))
    
    image aonl_mi25 upset future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/upset.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/upset.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/upset.png'))
    
    image aonl_mi25 cry_smile future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/cry_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/cry_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/cry_smile.png'))
    
    image aonl_mi25 grin future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/grin.png'))
    
    image aonl_mi25 happy future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/happy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/happy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/happy.png'))
    
    image aonl_mi25 sad future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/sad.png'))
    
    image aonl_mi25 smile future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/mi25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/mi25/smile.png'))
    
    # Алиса 25
    # Зимняя одежда
    image aonl_dv25 laugh future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/laugh.png'))
    
    image aonl_dv25 normal future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/normal.png'))
    
    image aonl_dv25 smile future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/smile.png'))
    
    image aonl_dv25 guilty future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/guilty.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/guilty.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/guilty.png'))
    
    image aonl_dv25 shy future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/shy.png'))
    
    # Пионерская форма
    image aonl_dv25 laugh future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/laugh.png'))
    
    image aonl_dv25 normal future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/normal.png'))
    
    image aonl_dv25 smile future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/smile.png'))
    
    image aonl_dv25 guilty future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/guilty.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/guilty.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/guilty.png'))
    
    image aonl_dv25 shy future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/dv25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/pioneer2.png', (0, 0), aonl_imgs + 'sprites/normal/dv25/shy.png'))
    
    # Ульяна 25
    # Зимняя одежда
    image aonl_us25 grin future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/grin.png'))
    
    image aonl_us25 laugh future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/laugh.png'))
    
    image aonl_us25 laugh_simle future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/laugh_simle.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/laugh_simle.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/laugh_simle.png'))
    
    image aonl_us25 normal future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/normal.png'))
    
    image aonl_us25 sad future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/sad.png'))
    
    image aonl_us25 smile future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/coat1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/smile.png'))
    
    # Пионерская форма
    image aonl_us25 grin future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/grin.png'))
    
    image aonl_us25 laugh future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/laugh.png'))
    
    image aonl_us25 laugh_simle future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/laugh_simle.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/laugh_simle.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/laugh_simle.png'))
    
    image aonl_us25 normal future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/normal.png'))
    
    image aonl_us25 sad future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/sad.png'))
    
    image aonl_us25 smile future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us25/body1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/pioneer1.png', (0, 0), aonl_imgs + 'sprites/normal/us25/smile.png'))
    
    # Ульяна
    # Полотенце

    image aonl_us normal towel = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/normal.png'))

    image aonl_us laugh towel = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/laugh.png'))

    image aonl_us laugh2 towel = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/laugh2.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/laugh2.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/laugh2.png'))

    image aonl_us grin towel = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/grin.png'))

    image aonl_us sad towel = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/sad.png'))

    image aonl_us smile towel = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/us/body2.png', (0, 0), aonl_imgs + 'sprites/normal/us/towel2.png', (0, 0), aonl_imgs + 'sprites/normal/us/smile.png'))

    # Славя 25
    # Зимняя одежда
    image aonl_sl25 normal future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/normal.png'))
    
    image aonl_sl25 serious future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/serious.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/serious.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/serious.png'))
    
    image aonl_sl25 smile future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/smile.png'))
    
    image aonl_sl25 happy future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/happy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/happy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/happy.png'))
    
    image aonl_sl25 laugh future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/laugh.png'))
    
    image aonl_sl25 shy future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/shy.png'))
    
    image aonl_sl25 smile2 future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/smile2.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/smile2.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat2.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/smile2.png'))
    
    image aonl_sl25 sad future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body3.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat3.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/sad.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body3.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat3.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/sad.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body3.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat3.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/sad.png'))

    image aonl_sl25 surprise future_winter = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body3.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat3.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/surprise.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body3.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat3.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/surprise.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body3.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/coat3.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/surprise.png'))
    
    # Пионерская форма
    image aonl_sl25 normal future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/normal.png'))
    
    image aonl_sl25 serious future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/serious.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/serious.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/serious.png'))
    
    image aonl_sl25 smile future = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), 
    "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), 
    True, im.Composite((900, 1080), (0, 0), aonl_imgs + 'sprites/normal/sl25/body.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/pioneer.png', (0, 0), aonl_imgs + 'sprites/normal/sl25/smile.png'))
    
