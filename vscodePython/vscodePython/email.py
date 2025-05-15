email = input("Enter your Email: ").strip()
domain = input("Enter your domain password: ").strip()

username = email[:email.index('@')]
domainPassword = domain[domain.index('') + 0:]

print(f"your username is {username} and domain is {domainPassword}")
