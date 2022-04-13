from django.contrib import admin
from .models import Blog,Contact,Service,Slider,Project,Testimonial,Author

admin.site.register (Blog)
admin.site.register(Project)
admin.site.register(Testimonial)
admin.site.register(Slider)
admin.site.register(Contact)
admin.site.register(Author)
admin.site.register(Service)