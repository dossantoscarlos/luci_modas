from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy
class CustomSite(AdminSite):
    site_header = 'Brecho Luci'
    site_title =  gettext_lazy('Brecho Luci')
    
    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)

        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])
            app['models'].reverse()

        return app_list
    