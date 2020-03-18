if [ "$1" == "" ]; then
    echo
    echo "usage: $(basename $0) [-t] NUMBER"
    echo
    echo "    print a psalm in Chinese, translated by Joseph."
    echo "       -t     Show Title"
    exit
fi

HERE=$(dirname $(grealpath $0))
RAW=${HERE}/__raw__
mkdir -p ${RAW}

function url    { echo https://www.bible.com/ur/bible/2296/PSA.${1} ; }
function raw    { echo ${RAW}/psalm.${1}.html ; }

if [ "$1" == "-t" ]; then
    echo "________________Psalm $2________________"
    shift
fi
[ -f $(raw $1)    ] ||  wget --waitretry 10 -c $(url $1) -O $(raw $1)

python3 parse.py $(raw $1)

