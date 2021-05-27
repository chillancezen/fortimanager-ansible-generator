#COOKIE='ips4_device_key=b6881f156e528cfcdd5ec75b50df742a; CookieScriptConsent={"action":"accept"}; ips4_ipsTimezone=Asia/Shanghai; ips4_hasJS=true; ips4_IPSSessionFront=d9gri210bk1udold1ahc88c28k; ips4_member_id=16887; ips4_login_key=0c5758a06ca36521c1b8fc308a83ed91'

#CSRFKEY=17e36557be95960dbba2097636a0cd8e

if [ ! $# -eq 2 ]; then
    echo "Please speficy the API path and handler"
    exit 1
fi
APIPATH=$1
APIHANDLER=$2
FORMDATA="csrfKey=$CSRFKEY&handler=$APIHANDLER&path=$APIPATH&filter=&host=&comparison=0&favourites=0&favedata="
APIURL="https://fndn.fortinet.net/index.php?app=apicompare&module=apis&controller=apis&id=5&name=fortimanager&do=getAPIData"


curl -s -X POST "$APIURL" -H "Cookie: $COOKIE" -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With: XMLHttpRequest" -d $FORMDATA
