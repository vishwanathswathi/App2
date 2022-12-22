from django.shortcuts import render
import datetime
def wishes3(request):
    date1=datetime.datetime.now()
    msg1='Hello User/Client...GOOD';
    hr=int(date1.strftime('%H'));
    imgs='image1.jpg';
    if hr<12:
        msg1+=' Morning!!'
        imgs = 'image1.jpg';
    elif hr<16:
        msg1+=' Afternoon!!'
        imgs = 'image2.jpg';
    elif hr<20:
        msg1+=' Evening!!'
        imgs = 'image3.jpg';
    else:
        msg1='Hello User/Client...Very Good Night!!'
        imgs = 'image4.jpg';
    dict1={'date1':date1,'msg1':msg1,'imgs':imgs}
    return render(request,'FirstApp/wishes3.html',context=dict1);