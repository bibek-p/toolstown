from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from blog.models import Blogs



class LatestPostsFeed(Feed):
    title = 'World News Headlines, Latest International News, World Breaking News - ToolsBand'
    link = '/blog'
    description = 'World News: ToolsBand news brings the latest world news headlines, Current International breaking news world wide. In depth analysis and top news headlines world wide.'

    def items(self):
        return Blogs.objects.all()[:20]

    def item_title(self, item):
        return item.blog_heading

    def item_link(self, item):
        mlink=item.link
        mlink="/blog/news/"+mlink
        return mlink

    def item_description(self, item):
        dec = truncatewords(item.blog_content, 30)
        dec = dec[:-1]
        img='<img border="0" hspace="10" align="left" style="margin-top:3px;margin-right:5px;" src="'+item.blog_image+'" />'
        return img+dec

    