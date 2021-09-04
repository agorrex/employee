from django.conf.urls import url, include

from .views import EmployeesListView, EmployeeCreateView, EmployeeDeleteView, EmployeeEditView, EmployeeDetailView

urlpatterns = [
    url(r'^$', EmployeesListView.as_view(), name='list'),
    url(r'^add/$', EmployeeCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', EmployeeEditView.as_view(), name='edit'),
    url(r'^delete/(?P<pk>[0-9]+)/$', EmployeeDeleteView.as_view(), name='delete'),
    url(r'^detail/(?P<pk>[0-9]+)/$', EmployeeDetailView.as_view(), name='detail'),

]