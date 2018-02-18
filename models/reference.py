class Reference:
    references = []
    formatted_references = []

    def __init__(self, contributors, journal):
        self.contributors = contributors
        self.journal = journal
        self.references.append(self)
        self.formatted_reference = "{} {}".format(self.contributors, self.journal.get_journal_entry())
        self.formatted_references.append(self.formatted_reference)

    @classmethod
    def get_sorted_references(cls):
        return sorted(cls.references, key=lambda x: x.contributors)
