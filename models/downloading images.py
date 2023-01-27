from quickdraw import QuickDrawDataGroup

class_names = ['donut', 'butterfly', 'eye', 'ice cream', 'crown', 'snowman', 'cat', 'clock', 'octopus', 'fish']

image_size = (28, 28)

for label in class_names:
    data = QuickDrawDataGroup(label, recognized=True)

    for i in range(2500):
        drawing = data.get_drawing()
        image = drawing.image
        image.resize(image_size).save('images/' + label + '/' + label + str(i) + '.png')