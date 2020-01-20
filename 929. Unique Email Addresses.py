class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_list = [i.split('@') for i in emails]
        categories = set()
        for j in emails_list:
            final_j0 = j[0].replace('.', '').split('+')[:1][0]
            final_j = '@'.join([final_j0, j[1]])
            categories.add(final_j)
        return len(categories)
