from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>   Home Page   </h1> <h2>  <a href='page1/'>Page1</a>  ||    <a href='page2/'>Page2</a>  ||    <a href='page3/'>Page3</a>  ||    <a href='page4/'>Page4</a>  ||    <a href='page5/'>Page5</a>  </h2>")

def page1(request):
    return HttpResponse("<h1>   Page 1  </h1>   <h2>    <a href='/'>Back</a>    </h2>")

def page2(request):
    return HttpResponse("<h1>   Page 2  </h1>   <h2>    <a href='/'>Back</a>    </h2>")

def page3(request):
    return HttpResponse("<h1>   Page 3  </h1>   <h2>    <a href='/'>Back</a>    </h2>")

def page4(request):
    return HttpResponse("<h1>   Page 4  </h1>   <h2>    <a href='/'>Back</a>    </h2>")

def page5(request):
    return HttpResponse("<h1>   Page 5  </h1>   <h2>    <a href='/'>Back</a>    </h2>")
