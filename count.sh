#!/bin/bash

# checks if file already exists; if not it downloads it
if [[ ! -f 'README' ]]
then
	wget ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README
fi

# read file
cat README |
# put to lower case and remove punctuation
tr [:upper:] [:lower:] | tr -d [:punct:] |
# separate into words every line
sed "s/ /\n/g" |
# remove digits and then remove empty lines
sed 's/^ *[0-9]//' | sed '/^$/d' |
# sort alphabetically
sort |
# get count of words and unify
uniq -c |
# sort numerical (put most common words on top)
sort -n -r |
# remove number-output from unique
sed 's/^ *[0-9]\+ //' |
# take the first 10 words
head -10
