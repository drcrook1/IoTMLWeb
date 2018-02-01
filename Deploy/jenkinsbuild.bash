# Part 1

WEB_IMAGE_NAME="iotml.azurecr.io/iotmlwebapp:kube${BUILD_NUMBER}"
docker build -t $WEB_IMAGE_NAME .
docker login iotml.azurecr.io -u iotml -p 3FjFUQK51wT/3TRXbHPjEmruCkGUUkFc
docker push $WEB_IMAGE_NAME

# Part 2
WEB_IMAGE_NAME="iotml.azurecr.io/iotmlwebapp:kube${BUILD_NUMBER}"
kubectl set image deployment/iotmlwebapp iotmlwebapp=$WEB_IMAGE_NAME --kubeconfig /var/lib/jenkins/config
