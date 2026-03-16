# army_test_2

The goal of the project is to build a system that receives 3 types of messages 
1 about intelligence information
2 about the air force attack
3 about the results of the attack
I saw fit to enter every intelligence event that is received directly into the Mongo database (if it is not there and if so, update missing fields if there are any)
And every time a certain piece of data arrives, for example about an air force attack or information about the result of an attack, I update the field that you are reporting and add data to it so that everything is concentrated in one place
To run the project, you need to "docker compose up" in the main project folder.

I also added a Kafka UI container so you can see the messages in a nice and organized way.