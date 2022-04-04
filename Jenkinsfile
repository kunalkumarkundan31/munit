node {
	    //Env specific variables
	def appName= 'CalcJen2'
	def workerType='Small'
	def workers='1'
	def region='us-west-2'
	def envProp= 'dev'
	def gitUrl='https://github.com/kunalkumarkundan31/CalculatorApp.git'
	def environment ='Sandbox'
	def orgId = '7b7f7c6d-fb9c-41fe-9a73-5eb790721add'
	def envId='be057240-328d-49bc-bd67-fe03f012dd52'
	def apiName='sample-policy'
	//def apiName=''
	
	
	// System variables
	def timeout=2000000
	def mvnHome=''
	def businessGroup=''
	def autoDiscoveryId=''
	def policyConfigFile='policy_config.json'
	def jenkinsGlobalCredDev='anypointCredentials'

  stage('Initialize') 
  {
    echo 'Configure maven directory and other initialize variables'
    
    mvnHome = tool 'MVN_HOME'
    deleteDir()
    echo "Mvn Directory " + mvnHome
    echo "Application Name " + appName
    echo "Worker Type " + workerType
    echo "Number of Workers " + workers
    echo "Region selected " + region
    echo "Env Property "  + envProp
    echo "GIT URL "  + gitUrl
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
  
  if(apiName != '')
    {
  
    stage('Apply Policy') 
     {
      try 
      {
      echo "Applying Policy start"
      withCredentials([usernamePassword(credentialsId: "${jenkinsGlobalCredDev}", passwordVariable: 'PASS', usernameVariable: 'USER')])
         	{
	   def pyPath1= 'python policy.py --u ' + USER + ' --p ' + PASS + ' --o '+ orgId + ' --e '+ envId + ' --at ' + apiName + ' --pp ' + policyConfigFile
       def pyPath2= pyPath + pyPath1
       bat pyPath2
       autoDiscoveryId = readFile(file: 'tempid.txt')
       echo autoDiscoveryId
	}
      }
      catch (Exception e)
      {
          echo "Auto Dsicovery ID IS not found or some other error occurred"
           if(apiName != '' && autodiscoveryId == '')
                {
                     throw new Exception("Autodiscovery Id is missing, please check if apiName is present")
                  }
      }
  }
    }

  stage('Deploy')
   {
    echo 'Deployment started'
    
    withCredentials([
		                    usernamePassword(credentialsId: "${jenkinsGlobalCredDev}", passwordVariable: 'PASS', usernameVariable: 'USER'),
		                   ]) {
		                     
                             def deployComm = mvnHome + '/bin' + '/mvn deploy -DmuleDeploy -DskipTests -Ddeployment=cloudhub ' + ' -Dusername=' + USER + ' -Dpassword=' + PASS + ' -DbusinessGroup='+businessGroup+ ' -Denvironment=' + environment + ' -DworkerType=' + workerType + ' -Dworkers=' + workers + ' -Dregion='+ region + ' -DappName='+ appName + ' -Dtimeout=' +timeout + ' -Denv=' + environment + ' -Denv='+ envProp + ' -DautoDiscoveryId='+ autoDiscoveryId 
                              echo deployComm
                              
                              bat deployComm
		                   }
   }
   
   stage('Cleanup') 
   {
      deleteDir()
   }
}
