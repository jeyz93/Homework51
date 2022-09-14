class Cat:

    def __init__(self, name=None, age=2, satiety=40, happy=10, sleep=0, avatar=None):
        self.name = name
        self.age = age
        self.satiety = satiety
        self.happy = happy
        self.avatar = avatar
        self.sleep = sleep

    def check_stat(self):
        if self.satiety > 100:
            self.happy = 0

    def set_avatar(self):
        if self.happy < 40:
            self.avatar = "images/cat2.jpg"
        if self.happy >= 40:
            self.avatar = "images/cat1.jpeg"
        if self.satiety > 100:
            self.avatar = "images/catfat.jpeg"
        if self.sleep == 1:
            self.avatar = "images/cat3.jpg"
        return self.avatar
