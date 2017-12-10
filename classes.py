class Contributor:
    contributors = []

    def __init__(self, first_name, middle_initial, last_name, suffix):
        contributor = "{},{}.{mi}{s}".format(last_name.title(),
                                             first_name[0].title(),
                                             mi=(middle_initial[0] + '.').title() if middle_initial != '' else '',
                                             s=("," + suffix + '.').title() if suffix != '' else ''
                                             )
        self.contributors.append(contributor)

    def get_contributors(self):
        contributors = sorted(self.contributors)

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


class Journal:
    def __init__(self, article_title, journal_title, year_published, page_start,
                 page_end, volume, issue, series, doi_or_website):
        self.article_title = article_title
        self.journal_title = journal_title
        self.year_published = year_published
        self.pages = f"{page_start}-{page_end}." if page_start != '' and page_end != '' else ''

        self.volume_issue = ''
        if volume != '' and issue != '':
            self.volume_issue = f"{volume}({issue}),"
        elif volume != "" and issue == '':
            self.volume_issue = f"{volume},"
        else:
            self.volume_issue = ''
        self.series = series if series != '' else ''
        self.doi_or_website = doi_or_website if doi_or_website != '' else ''

        # Last, F. M., Jr. (year). Article Title. Journal Title, Volume(Issue), series, P-Start-P-End.
        # doi:DOI_OR_WEBSITE

        self.journal = "({}). {}. {},{}{} {}{}".format(self.year_published, self.article_title, self.journal_title,
                                                       self.volume_issue, self.series, self.pages, self.doi_or_website)
        if self.journal[-1] == ',':
            self.journal = self.journal[0:-1] + '.'

    def get_journal_entry(self):
        return self.journal


class Reference:
    references = []

    def __init__(self, contributors, journal):
        self.reference = f"{contributors} {journal}"
        self.references.append(self.reference)

    def get_reference(self):
        return self.reference
