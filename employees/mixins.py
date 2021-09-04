from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings


class UserLoginRequiredMixin(LoginRequiredMixin):
    login_url = settings.LOGIN_URL

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_employee:
            return self.handle_no_permission()
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)