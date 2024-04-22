# NOTE: Replace the path to the data file with the correct path

# Remove bracketed content, convert to lowercase, find reduplications, and output in tab-separated format
cat $1 | sed -re 's/[[(].*[])]//g' | sed -e 's/\(.*\)/\L\1/' | egrep '\b([a-z]{3,})[ -]\1\b' | sed -re 's/(.*\b)([a-z]+ ?[a-z]*)([ -])\2(\b.*)/\2\t\1\2\3\2\4/g'

# OLD REGEX (allows multiple words and short words): egrep '\b([a-z]+ ?[a-z]*)[ -]\1\b'
# OLDER REGEX: egrep -i '\b(.*\w+.*),?[ -]+\1\b'
# Filtering out (some) double hyphens: sed -re 's/--/-/g'