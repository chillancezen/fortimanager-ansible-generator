
PWD=`pwd`
cp $PWD/common.py /usr/local/lib/python3.6/dist-packages/ansible/module_utils/network/fortimanager
ln -sf $PWD/modules  /usr/local/lib/python3.6/dist-packages/ansible/modules/network/fortimanager/generated_modules


