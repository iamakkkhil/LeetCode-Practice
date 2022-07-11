def unique_email(emails):
    corrected_emails = []
    for email in emails:
        domain_name = ""
        local_name = ""
        plus = False
        for i in range(len(email)):
            if email[i] == "+":
                plus = True
            elif plus == False and email[i] != "." and email[i] != "@":
                local_name += email[i]
            elif email[i] == "@":
                domain_name = email[i:]
                corrected_emails.append(local_name + domain_name)
                break

    print(len(set(corrected_emails)))


emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
unique_email(emails)
