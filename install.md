
docker run -it -d --name test_rabitt -p 15672:15672 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=magicQ -e RABBITMQ_DEFAULT_PASS=onlineQfortesting2022 rabbitmq:3.11-management