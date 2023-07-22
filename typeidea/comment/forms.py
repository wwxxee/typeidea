from django import forms
from captcha.fields import CaptchaField
from .models import Comment
import mistune


class CommentForm(forms.ModelForm):



    nickname = forms.CharField(
        label='昵称',
        max_length=20,
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': 'width: 60%;'}
        )
    )
    email = forms.CharField(
        label='email',
        max_length=50,
        widget=forms.widgets.EmailInput(
            attrs={'class': 'form-control', 'style': 'width: 60%;'}
        )
    )
    # website = forms.CharField(
    #     label='网站',
    #     max_length=25,
    #     widget=forms.widgets.URLInput(
    #         attrs={'class': 'form-control', 'style': 'width: 60%;'}
    #     )
    # )

    content = forms.CharField(
        label='内容',
        max_length=50,
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': 'width: 60%;'}
        )
    )

    captcha = CaptchaField(label='请输入验证码：')

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('内容长度太短啦！！')
        content = mistune.markdown(content)
        return content

    class Meta:
        model = Comment
        fields = [
            'nickname', 'email', 'content'
        ]
