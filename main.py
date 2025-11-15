class Transport:
    def __init__(self, tezlik):
        self.tezlik = tezlik

    def tezlik_oshirish(self):
        pass

    def yoqilgi_sarfi(self):
        pass

    def sayohat_masofa(self, masofa):
        vaqt = masofa / self.tezlik
        yoqilgi = masofa * self.yoqilgi_sarfi()
        return vaqt, yoqilgi

    def yuk_kotarish(self, yuk):
        return 0  # default


class Avtobus(Transport):
    def tezlik_oshirish(self):
        self.tezlik += 10

    def yoqilgi_sarfi(self):
        return 0.25


class YukMashinasi(Transport):
    def tezlik_oshirish(self):
        self.tezlik += 5

    def yoqilgi_sarfi(self):
        return 0.5

    def yuk_kotarish(self, yuk):
        return f"{yuk} kg yuk ko‘tarildi"


class SportAvto(Transport):
    def tezlik_oshirish(self):
        self.tezlik += 20

    def yoqilgi_sarfi(self):
        return 0.4


# TEST
park = [
    Avtobus(60),
    YukMashinasi(40),
    SportAvto(120)
]

for t in park:
    print(t.sayohat_masofa(200))
