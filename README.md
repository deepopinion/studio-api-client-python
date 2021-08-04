# studio-api-client-python

## Python client for the Studio API

Built via swagger code-gen v2

   git clone https://github.com/swagger-api/swagger-codegen.git
   git checkout v2.4.21
   sudo apt-get install maven  # install maven > 3.3
   sudo apt-get install openjdk-8-jdk  # install java 8 and active it
   sudo update-alternatives ---config java  # activate java 8
   cd swagger-codegen
   mvn clean package  # compile
   java -jar modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate \
   -i https://api.deepopinion.ai/apispec_1.json \
   -l python \
   -o ../studio-api-python-client
