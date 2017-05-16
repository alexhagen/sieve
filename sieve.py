
class sieve(object):
    """ some docstring here

    """
    def __init__(self, name):
        self.name = name
        self.sections = {}

    def email(self, email):
        """ some docstring here """
        # check if valid email
        self.email = email

    def phone(self, phone):
        """ some docstring here """
        # convert to all numbers
        # split into int array
        self.phone = phone

    def website(self, website):
        """ some docstring here """
        # check that website resolves
        self.website = website

    def location(self, location):
        """ some docstring here """
        # splti into address, city, state
        self.address = location
        self.city = location
        self.state = location

    def section(self, sname):
        """ some docstring here """
        self.sections[sname] = {}
        self.this_section = sname

    def add(self, matl, sect=None):
        """ some docstring here """
        if sect is not None:
            self.this_section = sect
        self.sections[self.this_section] = matl

    def cover_letter(self, cl):
        """ some docstring here """
        self.cl = cl

    def resume_export(self):
        """ some docstring here """
        for sect in self.sections.items():
            print sect
