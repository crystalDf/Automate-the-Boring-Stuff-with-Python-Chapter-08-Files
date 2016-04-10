import os

path = os.path.join('usr', 'bin', 'spam')

print(path)

my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in my_files:
    print(os.path.join(path, filename))

print(os.getcwd())
