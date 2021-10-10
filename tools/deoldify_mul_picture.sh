#!/bin/bash
#same as the python variant but without chances of crashes

mkdir -p $3
for FILE in $1/*;
do
	echo python3 deoldify_picture.py $FILE $2 $3/$(basename $FILE)
	python3 deoldify_picture.py $FILE $2 $3/$(basename $FILE)
done
