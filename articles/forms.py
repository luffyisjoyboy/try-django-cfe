from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        query_set = Article.objects.filter(title__icontains=title)
        if query_set.exists():
            self.add_error('title', f"\"{title}\" Alreay in Use choose an other title")
        
        return data

# class ArticleFormOld(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField()

#     def clean_title(self):
#         cleaned_data = self.cleaned_data
#         title =  cleaned_data.get('title')
#         if title.lower().strip() == 'the office':
#             raise forms.ValidationError('title already taken')
#         print(title)
#         return title
    
#     def clean(self):
#         cleaned_data = self.cleaned_data
#         print('all data', cleaned_data)
#         title = cleaned_data.get('title')
#         content = cleaned_data.get("content")
#         if title.lower().strip() == "the office":
#             self.add_error('title', 'This title is taken.')
#             # raise forms.ValidationError('This title is taken.')
#         if "office" in content or "office" in title.lower():
#             self.add_error('content', "Office cannot be in content")
#             raise forms.ValidationError("Office is not allowed")
#         return cleaned_data