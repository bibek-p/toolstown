from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Blogs
import json

@api_view(['POST'])
def headcheck(request):
    heading_request=request.data["heading_request"]
    page_details=Blogs.objects.filter(original_heading=heading_request)
    if len(page_details)==0:
        return Response(1)
    else:
        return Response(0)



def createpost(request):
        req=request.data
        post=Blogs()
        original_heading=req['original_heading']
        original_heading=original_heading.strip()
        post.original_heading= original_heading
        post.blog_heading= req['blog_heading']
        
        post.blog_image= req['blog_image']
        post.publish_date= str(datetime.today().strftime("%b %d %Y"))
        post.content_source= req['content_source']
        blog_heading=req['blog_heading']
        twwet_quote=req["twwet_quote"]
        twwet_quote=twwet_quote.split("===>")
        
        blog_heading=blog_heading.replace(",","")
        blog_heading=blog_heading.replace('"',"-")
        blog_heading=blog_heading.replace("'","")
        blog_heading=blog_heading.replace(".","")
        blog_heading=blog_heading.replace("?","")
        blog_heading=blog_heading.replace(" ","-")
        blog_heading=blog_heading.replace("/","")
        blog_heading=blog_heading.replace("\'","")

        if blog_heading[0]=="-":
            blog_heading = blog_heading[1:]
        if blog_heading[-1]=="-":
            blog_heading = blog_heading[:-1]

        post.link= blog_heading.lower()
        text=req['blog_content']
        text=text.split(".")
        print("===>",text)
        thing="Likewise READ:"
        for i in range(len(text)):
            if len(text) > i:
                sentense=text[i]
                if thing in sentense:
                    text.remove(sentense)

        round_para_n=round(len(text)/8)
        mainpara=""
        for i in range(1,round_para_n+1):
            first_list=text[(i-1)*8:i*8]
            para=".".join(first_list)
            if i != 1:
                if i <=len(twwet_quote):
                    mainpara=mainpara+".<br>"+twwet_quote[i]+"<br>"+para
                    del twwet_quote[i]
                else:
                    mainpara=mainpara+".<br><br>"+para
            else:
                mainpara=para
        restpara=text[round_para_n*8::]
        restpara="".join(restpara)
        mainpara=mainpara+".<br><br>"+restpara+" ."
        if len(twwet_quote) >0:
            for m in range(len(twwet_quote)):
                mainpara=mainpara+twwet_quote[m]
        post.blog_content= mainpara
        post.keyword=req['keywords']
        post.category=req['category']
        post.save()
        return Response("====> Added New post")
