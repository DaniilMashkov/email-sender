from django.urls import path
from mailer.views import *
from mailer.apps import MailerConfig

app_name = MailerConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('manage/', DistributionListView.as_view(), name='manage'),
    path('distribution_form/', DistributionCreateView.as_view(), name='create'),
    path('update/<int:pk>/', DistributionUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', DistributionDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', DistributionDetailView.as_view(), name='detail'),
    path('your_messages/', MessageListView.as_view(), name='messages'),
    path('create_message_form/', MessageCreateView.as_view(), name='create_message'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('your_recipients/', RecipientListView.as_view(), name='recipients'),
    path('create_recipient_form/', RecipientCreateView.as_view(), name='create_recipient'),
    path('recipient_update/<int:pk>/', RecipientUpdateView.as_view(), name='recipient_update'),
    path('recipient_delete/<int:pk>/', RecipientDeleteView.as_view(), name='recipient_delete'),
]
