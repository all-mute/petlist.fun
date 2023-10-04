import os


def get_fonts(directory="C:/Users/Eva-02/PycharmProjects/petlist.fun/assets/fonts"):
    font_dict = {}

    for filename in os.listdir(directory):
        if filename.endswith(".ttf"):
            name = os.path.splitext(filename)[0]
            font_dict[name] = f"/fonts/{filename}"

    return font_dict

#print(get_fonts())
