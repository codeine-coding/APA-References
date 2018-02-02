class Journal:
    def __init__(self, article_title, journal_title, year_published, page_start,
                 page_end, volume, issue, doi_or_website):
        self.article_title = article_title
        self.journal_title = journal_title
        self.year_published = year_published
        self.page_start = page_start
        self.page_end = page_end
        self.volume = volume
        self.issue = issue
        self.doi = doi_or_website

        self.pages = f"{page_start}-{page_end}." if page_start != '' and page_end != '' else ''
        self.volume_issue = ''
        if volume != '' and issue != '':
            self.volume_issue = f"{volume}({issue}),"
        elif volume != "" and issue == '':
            self.volume_issue = f"{volume},"
        else:
            self.volume_issue = ''
        self.doi_or_website = doi_or_website if doi_or_website != '' else ''

        # Last, F. M., Jr. (year). Article Title. Journal Title, Volume(Issue), series, P-Start-P-End.
        # doi:DOI_OR_WEBSITE

    def get_journal_entry(self):
        journal = "({}). {}. {},{} {} {}".format(self.year_published, self.article_title, self.journal_title,
                                                 self.volume_issue, self.pages, self.doi_or_website)
        if journal[-1] == ',':
            journal = journal[0:-1] + '.'
        return journal
