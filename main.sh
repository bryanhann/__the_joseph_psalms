if [ "$1" == "" ]; then
    echo
    echo "usage: $(basename $0) <book> <chapter>"
    echo
    echo "    print a bible chapter in Chinese, translated by Joseph."
    exit
fi

_export () { export $1=$2 ; }

_export short   ${1}.${2}
_export long    ${1}.$(printf "%.3d" ${2})
_export HERE    $(dirname $(grealpath ${0}))
_export BUILD   ${HERE}/.B
_export URL     https://www.bible.com/ur/bible/2296
_export RAW     ${BUILD}/raw
_export COO     ${HERE}/parsed
_export url     ${URL}/${short}
_export raw     ${RAW}/${short}
_export coo     ${COO}/${long}.txt

mkdir -p ${RAW}
mkdir -p ${COO}
[ ! -f $coo ] && [ ! -f $raw ] && wget --waitretry 10 -c $url -O $raw
[ ! -f $coo ] && python3 parse.py $raw > $coo
cat $coo




