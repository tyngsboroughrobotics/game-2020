import os

# Remove existing documentation
os.system('rm -r docs/')

# Generate the documentation
os.system('pdoc --overwrite --html --html-dir docs/ --html-no-source botball')

# Move it to the top of the docs/ folder
os.system('mv docs/botball/* docs/')
os.system('rm -r docs/botball')
