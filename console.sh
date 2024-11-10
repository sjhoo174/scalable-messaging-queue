./kafka-console-consumer --bootstrap-server kafka-3:9096 --topic shopping --from-beginning

./kafka-console-producer --bootstrap-server localhost:9092 --topic shopping 

./kafka-topics --describe --topic shopping --bootstrap-server kafka-3:9096

./kafka-consumer-groups --bootstrap-server kafka-1:9092 --describe --group 

./kafka-consumer-groups --bootstrap-server kafka-1:9092 --list

