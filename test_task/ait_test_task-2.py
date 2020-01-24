import re


"""
You have a list of emails.
Task: you should to collect all the names from the mails list, where mail contains 'Subject: * viewed the
document'.
The result should be a list of unique name entries.
"""

def get_viewers_names(email_list):
    pattern = r'Subject: [\w\s]+ viewed'
    names = set()
    for mail in email_list:
        if re.search(pattern, mail):
            message = re.search(pattern, mail).group()
            name = message[9: -7]
            names.add(name)
    return list(names)



if __name__ == '__main__':

    mails = [
        'Sep 30, 2019. From: Robot. Subject: John Doe viewed the document. 123',
        'Oct 15, 2019. To: me. Subject: Spam. Spam',
        'Dec 2, 2019. From: Robot. To: me. Subject: Vasya Pupkin viewed the document. Please sign',
        'Dec 15, 2019. Subject: The truth is out there',
        'Dec 25, 2019. Subject: Merry Christmas!',
        'Jan 10, 2020. Subject: Fox Mulder viewed the document. Please check',
        'Jan 12, 2020. Subject: John Doe viewed the document. Great news...',
        'Jan 12, 2020. Subject: Frank Good Man viewed the document.',
        'Jan 12, 2020. Subject: Billy viewed the document.'
    ]

    print(get_viewers_names(mails))
