 node {
    def Mule_Version = ""
    def mavenSettingsFile='maven-mulesoft-settings'
    def workerType=''
	def workers=''
	def mvnHome=''
	def region=''
    def timeout='0'
    def gitUrl=''
    
  stage('Initialize') 
  {
    echo 'Configure maven directory and other initialize variables'
    workerType='Small'
    workers='1'
	Mule_Version = '4.3.0'
    region='us-west-2'
    timeout=2000000
    gitUrl='https://github.com/kunalkumarkundan31/CalculatorApp.git'
    mvnHome = tool 'MVN_HOME'
    deleteDir()
    echo "Mvn Directory " + mvnHome
	echo "Worker Type " + workerType
	echo "Number of Workers " + workers
	echo "Mule runtime version " + Mule_Version
	echo "Region selected " + region
	echo "Tiemout value " + timeout
  }
  
  stage('Checkout Source Code') 
  {
    echo 'Fetching the soure code'
	git branch: 'DEV', url: gitUrl
	
  }
  
   stage('Build') 
  {
      echo "Starting Build"
      def buildComm = mvnHome + '/bin' + '/mvn clean package -DskipTests'
      bat buildComm
  }
  
     stage('Munit Test') 
  {
      echo "Starting Munit testing"
      //skipping Munit testing
      def munitComm = mvnHome + '/bin' + '/mvn clean package'
      bat munitComm
  }
  
       stage('Apply Policy') 
  {
      echo "Applying Policy start"
	 bat pyPath + 'python policy.py --u kunalkumarkundan007 --p Dell@1234 --o 7b7f7c6d-fb9c-41fe-9a73-5eb790721add --e be057240-328d-49bc-bd67-fe03f012dd52 --at sample-policy --pp policy_config.json'
       
	  echo "Applying Policy finish"
  }
  stage('Deploy')
   {
    echo 'Deployment started'
    def jenkinsGlobalCredDev='anypointCredentials'
    withCredentials([
		                    usernamePassword(credentialsId: "${jenkinsGlobalCredDev}", passwordVariable: 'PASS', usernameVariable: 'USER'),
		                   ]) {
		                        echo USER
		                       echo PASS
		                       def deployComm = mvnHome + '/bin' + '/mvn deploy -DmuleDeploy' + ' -Danypoint.username=' + USER + ' -Danypoint.password=' + PASS 
                               bat deployComm
		                   }
   }
   
   stage('Cleanup') 
   {
      deleteDir()
   }
}
