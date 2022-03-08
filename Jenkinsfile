node {
  stage('Preparation') {
    echo 'Fetching the code'
    def mvnHome = tool 'MVN_HOME'
    def comm = mvnHome + '/bin' 
    echo comm
  }
  
    stage('Checkout Source Code') {
    echo 'Fetching the code'
	git branch: 'devBranch', url: 'https://github.com/kunalkumarkundan31/Calculator.git'
    def mvnHome = tool 'MVN_HOME'
    def comm = mvnHome + '/bin' 
    echo comm
  }
    stage('Build') {
    echo 'Build the code'
    def mvnHome = tool 'MVN_HOME'
    def comm1 = mvnHome + '/bin' + '/mvn clean package -DskipTests'
     echo comm1
   bat comm1
  }
   
   
   stage('Munit Test') {
    echo 'Munit Testing'
    def mvnHome = tool 'MVN_HOME'
    def comm1 = mvnHome + '/bin' + '/mvn clean package'
    echo comm1
   bat comm1
  }
  
    stage('Deploy cloudHub') {
    echo 'Munit Testing'
    def mvnHome = tool 'MVN_HOME'
    def comm1 = mvnHome + '/bin' + '/mvn deploy -Dmule.version=4.3.0 -DmuleDeploy -Ddeployment=cloudhub -Danypoint.username=kunalkumarkundan007 -Danypoint.password=Dell@1234'
    echo comm1
    
   bat comm1
  }
}
