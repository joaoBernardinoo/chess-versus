import pyglet


def image( file ):
    img = pyglet.image.load( file )
    return img

def sprite( img, x, y, batch ):
    return pyglet.sprite.Sprite(img,x,y,batch=batch)


