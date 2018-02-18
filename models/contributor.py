class Contributor:
    contributors = []

    def __init__(self, first_name, middle_initial, last_name):
        contributor = "{},{}.{mi}".format(last_name.title(),
                                          first_name[0].title(),
                                          mi=(middle_initial[0] + '.').title() if middle_initial != '' else '')
        self.contributors.append(contributor)

    @classmethod
    def get_contributors(cls):
        contributors = cls.contributors

        if len(contributors) == 1:
            authors = contributors[0]
        elif len(contributors) == 2:
            authors = ', & '.join(contributors)
        elif 3 <= len(contributors) <= 7:
            authors = (', '.join(contributors[0:-1]) + ', & {}'.format(contributors[-1]))
        elif len(contributors) > 7:
            authors = (', '.join(contributors[0:6]) + ',...{}'.format(contributors[-1]))
        else:
            authors = ''

        return authors