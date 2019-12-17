#! /bin/sh

if [ ! $# -eq 1 ]; then
    echo "please specify top level path metadata file"
    exit 1
fi


while read -r line;
do
    apipath=`echo $line |cut -d ' ' -f1`
    apihandler=`echo $line |cut -d ' ' -f2`
    apipath_urlencoded=`echo $line |cut -d ' ' -f3`
    apipath_filename=`echo $apipath | sed 's=/=.=g'`
    echo "downloading $apipath_filename.json ..."
    ./request_schema.sh $apipath_urlencoded $apihandler > ./schemas/$apipath_filename.$apihandler.json
    if [ ! $? -eq 0 ]; then
        echo "error downloading $apipath_filename.json"
    fi
done < $1
