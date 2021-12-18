from django.urls import path
from . import views
urlpatterns = [
    path("text-to-uppercase",views.text_to_uppercase,name="Text To Upper Case"),
    path("text-to-lowercase",views.text_to_lowercase,name="Text To Lower Case"),
    path("text-to-capitalize",views.text_to_capitalize,name="Text To Capitalize"),
    path("word-count",views.word_count,name="Word Count"),
    path("clean-space",views.remove_space,name="Clean Space"),
    path("remove-space",views.remove_space,name="Remove Space"),
    path("replace-text",views.replace_text,name="Replace Text"),
    path("text-reverse",views.text_reverse,name="Text Reverse"),
    path("repeat-text",views.repeat_text,name="Repeat Text"),
]