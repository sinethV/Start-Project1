from django.contrib import admin
from .models import computer
#add new model in class foreinge key
from django.contrib import admin
from .models import School, Student, Teacher, Class

# last finish

from.models import car
from .models import Person
from .models import Branch
from .models import Staff

admin.site.register(Person)


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
admin.site.register(computer, ComputerAdmin)
class CarAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'YearMade')

    # your_app/admin.py


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branchNo', 'branchAddress', 'telNo')  # Fields to display in the list view
    search_fields = ('branchNo', 'branchAddress')  # Fields to search
    list_filter = ('branchNo',)  # Filters for the sidebar

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staffNo', 'name', 'position', 'salary', 'branch')  # Fields to display
    search_fields = ('name', 'staffNo', 'position')  # Fields to search
    list_filter = ('position', 'branch')  # Filters for the sidebar
#add admin for register in admin panel

admin.site.register(car, CarAdmin)



# Create a School
school1 = School.objects.create(studentname="ABC School", address="123 Street", yearStudy=2024)

# Create a Student linked to that School
student1 = Student.objects.create(studentID=school1, name="John Doe", age=15)

# Create a Teacher linked to that School
teacher1 = Teacher.objects.create(name="Ms. Smith", subject="Math", schoolID=school1)

# Create a Class linked to School & Teacher
class1 = Class.objects.create(classname="Math Class", schoolID=school1, TeacherID=teacher1)

# Display Data
print(student1.name, "studies at", student1.studentID.studentname)
print(teacher1.name, "teaches", teacher1.subject, "at", teacher1.schoolID.studentname)
print(class1.classname, "is taught by", class1.TeacherID.name)


#add admin for store informations
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)


# Register your models here.
