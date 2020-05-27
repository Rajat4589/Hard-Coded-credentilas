# Hard-Coded-credentilas and Web services using smart camera


Abstract: Internet of Things (IoT) is one of the emerging field of communication technology used in areas such as e-health, e-agriculture, smart cities, etc.
Along with the launch of most of IoT products, hard-coded credentials and web service approach of configuring these devices are vulnerable to many attacks
such as Mirai malware, weak havoc, etc. Access to IoT’s cshell service is one of the most severe flaws of hard-coded credentials. Hard-coded credentials
are nothing but, default login id and password used for initial configurations of IoT devices and further through the web. Some of the reasons for these
attacks include the availability of plain text hard-coded credentials on IoT devices provided by the manufacturers and a uniform pattern of these credentials
used in IoT devices which are manufactured by a single manufacturer. Unsecured web services is another issue in IoT devices which is responsible for
replay attack. The main reason for unsecured web services in IoT is compatibility with the existing protocol and unavailability of secure web applications
provided by the IoT manufacturers. This paper presents security issues and challenges of hard-coded credentials and web service in IoT.


# How to run?

open raspberry pi terminal

$ source ~/.profile

$ workon cv

$ cd Desktop

$ cd smart-camera

$ pip install -r requirments.txt

$ vim mail.py

$python main.py

$open browser 192.168.0.25:50000
