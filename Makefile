.PHONY: modules
modules:
	@echo '[Generate] modules'
	@python3 generate.py
test: modules
	@echo '[Install] Local Galaxy collection'
	@rm -f ~/.ansible/collections/ansible_collections/fortinet/fortimanager/plugins/modules/*
	@cp modules/* ~/.ansible/collections/ansible_collections/fortinet/fortimanager/plugins/modules
	@cp galaxy_template/fmgr_generic.py ~/.ansible/collections/ansible_collections/fortinet/fortimanager/plugins/modules
