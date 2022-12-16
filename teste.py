import pyglet
from pyglet.window.key import *

window = pyglet.window.Window()

batch = pyglet.graphics.Batch()

@window.event
def on_draw():
    pyglet.gl.glClearColor( *background, 1 )
    window.clear()
    batch.draw()



key_state = key_state_old = set()

@window.event
def on_key_press( symbol, modifiers ):
    key_state.add( symbol )

@window.event
def on_key_release( symbol, modifiers ):
    key_state.discard( symbol )


def key( k ):
    return k in key_state

def key_old( k ):
    return k in key_state_old

def score( s=0 ):
    global score_draw, score_now, score_best

    score_draw = True
    score_now = max( 0, score_now+s )
    score_best = max( score_now, score_best )

    return score_now


movers = []

class Mover:
    pass

def create_object( move_func, image=None, size=0.1, x=0, y=0, vx=0, vy=0, **kargs ):
    m = Mover()
    m.move = move_func
    m.image = image

    if image:
        m.sprite = pyglet.sprite.Sprite( image, batch=batch )
        m.sprite.scale_x = m.sprite.scale_y = 0
    else:
        m.sprite = None

    m.sx = m.sy = size
    m.x, m.y = x, y
    m.vx, m.vy = vx, vy
    m.r = m.state = m.time = 0
    m.life = 1

    for k, v in kargs.items():
        setattr( m, k, v )
    
    movers.append( m )

    return m


def image( file ):
    img = pyglet.resource.image( file )
    img.anchor_x = img.width//2
    img.anchor_y = img.height//2
    return img


snd_dummy = None

def sound( file ):
    global snd_dummy

    if not snd_dummy:
        snd_dummy = pyglet.resource.media( 'dummy.wav' )
        snd_dummy.play()
    
    snd = pyglet.resource.media( file, streaming=False )

    return snd


def group( *move ):
    for m in movers:
        if m.move in move:
            yield m


time_sum = 0
time_min = 1/60*0.9
camera_x = camera_y = 0


def move_objects( dt ):
    global pause, score_now, fps_draw, help_draw, time_sum, time_min, movers

    time_sum += dt

    if not pause and time_sum >= time_min:
        time_sum = 0

        for m in movers:
            m.move( m )
        
        w, w2, h2 = window.width, window.width//2, window.height//2

        for m in movers:
            if m.sprite:
                m.sprite.image = m.image
                m.sprite.scale_x = m.sx * w / m.image.width
                m.sprite.scale_y = m.sy * w / m.image.height
                m.sprite.x = ( m.x - camera_x ) * w2 + w2
                m.sprite.y = ( m.y - camera_y ) * w2 + h2
                m.sprite.rotation = -m.r * 360
        
        old_movers = movers
        movers = [ m for m in old_movers if m.life > 0 ]
        old_movers.clear()


    if key( ESCAPE ):
        pyglet.app.exit()
    
    if key( BACKSPACE ):
        score_now = 0
        movers.clear()
        start()
    
    if key( F ) and not key_old( F ):
        fps_draw = not fps_draw
    
    if key( S ) and not key_old( S ):
        pause = not pause
    
    if key( H ) and not key_old( H ):
        help_draw = not help_draw
    
    global key_state_old
    key_state_old = key_state.copy()


def run( start_func, w=window.width, h=window.height, bg=(1,1,1), fs=False, tc=(0.5, 0.5, 0.5), tfn='Broadway' ):
    global start, background, text_color, text_font_name

    start = start_func
    background = bg
    snl, sbl, fl, pl = score_now_label, score_best_label, fps_label, pause_label
    snl.color = sbl.color = fl.color = pl.color = int( 255*tc[0] ), int( 255*tc[1] ), int( 255*tc[2] ), 255
    snl.font_name = sbl.font_name = fl.font_name = pl.font_name = tfn

    window.set_size( w, h )
    window.set_fullscreen( fs )

    start()

    pyglet.clock.schedule( move_objects )

    pyglet.app.run()