from PIL import Image

def get_image(filename):
    return Image.open(filename)
    
def get_size(img):
    return img.size
    
def get_colors(img):
    colors = []
    colors_t = {
        
    }
    width, height = get_size(img)
    for i in range(int(width/4)):
        for j in range(int(height/4)):
            # Crear tupla
            colores_img = img.getpixel((i*4,j*4))

            # Comprobar si valor existe en la lista
            if (colores_img in colors):
                # Si existe, sumar uno al indice de la tupla
                update_dict(colores_img, colors_t)
            else:
                # Si no, añadir la tupla con indice en 1
                key = colores_img
                value = 1
                add_to_dict(key, value, colors_t)

                # Añadir valor a la lista
                colors.append(colores_img)

    return colors_t

def add_to_dict(key, value, d):
    d[key] = value

def update_dict(key, d):
    d[key] = d[key] + 1

def get_palette(d):
    palette = []
    for i in range(4):
        max_key = max(d, key=d.get)
        palette.append(max_key)
        del d[max_key]

    return palette