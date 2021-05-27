#! /bin/sh

do_download()
{
        mkdir -p $2
        while read -r line;
        do
        apipath=`echo $line |cut -d ' ' -f1`
        apihandler=`echo $line |cut -d ' ' -f2`
        apipath_urlencoded=`echo $line |cut -d ' ' -f3`
        apipath_filename=`echo $apipath | sed 's=/=.=g'`
        echo "downloading \e[4m$2/$apipath_filename.$apihandler.json\e[0m ..."
        ./request_schema.sh $apipath_urlencoded $apihandler > ./$2/$apipath_filename.$apihandler.json
        if [ ! $? -eq 0 ]; then
            echo "error downloading $apipath_filename.json"
        fi
    done < $1
}

for f in `ls top_level_apipath.metadata.*`
do
    schemas_path=`echo $f | sed 's/^top_level_apipath.metadata./schemas./g'`
    do_download $f $schemas_path
done
