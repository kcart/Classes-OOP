"""This file should have our melon-type classes in it."""
class Melon(object):
    
    def get_base_price(self):
        return 5.00

class WatermelonOrder(Melon):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        if qty >= 3:
            return qty * Melon.get_base_price() * .75 
        else:
            return qty * Melon.get_base_price()

class Cantaloupe(Melon):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        if qty >=5:
            return qty * Melon.get_base_price() * .5
        else:
            return qty * Melon.get_base_price()

        

class Casaba(Melon):
    species = "Casaba"
    color = 'green'
    imported = True
    shape = "natural"
    seasons = ['Spring','Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        return qty * ((Melon.get_base_price() + 1) * 1.5)

class Sharlyn(Melon):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        return qty * (Melon.get_base_price() * 1.5)

class SantaClaus(Melon):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ['Winter', "Spring"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        return qty * (Melon.get_base_price() * 1.5)

class Christmas(Melon):
    species = "Christmas"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Winter", "Spring"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        return qty * Melon.get_base_price()

class HornedMelon(Melon):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        return qty * (Melon.get_base_price() * 1.5)

class Xigua(Melon):
    species = "Xigua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        return qty * (Melon.get_base_price() * 2 * 1.5)

class Ogen(Melon):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        return qty * (Melon.get_base_price() + 1)