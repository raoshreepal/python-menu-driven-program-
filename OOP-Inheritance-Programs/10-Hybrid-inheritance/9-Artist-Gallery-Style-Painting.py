#✅ 9. Artist + Gallery + Style = Painting

class Artist:
    def __init__(self, name):
        self.name = name

class Gallery:
    def __init__(self, gallery_name):
        self.gallery_name = gallery_name

class Style:
    def __init__(self, style_type):
        self.style_type = style_type

class Painting(Artist, Gallery, Style):
    def __init__(self, name, gallery_name, style_type):
        Artist.__init__(self, name)
        Gallery.__init__(self, gallery_name)
        Style.__init__(self, style_type)

    def display(self):
        print(f"Painting by {self.name} in {self.gallery_name} gallery | Style: {self.style_type}")

p = Painting("M. F. Husain", "Modern Art", "Cubism")
p.display()
