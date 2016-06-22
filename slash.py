import os

path = os.path.join('usr', 'bin', 'spam')

print(path)

my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in my_files:
    print(os.path.join(path, filename))

print()

cwd = os.getcwd()
print(os.getcwd())
os.chdir('/Users')
print(os.getcwd())
os.chdir(cwd)
print(os.getcwd())

print()

print(os.path.abspath('.'))
print(os.path.abspath('./Scripts'))

print()

# print(os.makedirs(os.path.abspath('./Scripts')))
#
# print()

print(os.path.relpath(os.path.abspath('./Scripts')))
print(os.path.relpath(os.path.abspath('./Scripts'), '/Users'))
print(os.path.relpath(os.path.abspath('./Scripts'), '/Applications'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print()

print(os.path.basename(os.path.abspath('.')))
print(os.path.dirname(os.path.abspath('.')))
print(os.path.split(os.path.abspath('.')))
print(os.path.abspath('.').split(os.path.sep))

print()

print(os.path.getsize('.'))
print(os.listdir('.'))

total_size = 0
for filename in os.listdir('.'):
    total_size += os.path.getsize(os.path.join('.', filename))
print(total_size)

print()

print(os.path.exists(os.path.join(os.getcwd(), './Scripts')))
print(os.path.exists(os.path.join(os.getcwd(), './script')))
print(os.path.isfile(os.path.join(os.getcwd(), './Scripts')))
print(os.path.isfile(os.path.join(os.getcwd(), './slash.py')))
print(os.path.isdir(os.path.join(os.getcwd(), './Scripts')))
print(os.path.isdir(os.path.join(os.getcwd(), './slash.py')))
