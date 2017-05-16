
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

class line_item(object):
    """ some docstring here """
    def __init__(self):
        pass

    def important(self):
        self.important = True

    def description(self, description):
        self.description = description

    def start_date(self, start_date):
        self.start_date = start_date

    def end_date(self, end_date):
        self.end_date = end_date

class specification(line_item):
    """ """
    def __init__(self):
        super(specification, self).__init__()

class degree(specification):
    """ """
    def __init__(self, _degree, field):
        super(degree, self).__init__()
        self.degree = _degree
        self.field = field

class phd(degree):
    """ """
    def __init__(self, field):
        super(phd, self).__init__('Ph.D.', field)

class ms(degree):
    """ """
    def __init__(self, field):
        super(ms, self).__init__('M.S.', field)

class bs(degree):
    """ """
    def __init__(self, field):
        super(bs, self).__init__('B.S.', field)

class experience(line_item):
    """ """
    def __init__(self):
        super(experience, self).__init__()

class job(experience):
    """ """
    def __init__(self):
        super(job, self).__init__()

class project(experience):
    """ """
    def __init__(self):
        super(project, self).__init__()
