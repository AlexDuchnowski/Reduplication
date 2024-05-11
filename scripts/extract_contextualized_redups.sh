# The whole enchilada of processing subtitle data for reduplication

name=$(echo $1 | rev | cut -d "/" -f1 | rev | cut -d "." -f1)

mkdir data/$name

python3 scripts/context.py $1 > data/$name/contextualized_$name.txt  # add context to each line of input

echo "Created Contextualized File: data/$name/contextualized_$name.txt"

tab=$'\t'   # tab character for egrep use

# Remove bracketed content, convert to lowercase, find reduplications, and output in tab-separated format
cat data/$name/contextualized_$name.txt                 |
grep -vP '^[^\t]*\b([a-z]{3,})[ ,-]+\1[ ,-]+\1\b'       |   # remove rows with triples in the first column
sed -re 's/^([^\t]*)([[\(].*[]\)])(.*)\2/\1\3/g'        |   # remove bracketed content in the first column
sed -re 's/^([^\t]*)/\L\1/'                             |   # convert text in the first column to lowercase
egrep "^[^$tab]*\b([a-z]{3,})[ ,-]\1\b"                 |   # filter for reduplications in the first column
sed -re 's/^[^\t]*\b([a-z]{3,})[ ,-]\1\b[^\t]*\t/\1\t/g'   `# extract reduplicated words in the first column` \
> data/$name/${name}_redups.txt

echo "Created Reduplications File: data/$name/${name}_redups.txt"

python3 scripts/pos_filter.py data/$name/${name}_redups.txt