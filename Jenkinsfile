node {
    def Mule_Version = "4.3.0"
    
  stage('Preparation') {
    echo 'Fetching the code'
    def mvnHome = tool 'MVN_HOME'
    def comm = mvnHome + '/bin' 
   def workerType='Small'
   def workers='1'

   def region='us-west-2'
   def timeout=2000000
    echo comm
	
	def get = new URL("https://httpbin.org/get").openConnection();
def getRC = get.getResponseCode();
println(getRC);
if(getRC.equals(200)) {
    println(get.getInputStream().getText());
}
  }
}
