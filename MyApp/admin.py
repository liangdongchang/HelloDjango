from django.contrib import admin

# Register your models here.
from MyApp.models import Grade, Students


class StudentInfo(admin.TabularInline):
    model = Students
    extra = 2

# admin.site.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('gname','gdate','ggirlnum')
    list_filter = ('gdate',)
    list_per_page = 3
    search_fields = ('gname',)

    inlines = [StudentInfo]

# admin.site.register(Grade)
class StudentAdmin(admin.ModelAdmin):

    def getGender(self):
        if self.sgender == True:
            return '男'
        else:
            return '女'
    getGender.short_description = '性别'
    list_display = ('sname',getGender,'sage','sinfo','sgrade')



class MySite(admin.AdminSite):

    site_title = '管理系统'
    site_header = '学生管理系统'
    site_url = '/welcome'

mysite = MySite()

# admin.site.register(Grade,GradeAdmin)
# admin.site.register(Students,StudentAdmin)
mysite.register(Grade,GradeAdmin)
mysite.register(Students,StudentAdmin)