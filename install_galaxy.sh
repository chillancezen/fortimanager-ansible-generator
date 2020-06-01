#! /bin/bash
#GALAXY=/home/linky/Ansible/ansible-galaxy-fortimanager-collection

if [[ -z "${GALAXY}" ]]; then
     echo 'Environmental variable $GALAXY not set'
     exit 1
fi

galaxy_module_path=${GALAXY}/plugins/modules/
rm -f $galaxy_module_path/*

for mod in `cat module_list`;
do
    cp modules/$mod.py $galaxy_module_path
done

 
