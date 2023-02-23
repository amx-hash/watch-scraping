class Watch:
    def __init__(self, brand, name, ref, condition, box, papers, price):
        self.set_brand(brand)
        self.set_name(name)
        self.set_ref(ref)
        self.set_condition(condition)
        self.set_box(box)
        self.set_papers(papers)
        self.set_price(price)

    def set_brand(self, brand):
        self.brand = brand

    def set_name(self, name):
        self.name = name

    def set_ref(self, ref):
        self.ref = ref

    def set_condition(self, condition):
        self.condition = condition

    def set_box(self, box):
        self.box = box

    def set_papers(self, papers):
        self.papers = papers

    def set_price(self, price):
        self.price = price

    def get_brand(self):
        return self.brand

    def get_name(self):
        return self.name

    def get_ref(self):
        return self.ref

    def get_condition(self):
        return self.condition

    def get_box(self):
        return self.box

    def get_papers(self):
        return self.box

    def get_price(self):
        return self.price
