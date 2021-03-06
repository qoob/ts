from datetime import date


class User(object):

    def __init__(self, uid, first_name, last_name):
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.sex = None
        self.age = None

    def set_age(self, birth_date):
        if birth_date:
            self.age = int((date.today() - birth_date).days / 365.2425)

    def to_tsv(self):
        return u'\t'.join([unicode(self.uid), unicode(self.first_name), unicode(self.last_name), unicode(self.sex), unicode(self.age)])

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return u"User('{uid}', '{first}', '{last}')".format(uid=self.uid, first=self.first_name, last=self.last_name)
