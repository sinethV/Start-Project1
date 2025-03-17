from django.db import models


#add values in model for store information 
#like : name, price, quantity, image

class computer(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='computer_images/', blank=True, null=True)
    # other fields...

    def __str__(self):
        return self.name
    
class car(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    YearMade = models.IntegerField()
    Image = models.URLField(max_length=200)

class Ford(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    YearMade = models.IntegerField()
    Image = models.URLField(max_length=200)
    Brand = models.CharField(max_length=100)  
    from django.db import models

class Person(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    HOBBY_CHOICES = [
        ('Swimming', 'Swimming'),
        ('Reading', 'Reading'),
        ('Biking', 'Biking'),
        ('Other', 'Other'),
    ]

    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Khmer', 'Khmer'),
        ('French', 'French'),
        ('Other', 'Other'),
    ]

   

    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    hobby = models.CharField(max_length=20, choices=HOBBY_CHOICES)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    image = models.ImageField(upload_to='images/')
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    #Martial_Status = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    photo = models.ImageField(upload_to='images/')

    def str(self):
        return self.name
    

 




class Branch(models.Model):
    branchNo = models.CharField(max_length=10, primary_key=True)
    branchAddress = models.CharField(max_length=255)
    telNo = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.branchNo} - {self.branchAddress}"

class Staff(models.Model):
    staffNo = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    salary = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='staff_members')

    def __str__(self):
        return f"{self.name} - {self.position} (Branch: {self.branch.branchNo})"
    

    

class School(models.Model):
    studentID = models.AutoField(primary_key=True)
    studentname = models.CharField(max_length=100)
    address = models.TextField()
    yearStudy = models.IntegerField()

    def __str__(self):
        return self.studentname

class Student(models.Model):
    studentID = models.OneToOneField(School, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    TeacherID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    schoolID = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Class(models.Model):
    classID = models.AutoField(primary_key=True)
    classname = models.CharField(max_length=100)
    schoolID = models.ForeignKey(School, on_delete=models.CASCADE)
    TeacherID = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.classname


# Optional: Create the database tables
# You can run these commands in your Django project after setting up:
# python manage.py makemigrations
# python manage.py migrate