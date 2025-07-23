# Hello, CI/CD

Aplicação simples, usada como base para projeto de CI/CD

## Entregas do Projeto

### Build e push da imagem no Docker Hub

![](./screenshots/dockerhub-repo.png)
*Repositório com imagens enviadas via workflow*

### Atualização automática do manifest

![](./screenshots/pr-files-changed.png)
*Informação de arquivos alterados no PR*

### Argo CD sincronizado com o app

![](./screenshots/argocd-app.png)
*UI do Argo com informações do deploy local após rolling update*

### App em execução no cluster local

![](./screenshots/kubectl-get-all.png)
*Deployment, Service, ReplicaSets e Pods do cluster filtrados por label*

### Acessando App

![](./screenshots/localhost-browser.png)
*Requisição HTTP via browser*

![](./screenshots/localhost-curl.png)
*Requisição HTTP via curl*
