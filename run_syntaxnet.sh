#!/usr/bin/env bash

if [ "$1" == "" ]; then
echo "Error: enter input filename"
exit 1
fi

if [ "$2" == "" ]; then
echo "Error: enter output filename"
exit 1
fi

if [ "$3" == "" ]; then
echo "Error: enter models path"
exit 1
fi

workDir=$(pwd)
cd ~/Python_libs/models/syntaxnet


cat $workDir/$1 | $3/parsey_universal/parse.sh $3/Russian-SynTagRus > $workDir/$2
