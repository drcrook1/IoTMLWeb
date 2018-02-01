az aks create ^
--resource-group dacrook-iotmlweb ^
--name=dacrookiotmlcluster ^
--generate-ssh-keys ^
--node-count=2 ^
--node-vm-size=Standard_D1_v2
