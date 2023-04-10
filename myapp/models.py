from django.db import models

#BANK
class BA_Customers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ba_customers'


class BA_Accounts(models.Model):
    id = models.AutoField(primary_key=True)
    customerid = models.ForeignKey('BA_Customers', models.DO_NOTHING, db_column='customerid', blank=True, null=True)
    number = models.TextField(unique=True, blank=True, null=True)
    balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ba_accounts'


# DRUGSTORE
class DS_Customers(models.Model):
    name = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ds_customers'


class DS_Suppliers(models.Model):
    name = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ds_suppliers'


class DS_Storage(models.Model):
    item = models.TextField(unique=True, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    supplierid = models.ForeignKey('DS_Suppliers', models.DO_NOTHING, db_column='supplierid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ds_storage'


class DS_Prescriptions(models.Model):
    id = models.AutoField(primary_key=True)
    customerid = models.ForeignKey('DS_Customers', models.DO_NOTHING, db_column='customerid', blank=True, null=True)
    item = models.ForeignKey('DS_Storage', models.DO_NOTHING, db_column='item', to_field='item', blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ds_prescriptions'


# GYM
class GY_Customers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    membership_start = models.DateField(blank=True, null=True)
    membership_end = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gy_customers'


class GY_Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    hire_date= models.DateField(blank=True, null=True)
    salary = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shiftid = models.ForeignKey('GY_Shifts', models.DO_NOTHING, db_column='shiftid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gy_staff'


class GY_Shifts(models.Model):
    id = models.AutoField(primary_key=True)
    start = models.DateField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    workhours = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gy_shifts'


#PRAYER
class PR_Prayer(models.Model):
    name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    denomination = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pr_prayer'


# RESIDENCE
class RE_Apartments(models.Model):
    id = models.AutoField(primary_key=True)
    building_name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    apartment_number = models.IntegerField(blank=True, null=True)
    number_of_rooms = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    monthly_rent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    occupied = models.BooleanField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 're_apartments'


class RE_Houses(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.TextField(blank=True, null=True, unique=True)
    number_of_rooms = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    monthly_rent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    occupied = models.BooleanField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 're_houses'


class RE_Residents(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.TextField(blank=True, null=True)
    family_name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=1, choices=[('M', 'M'), ('F', 'F')], blank=True, null=True)    
    occupation = models.TextField(blank=True, null=True)
    religion = models.TextField(blank=True, null=True)
    property_type = models.TextField(blank=True, null=True)
    propertyid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 're_residents'


# SCHOOL
class SC_Courses(models.Model):
    name = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    teacherid = models.ForeignKey('SC_Teachers', models.DO_NOTHING, db_column='teacherid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sc_courses'


class SC_Enrollments(models.Model):
    studentid = models.ForeignKey('SC_Students', models.DO_NOTHING, db_column='studentid', null=True, blank=True)
    courseid = models.ForeignKey('SC_Courses',  models.DO_NOTHING,  db_column='courseid', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'sc_enrollments'


class SC_LibraryBooks(models.Model):
    title = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    genre = models.TextField(blank=True, null=True)
    isbn = models.TextField(blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sc_library_books'


class SC_LibraryLoans(models.Model):
    id = models.AutoField(primary_key=True)
    memberid = models.ForeignKey('SC_LibraryMembers', models.DO_NOTHING, db_column='memberid', blank=True, null=True)
    bookid = models.ForeignKey('SC_LibraryBooks', models.DO_NOTHING, db_column='bookid', blank=True, null=True)
    borrowed_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sc_library_loans'


class SC_LibraryMembers(models.Model):
    name = models.TextField(blank=True, null=True)
    age = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sc_library_members'


class SC_Students(models.Model):
    name = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sc_students'


class SC_Teachers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sc_teachers'


#SUPERMARKET
class SM_Employees(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    salary = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    functionid = models.ForeignKey('SM_Functions', models.DO_NOTHING, db_column='functionid', blank=True, null=True)
    shiftid = models.ForeignKey('SM_Shifts', models.DO_NOTHING, db_column='shiftid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sm_employees'


class SM_Functions(models.Model):
    name = models.TextField(blank=True, null=True)
    workload = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sm_functions'


class SM_Shifts(models.Model):
    id = models.AutoField(primary_key=True)
    start = models.DateField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    workhours = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sm_shifts'


class SM_Inventory(models.Model):
    item = models.TextField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    entry_date = models.DateField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    kosher = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sm_inventory'





