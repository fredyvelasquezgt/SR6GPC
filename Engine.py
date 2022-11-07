from libraryGame import Renderer, V3, _color

from obj import Texture


width = 1920
height = 1080

rend = Renderer(width, height)

modelTexture = Texture("models/wings.bmp")
# rend.clear_color
rend.glClearColor(1, 1, 1)
rend.glClear()

modelPosition = V3(0, 0, -10)
# modelPosition2 = V3(5, 0, -10)

rend.glLookAt(modelPosition, V3(0, 8, 0))
# rend.glLookAt(modelPosition2, V3(50, 8, 0))

rend.glLoadModel("models/dragon.obj",
                 modelTexture,
                 translate=modelPosition,
                 scale=V3(0.01, 0.01, 0.01),
                 rotate=V3(0, 0, 0))


rend.glFinish("prueba.bmp")
