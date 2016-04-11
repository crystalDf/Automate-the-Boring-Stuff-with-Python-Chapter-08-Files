import os

path = os.path.join('usr', 'bin', 'spam')

print(path)

my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in my_files:
    print(os.path.join(path, filename))

print(os.getcwd())

print(os.path.abspath('.'))
print(os.path.abspath('./Scripts'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.basename(os.path.abspath('.')))
print(os.path.dirname(os.path.abspath('.')))
print(os.path.split(os.path.abspath('.')))
print(os.path.abspath('.').split(os.path.sep))
