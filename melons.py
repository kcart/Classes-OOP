"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']
    base_price = 5.0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if qty >= 3:
            return qty * self.base_price * .75 
        else:
            return qty * self.base_price

class Cantaloupe(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ['Spring', 'Summer']
    base_price = 5.0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if qty >=5:
            return qty * self.base_price * .5
        else:
            return qty * self.base_price

        

class Casaba(object):
    species = "Casaba"
    color = 'green'
    imported = True
    shape = "natural"
    seasons = ['Spring','Summer', 'Fall', 'Winter']
    base_price = 9.0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        return qty * self.base_price

class Sharlyn(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    seasons = ["Summer"]
    base_price = 7.50

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        return qty * self.base_price

class SantaClaus(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ['Winter', "Spring"]
    base_price = 7.50 

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        return qty * self.base_price

class Christmas(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Winter", "Spring"]
    base_price = 5.00

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        return qty * self.base_price

class HornedMelon(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]
    base_price = 7.50

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        return qty * self.base_price

class Xigua(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ["Summer"]
    base_price = 15.0

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        return qty * self.base_price

class Ogen(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]
    base_price = 6.00 

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        return qty * self.base_price