sudo apt install docker.io
sudo docker login iotml.azurecr.io -u iotml -p 3FjFUQK51wT/3TRXbHPjEmruCkGUUkFc
sudo gpasswd -a jenkins docker
sudo usermod -aG docker jenkins
sudo service jenkins restart

az aks install-cli
az aks-getcredentials --resource-group=dacrook-iotmlweb --name=dacrookiotmlcluster

sudo mkdir /var/lib/jenkins/.kube
sudo cp ~/.kube/config /var/lib/jenkins/.kube/config

git clone https://github.com/drcrook1/IoTMLWeb.git

cd IoTMLWeb
sudo docker build -t iotml.azurecr.io/iotmlwebapp ./WebApp
sudo docker push iotml.azurecr.io/iotmlwebapp

kubectl create secret docker-registry regsecret --docker-server=iotml.azurecr.io --docker-username=iotml --docker-password=3FjFUQK51wT/3TRXbHPjEmruCkGUUkFc --docker-email=dacrook@microsoft.com

kubectl create -f ./WebApp/webapp.yaml --record
