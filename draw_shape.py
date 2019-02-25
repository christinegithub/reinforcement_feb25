
def draw_shape(options):

    shape = ""

    for r in range(options['rows']):
        for c in range(options['cols']):
            shape += options['char']

        shape += "\n"

    return shape


options = [
    {
        'rows': 4,
        'cols': 4,
        'char': '*'
    },
    {
        'rows': 3,
        'cols': 9,
        'char': '0'
    }
]

print(draw_shape(options[0]))

print(draw_shape(options[1]))
