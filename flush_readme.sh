#!/bin/sh
echo """# 刷题喽~

  本工程单纯用来维护刷题的代码，自娱自乐~
""" > ./README.md

for f in *.py;
do
     if [[ $f =~ ^[0-9]{1,}.*.py ]]
     then
        echo "Add to README: ${f%.*}"
        echo "### ${f%.*}" >> ./README.md
     else
        echo "skipped: $f"
     fi
done
