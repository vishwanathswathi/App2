from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    print("welcome/ url is requested & display() is executed");
    ss='''
            <center>
             <h2 style='color:Blue;'>
                Hello User,Welcome to Django First project First-App
             </h2>
             <hr/>
            </center>
        '''
    return HttpResponse(ss);
    
def show(request):
    ss='''<!--
           Html webpage to display"welcome-msg" with diff headings
           -->
           <html>
           <head>
           <title>**welocme-page**</title>
           <style>
           h1{
           	color:pink;
           }
           h2{
           	color:blue;
           }
           h3{
           	color:lightgreen;
           }
           h4{
           	color:red;
           }
           h5{
           	color:blue;
           }
           h6{
           	color:green;
           }
           h1,h2,h3{
           background:gray;
           }
           h4,h5,h6{
           background:orange
           }
           
           </style>
           </head>
           <body>
           <center>
           <h1>welcome to django html webpage</h1>
           <hr color="brown" width="80%"/>
           <h2>welcome to django html webpage</h2>
           <hr  color="brown" width="70%"/>
           <h3>welcome to django html webpage</h3>
           <hr color="brown" width="60%"/>
           <h4>welcome to django html webpage</h4>
           <hr color="brown" width="50%"/>
           <h5>welcome to django html webpage</h5>
           <hr  color="brown" width="40%"/>
           <h6>welcome to django html webpage</h6>
           <hr  color="brown" width="30%"/>
           </body>
           </html>
        ''';
    return HttpResponse(ss);
def hello(request):
    ss='''
           <!--
           Html webpage to display"welcome-msg" with diff headings
           -->
           <html>
           <head>
           <title>**welocme-page**</title>
           <style>
           h1{
           	color:pink;
           }
           h2{
           	color:blue;
           }
           h3{
           	color:lightgreen;
           }
           h4{
           	color:red;
           }
           h5{
           	color:blue;
           }
           h6{
           	color:green;
           }
           h1,h2,h3{
           background:gray;
           }
           h4,h5,h6{
           background:orange
           }
           
           </style>
           </head>
           <body>
           <center>
           <h1>welcome to django html webpage</h1>
           <hr color="brown" width="80%"/>
           <h2>welcome to django html webpage</h2>
           <hr  color="brown" width="70%"/>
           <h3>welcome to django html webpage</h3>
           <hr color="brown" width="60%"/>
           <h4>welcome to django html webpage</h4>
           <hr color="brown" width="50%"/>
           <h5>welcome to django html webpage</h5>
           <hr  color="brown" width="40%"/>
           <h6>welcome to django html webpage</h6>
           <hr  color="brown" width="30%"/>
           </body>
           </html>
          
       ''';
    return HttpResponse(ss);
import time;
def senddatetime(request):
    ct=time.ctime()
    print("dtime/ url is requested & senddatetime() is executed");
    ss='''
	<html>
		<head>
			<title>Date-time Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightgreen;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Welcome to DJango-User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Server-Date & Time :: </h2>
				<hr color='brown' width='70%'/>
				<h3>''',ct,'''</h3>
				<hr color='brown' width='60%'/>
			</center>
		</body>
	</html>
	''';
    return HttpResponse(ss);
def demo(request):   
	print("mulitple-Requests-URLs same respose");
	htmldata='''<center>
		<h1>Welcome Demo User!!!</h1>
		<hr />
		<h2>This is Same-Output for diff-mulitple-Requests-URLs</h2>
		<hr />
		<h3>Have a Great Day...</h3>
		</center>''';
	return HttpResponse(htmldata);

def homepage(request):
    htmldata='''<center>
        <h1>Welcome to DEFAULT Home-Page!!!</h1>
        <hr />
        <h2>Your Request Page is Not-Found...</h2>
        <hr />
        <h3>Plz try other URL or Links!!!</h3>
    </center>''';
    return HttpResponse(htmldata);


    


    