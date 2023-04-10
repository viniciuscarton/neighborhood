from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.http import JsonResponse
import os
from .models import SM_Inventory
from .models import SM_Functions
from .models import SM_Shifts
from .models import SM_Employees
from .models import RE_Houses
from .models import RE_Apartments
from .models import RE_Residents
from .models import PR_Prayer
from .models import BA_Customers
from .models import BA_Accounts
from .models import DS_Customers
from .models import DS_Suppliers
from .models import DS_Storage
from .models import DS_Prescriptions
from .models import GY_Customers
from .models import GY_Shifts
from .models import GY_Staff
from .models import SC_Students
from .models import SC_Teachers
from .models import SC_Courses
from .models import SC_Enrollments
from .models import SC_LibraryBooks
from .models import SC_LibraryMembers
from .models import SC_LibraryLoans

def index(request):
    counts = {
        '🧔 Residents 🧔': RE_Residents.objects.using('residencies').count(),
        '🎓 Students 🎓': SC_Students.objects.using('default').count(),
        '📖 Library Loans 📖': SC_LibraryLoans.objects.using('default').count(),
        '💸 Bank Accounts 💸': BA_Accounts.objects.using('bank').count(),
        '🛒 Supermarket Inventory 🛒': SM_Inventory.objects.using('supermarket').count(),
        '💊 Drugstore Customers 💊': DS_Customers.objects.using('drugstore').count(),
        '🤸 Gym Memberships 🤸': GY_Customers.objects.using('gym').count(),
    }
    return render(request, 'index.html', {'counts': counts})

# SUPERMARKET INVENTORY
def sm_add_inventory(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        entry_date = request.POST.get('entry_date')
        exp_date = request.POST.get('exp_date')
        kosher = request.POST.get('kosher') == 'on'
        SM_Inventory.objects.using('supermarket').create(
            item=item,
            quantity=quantity,
            entry_date=entry_date,
            exp_date=exp_date,
            kosher=kosher
        )
        return redirect('index')

def sm_delete_inventory(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        SM_Inventory.objects.using('supermarket').filter(id=id).delete()
        return redirect('index')
    
def sm_read_inventory(request):
    inventory = SM_Inventory.objects.using('supermarket').order_by('id')
    context = {'inventory':inventory}
    return render(request, 'read_templates/sm_read_inventory.html', context)

def sm_edit_inventory(request):
    if request.method == 'POST':
        id = request.POST['id']
        inventory = SM_Inventory.objects.using('supermarket').get(id=id)

        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        entry_date = request.POST.get('entry_date')
        exp_date = request.POST.get('exp_date')
        kosher = request.POST.get('kosher') == 'on'

        if item:
            inventory.item = item
        if quantity:
            inventory.quantity = quantity
        if entry_date:
            inventory.entry_date = entry_date
        if exp_date:
            inventory.exp_date = exp_date
        inventory.kosher = kosher
        inventory.save()
        return redirect('index')

    context = {}
    return render(request,'', context)

# SUPERMARKET FUNCTIONS
def sm_add_functions(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        workload = request.POST.get('workload')
        location = request.POST.get('location')

        SM_Functions.objects.using('supermarket').create(
            name=name,
            workload=workload,
            location=location,
        )
        return redirect('index')

def sm_delete_functions(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        SM_Functions.objects.using('supermarket').filter(id=id).delete()
        return redirect('index')
    
def sm_read_functions(request):
    functions = SM_Functions.objects.using('supermarket').order_by('id')
    context = {'functions': functions}
    return render(request, 'read_templates/sm_read_functions.html', context)

def sm_edit_functions(request):
    if request.method == 'POST':
        id = request.POST['id']
        function = SM_Functions.objects.using('supermarket').get(id=id)

        name = request.POST.get('name')
        workload = request.POST.get('workload')
        location = request.POST.get('location')

        if name:
            function.name = name
        if workload:
            function.workload = workload
        if location:
            function.location = location
        function.save()

        return redirect('index')

    context = {}
    return render(request,'', context)

# SUPERMARKET SHIFTS
def sm_add_shifts(request):
    if request.method == 'POST':
        start = request.POST.get('start')
        hour = request.POST.get('hour')
        workhours = request.POST.get('workhours')

        SM_Shifts.objects.using('supermarket').create(
            start=start,
            hour=hour,
            workhours=workhours,
        )
        return redirect('index')

def sm_delete_shifts(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        SM_Shifts.objects.using('supermarket').filter(id=id).delete()
        return redirect('index')
    
def sm_read_shifts(request):
    shifts = SM_Shifts.objects.using('supermarket').order_by('id')
    context = {'shifts': shifts}
    return render(request, 'read_templates/sm_read_shifts.html', context)

def sm_edit_shifts(request):
    if request.method == 'POST':
        id = request.POST['id']
        shifts = SM_Shifts.objects.using('supermarket').get(id=id)

        id = request.POST.get('id')
        start = request.POST.get('start')
        hour = request.POST.get('hour')
        workhours = request.POST.get('workhours')

        if id:
            shifts.id = id
        if start:
            shifts.start = start
        if hour:
            shifts.hour = hour
        if workhours:
           shifts.workhours = workhours
        shifts.save()

        return redirect('index')

    context = {}
    return render(request,'', context)

# SUPERMARKET EMPLOYEES
def sm_add_employees(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        hire_date = request.POST.get('hire_date')
        salary = request.POST.get('salary')
        functionid = request.POST.get('functionid')
        shiftid = request.POST.get('shiftid')

        function_instance = SM_Functions.objects.using('supermarket').get(id=functionid)
        shift_instance = SM_Shifts.objects.using('supermarket').get(id=shiftid)

        SM_Employees.objects.using('supermarket').create(
            name=name,
            age=age,
            phone=phone,
            hire_date=hire_date,
            salary=salary,
            functionid=function_instance,
            shiftid=shift_instance
        )
        return redirect('index')

def sm_delete_employees(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        SM_Employees.objects.using('supermarket').filter(id=id).delete()
        return redirect('index')
    
def sm_read_employees(request):
    employees = SM_Employees.objects.using('supermarket').order_by('id')
    context = {'employees': employees}
    return render(request, 'read_templates/sm_read_employees.html', context)

def sm_edit_employees(request):

    if request.method == 'POST':
        id = request.POST['id']
        employees= SM_Employees.objects.using('supermarket').get(id=id)

        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        hire_date = request.POST.get('hire_date')
        salary = request.POST.get('salary')
        functionid = request.POST.get('functionid')
        shiftid = request.POST.get('shiftid')

        if name:
            employees.name = name
        if age:
            employees.age = age
        if phone:
            employees.phone = phone
        if hire_date:
            employees.hire_date = hire_date
        if salary:
            employees.salary = salary
        if functionid:
            function_instance = SM_Functions.objects.using('supermarket').get(id=functionid)
            employees.functionid = function_instance
        if shiftid:
            shift_instance = SM_Shifts.objects.using('supermarket').get(id=shiftid)
            employees.shiftid = shift_instance
        employees.save()
        return redirect('index')
    context = {}
    return render(request,'', context)

# RESIDENCIES HOUSES
def re_add_houses(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        number_of_rooms = request.POST.get('number_of_rooms')
        area = request.POST.get('area')
        monthly_rent = request.POST.get('monthly_rent')
        occupied = request.POST.get('occupied') == 'on'

        RE_Houses.objects.using('residencies').create(
            address = address,
            number_of_rooms = number_of_rooms,
            area = area,
            monthly_rent = monthly_rent,
            occupied = occupied,
        )
        return redirect('index')

def re_read_houses(request):
    houses = RE_Houses.objects.using('residencies').order_by('id')
    context = {'houses': houses}
    return render(request, 'read_templates/re_read_houses.html', context)

def re_delete_houses(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        RE_Houses.objects.using('residencies').filter(id=id).delete()
        return redirect('index')

def re_edit_houses(request):
    if request.method == 'POST':
        id = request.POST['id']
        houses= RE_Houses.objects.using('residencies').get(id=id)

        address = request.POST.get('address')
        number_of_rooms = request.POST.get('number_of_rooms')
        area = request.POST.get('area')
        monthly_rent = request.POST.get('monthly_rent')
        occupied = request.POST.get('occupied')  == 'on'

        if address:
            houses.address = address
        if number_of_rooms:
            houses.number_of_rooms = number_of_rooms
        if area:
            houses.area = area
        if monthly_rent:
            houses.monthly_rent = monthly_rent
        houses.occupied = occupied
        houses.save()
        return redirect('index')

    context = {}
    return render(request,'', context)

# RESIDENCIES APARTMENTS
def re_add_apartments(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        building_name = request.POST.get('building_name')
        apartment_number = request.POST.get('apartment_number')
        number_of_rooms = request.POST.get('number_of_rooms')
        area = request.POST.get('area')
        monthly_rent = request.POST.get('monthly_rent')
        occupied = request.POST.get('occupied') == 'on'

        RE_Apartments.objects.using('residencies').create(
            address = address,
            building_name = building_name,
            apartment_number =  apartment_number,
            number_of_rooms = number_of_rooms,
            area = area,
            monthly_rent = monthly_rent,
            occupied = occupied,
        )
        return redirect('index')

def re_read_apartments(request):
    apartments = RE_Apartments.objects.using('residencies').order_by('id')
    context = {'apartments':apartments}
    return render(request, 'read_templates/re_read_apartments.html', context)

def re_delete_apartments(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        RE_Apartments.objects.using('residencies').filter(id=id).delete()
        return redirect('index')

def re_edit_apartments(request):
    if request.method == 'POST':
        id = request.POST['id']
        apartments= RE_Apartments.objects.using('residencies').get(id=id)

        address = request.POST.get('address')
        building_name = request.POST.get('building_name')
        apartment_number = request.POST.get('apartment_number')
        number_of_rooms = request.POST.get('number_of_rooms')
        area = request.POST.get('area')
        monthly_rent = request.POST.get('monthly_rent')
        occupied = request.POST.get('occupied') == 'on'

        if address:
            apartments.address = address
        if building_name:
            apartments.building_name = building_name
        if apartment_number:
            apartments.apartment_number = apartment_number
        if number_of_rooms:
            apartments.number_of_rooms = number_of_rooms
        if area:
            apartments.area = area
        if monthly_rent:
            apartments.monthly_rent = monthly_rent
        apartments.occupied = occupied
        apartments.save()
        return redirect('index')

    context = {}
    return render(request,'', context)

# RESIDENCIES RESIDENTS
def re_add_residencies(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        family_name = request.POST.get('family_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        occupation = request.POST.get('occupation')
        religion = request.POST.get('religion')
        property_type = request.POST.get('property_type')
        propertyid = request.POST.get('propertyid')

        if property_type == 'house':
            if not RE_Houses.objects.using('residencies').filter(id=propertyid).exists():
                return HttpResponse('Invalid house ID')
        elif property_type == 'apartment':
            if not RE_Apartments.objects.using('residencies').filter(id=propertyid).exists():
                return HttpResponse('Invalid apartment ID')

        RE_Residents.objects.using('residencies').create(
            first_name = first_name,
            family_name = family_name,
            email = email,
            phone = phone,
            age = age,
            sex = sex,
            occupation = occupation,
            religion = religion,
            property_type = property_type,
            propertyid = propertyid
        )
        return redirect('index')

def re_read_residencies(request):
    residents = RE_Residents.objects.using('residencies').order_by('id')
    context = {'residents':residents}
    return render(request, 'read_templates/re_read_residents.html', context)

def re_delete_residencies(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        RE_Residents.objects.using('residencies').filter(id=id).delete()
        return redirect('index')

def re_edit_residencies(request):
    if request.method == 'POST':
        id = request.POST['id']
        residents= RE_Residents.objects.using('residencies').get(id=id)

        first_name = request.POST.get('first_name')
        family_name = request.POST.get('family_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        occupation = request.POST.get('occupation')
        religion = request.POST.get('religion')
        property_type = request.POST.get('property_type')
        propertyid = request.POST.get('propertyid')
 
        if first_name:
            residents.first_name = first_name
        if family_name:
            residents.family_name = family_name
        if email:
            residents.email = email
        if phone:
            residents.phone = phone
        if age:
            residents.age= age
        if sex:
            residents.sex= sex
        if occupation:
            residents.occupation = occupation
        if religion:
            residents.religion= religion
        if property_type:
             residents.property_type = property_type
        if propertyid:
             residents.propertyid = propertyid

        residents.save()
        return redirect('index')

    context = {}
    return render(request,'', context)

# PRAYER
def pr_add_prayer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        denomination = request.POST.get('denomination')
        
        PR_Prayer.objects.using('prayer').create(
            name = name,
            address = address,
            denomination = denomination,
        )
        return redirect('index')

def pr_read_prayer(request):
    prayer = PR_Prayer.objects.using('prayer').order_by('id')
    context = {'prayer':prayer}
    return render(request, 'read_templates/pr_read_prayer.html', context)

def pr_delete_prayer(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        PR_Prayer.objects.using('prayer').filter(id=id).delete()
        return redirect('index')

def pr_edit_prayer(request):
    if request.method == 'POST':
        id = request.POST['id']
        prayer = PR_Prayer.objects.using('prayer').get(id=id)

        name = request.POST.get('name')
        address = request.POST.get('address')
        denomination = request.POST.get('denomination')
 
        if name:
            prayer.name = name
        if address:
            prayer.address = address
        if denomination:
           prayer.denomination = denomination

        prayer.save()
        return redirect('index')

    context = {}
    return render(request, '', context)

# BANK CUSTOMERS
def ba_add_customers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')

        BA_Customers.objects.using('bank').create(
            name=name,
            age=age,
            address=address,
        )
        return redirect('index')

def ba_delete_customers(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        BA_Customers.objects.using('bank').filter(id=id).delete()
        return redirect('index')
    
def ba_read_customers(request):
    customers = BA_Customers.objects.using('bank').order_by('id')
    context = {'customers': customers}
    return render(request, 'read_templates/ba_read_customers.html', context)

def ba_edit_customers(request):
     if request.method == 'POST':
        id = request.POST['id']
        customers= BA_Customers.objects.using('bank').get(id=id)

        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
 
        if name:
            customers.name = name
        if age:
            customers.age= age
        if address:
           customers.address = address

        customers.save()
        return redirect('index')

        context = {}
        return render(request,'', context)

# BANK ACCOUNTS
def ba_add_accounts(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        balance = request.POST.get('balance')
        customerid = request.POST.get('customerid')
        customer_instance = BA_Customers.objects.using('bank').get(id=customerid)

        BA_Accounts.objects.using('bank').create(
            number=number,
            balance=balance,
            customerid=customer_instance,
        )
        return redirect('index')

def ba_delete_accounts(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        BA_Accounts.objects.using('bank').filter(id=id).delete()
        return redirect('index')
    
def ba_read_accounts(request):
    accounts = BA_Accounts.objects.using('bank').order_by('id')
    context = {'accounts': accounts}
    return render(request, 'read_templates/ba_read_accounts.html', context)

def ba_edit_accounts(request):
     if request.method == 'POST':
        id = request.POST['id']
        accounts = BA_Accounts.objects.using('bank').get(id=id)

        number = request.POST.get('number')
        balance = request.POST.get('balance')
        customerid = request.POST.get('customerid')
 
        if number:
            accounts.number= number
        if balance:
            accounts.balance= balance
        if customerid:
           customer_instance = BA_Customers.objects.using('bank').get(id=customerid)
           accounts.customerid = customer_instance

        accounts.save()
        return redirect('index')

        context = {}
        return render(request,'', context)

# DRUGSTORE CUSTOMERS
def ds_add_customers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        DS_Customers.objects.using('drugstore').create(
            name = name,
            age = age, 
            address = address,
            phone = phone,
        )
        return redirect('index')

def ds_delete_customers(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        DS_Customers.objects.using('drugstore').filter(id=id).delete()
        return redirect('index')
    
def ds_read_customers(request):
    customers = DS_Customers.objects.using('drugstore').order_by('id')
    context = {'customers': customers}
    return render(request, 'read_templates/ds_read_customers.html', context)

def ds_edit_customers(request):
     if request.method == 'POST':
        id = request.POST['id']
        customers= DS_Customers.objects.using('drugstore').get(id=id)

        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
 
        if name:
           customers.name= name
        if age:
           customers.age= age
        if address:
           customers.address = address
        if phone:
            customers.phone = phone

        customers.save()
        return redirect('index')

        context = {}
        return render(request,'', context)

# DRUGSTORE SUPPLIERS
def ds_add_suppliers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        DS_Suppliers.objects.using('drugstore').create(
            name = name,
            phone = phone,
            email = email,
        )
        return redirect('index')

def ds_delete_suppliers(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        DS_Suppliers.objects.using('drugstore').filter(id=id).delete()
        return redirect('index')
    
def ds_read_suppliers(request):
    suppliers = DS_Suppliers.objects.using('drugstore').order_by('id')
    context = {'suppliers': suppliers}
    return render(request, 'read_templates/ds_read_suppliers.html', context)

def ds_edit_suppliers(request):
     if request.method == 'POST':
        id = request.POST['id']
        supplier= DS_Suppliers.objects.using('drugstore').get(id=id)

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
 
        if name:
           supplier.name= name
        if phone:
            supplier.phone = phone
        if email:
            supplier.email = email

        supplier.save()
        return redirect('index')

        context = {}
        return render(request,'', context)

# DRUGSTORE STORAGE
def ds_add_storage(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        exp_date = request.POST.get('exp_date')
        supplierid = request.POST.get('supplierid')
        supplier_instance = DS_Suppliers.objects.using('drugstore').get(id=supplierid)

        DS_Storage.objects.using('drugstore').create(
            item = item,
            quantity = quantity,
            exp_date = exp_date,
            supplierid = supplier_instance
        )
        return redirect('index')

def ds_delete_storage(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        DS_Storage.objects.using('drugstore').filter(id=id).delete()
        return redirect('index')
    
def ds_read_storage(request):
    storage = DS_Storage.objects.using('drugstore').order_by('id')
    context = {'storage': storage}
    return render(request, 'read_templates/ds_read_storage.html', context)

def ds_edit_storage(request):
     if request.method == 'POST':
        id = request.POST['id']
        storage= DS_Storage.objects.using('drugstore').get(id=id)

        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        exp_date = request.POST.get('exp_date')
        supplierid = request.POST.get('supplierid')
        supplier_instance = DS_Suppliers.objects.using('drugstore').get(id=supplierid)
 
        if item:
           storage.item= item
        if quantity:
            storage.quantity = quantity
        if exp_date:
            storage.exp_date = exp_date
        if supplierid:
            supplier_instance = DS_Suppliers.objects.using('drugstore').get(id=supplierid)
            storage.supplierid = supplier_instance

        storage.save()
        return redirect('index')

        context = {}
        return render(request,'', context)

# DRUGSTORE PRESCRIPTIONS
def ds_add_prescriptions(request):
    if request.method == 'POST':
        customerid = request.POST.get('customerid')
        customer_instance = DS_Customers.objects.using('drugstore').get(id=customerid)
        item = request.POST.get('item')
        item_instance = DS_Storage.objects.using('drugstore').get(item=item)
        quantity = request.POST.get('quantity')
        date = request.POST.get('date')
        

        DS_Prescriptions.objects.using('drugstore').create(
            customerid = customer_instance,
            item = item_instance,
            quantity = quantity,
            date = date,
        )
        return redirect('index')

def ds_delete_prescriptions(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        DS_Prescriptions.objects.using('drugstore').filter(id=id).delete()
        return redirect('index')
    
def ds_read_prescriptions(request):
    prescriptions = DS_Prescriptions.objects.using('drugstore').order_by('id')
    context = {'prescriptions': prescriptions}
    return render(request, 'read_templates/ds_read_prescriptions.html', context)

def ds_edit_prescriptions(request):
     if request.method == 'POST':
        id = request.POST['id']
        prescriptions = DS_Prescriptions.objects.using('drugstore').get(id=id)

        customerid = request.POST.get('customerid')
        customer_instance = DS_Customers.objects.using('drugstore').get(id=customerid)
        item = request.POST.get('item')
        item_instance = DS_Storage.objects.using('drugstore').get(item=item)
        quantity = request.POST.get('quantity')
        date = request.POST.get('date')
 
        if customerid:
            customer_instance = DS_Customers.objects.using('drugstore').get(id=customerid)
            prescriptions.customerid = customer_instance
        if item:
            item_instance = DS_Storage.objects.using('drugstore').get(item=item)
            prescriptions.item = item_instance
        if quantity:
            prescriptions.quantity = quantity
        if date:
            prescriptions.date = date

        prescriptions.save()
        return redirect('index')

        context = {}
        return render(request,'', context)

# GYM CUSTOMERS
def gy_add_customers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        membership_start = request.POST.get('membership_start')
        membership_end = request.POST.get('membership_start')

        GY_Customers.objects.using('gym').create(
            name = name,
            age = age, 
            membership_start = membership_start,
            membership_end = membership_end,
        )
        return redirect('index')

def gy_delete_customers(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        GY_Customers.objects.using('gym').filter(id=id).delete()
        return redirect('index')
   
def gy_read_customers(request):
    customers = GY_Customers.objects.using('gym').order_by('id')
    context = {'customers': customers}
    return render(request, 'read_templates/gy_read_customers.html', context)

def gy_edit_customers(request):
     if request.method == 'POST':
        id = request.POST['id']
        customers = GY_Customers.objects.using('gym').get(id=id)

        name = request.POST.get('name')
        age = request.POST.get('age')
        membership_start = request.POST.get('membership_start')
        membership_end = request.POST.get('membership_start')
 
        if name:
            customers.name = name
        if age:
            customers.age = age
        if membership_start:
            customers.membership_start = membership_start
        if membership_end:
            customers.membership_end = membership_end

        customers.save()
        return redirect('index')

        context = {}
        return render(request,'', context)

# GYM SHIFTS
def gy_add_shifts(request):
    if request.method == 'POST':
        start = request.POST.get('start')
        hour = request.POST.get('hour')
        workhours = request.POST.get('workhours')

        GY_Shifts.objects.using('gym').create(
            start = start,
            hour = hour,
            workhours = workhours,
        )
        return redirect('index')

def gy_delete_shifts(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        GY_Shifts.objects.using('gym').filter(id=id).delete()
        return redirect('index')
    
def gy_read_shifts(request):
    shifts = GY_Shifts.objects.using('gym').order_by('id')
    context = {'shifts': shifts}
    return render(request, 'read_templates/gy_read_shifts.html', context)

def gy_edit_shifts(request):
     if request.method == 'POST':
        id = request.POST['id']
        shifts = GY_Shifts.objects.using('gym').get(id=id)

        start = request.POST.get('start')
        hour = request.POST.get('hour')
        workhours = request.POST.get('workhours')
 
        if start:
            shifts.start = start
        if hour:
            shifts.hour = hour
        if workhours:
            shifts.workhours = workhours

        shifts.save()
        return redirect('index')

        context = {}
        return render(request,'', context)

# GYM STAFF
def gy_add_staff(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        hire_date = request.POST.get('hire_date')
        salary = request.POST.get('salary')
        shiftid = request.POST.get('shiftid')
        shift_instance = GY_Shifts.objects.using('gym').get(id=shiftid)

        GY_Staff.objects.using('gym').create(
            name = name,
            age = age,
            hire_date = hire_date,
            salary = salary,
            shiftid = shift_instance
        )
        return redirect('index')

def gy_delete_staff(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        GY_Staff.objects.using('gym').filter(id=id).delete()
        return redirect('index')
    
def gy_read_staff(request):
    staff = GY_Staff.objects.using('gym').order_by('id')
    context = {'staff': staff}
    return render(request, 'read_templates/gy_read_staff.html', context)

def gy_edit_staff(request):
     if request.method == 'POST':
        id = request.POST['id']
        staff = GY_Staff.objects.using('gym').get(id=id)

        name = request.POST.get('name')
        age = request.POST.get('age')
        hire_date = request.POST.get('hire_date')
        salary = request.POST.get('salary')
        shiftid = request.POST.get('shiftid')
        shift_instance = GY_Shifts.objects.using('gym').get(id=shiftid)

        if name:
            staff.name = name
        if age:
            staff.age = age
        if hire_date:
            staff.hire_date = hire_date
        if salary:
            staff.salary = salary
        if shiftid:
            shift_instance = GY_Shifts.objects.using('gym').get(id=shiftid)
            staff.shiftid = shift_instance

        staff.save()
        return redirect('index')

        context = {}
        return render(request,'', context)

# SCHOOL STUDENTS
def sc_add_students(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        address = request.POST.get('address')

        SC_Students.objects.create(
            name = name,
            age = age,
            grade = grade,
            address = address,
        )
        return redirect('index')

def sc_delete_students(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        SC_Students.objects.filter(id=id).delete()
        return redirect('index')
    
def sc_read_students(request):
    students = SC_Students.objects.order_by('id')
    context = {'students': students}
    return render(request, 'read_templates/sc_read_students.html', context)

def sc_edit_students(request):
     if request.method == 'POST':
        id = request.POST['id']
        students = SC_Students.objects.get(id=id)

        name = request.POST.get('name')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        address = request.POST.get('address')

        if name:
            students.name = name
        if age:
            students.age = age
        if grade:
            students.grade = grade
        if address:
            students.address = address

        students.save()
        return redirect('index')

        context = {}
        return render(request,'', context)

# SCHOOL TEACHERS
def sc_add_teachers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        SC_Teachers.objects.create(
            name = name,
            age = age,
            email = email,
        )
        return redirect('index')

def sc_delete_teachers(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        SC_Teachers.objects.filter(id=id).delete()
        return redirect('index')
    
def sc_read_teachers(request):
    teachers =  SC_Teachers.objects.order_by('id')
    context = {'teachers': teachers}
    return render(request, 'read_templates/sc_read_teachers.html', context)

def sc_edit_teachers(request):
     if request.method == 'POST':
        id = request.POST['id']
        teachers = SC_Teachers.objects.get(id=id)

        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        if name:
            teachers.name = name
        if age:
            teachers.age = age
        if email:
            teachers.grade = email

        teachers.save()
        return redirect('index')

        context = {}
        return render(request,'', context)

# SCHOOL COURSES
def sc_add_courses(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')
        teacherid = request.POST.get('teacherid')
        teacher_instance = SC_Teachers.objects.get(id=teacherid)
        
        SC_Courses.objects.create(
            name = name,
            code = code,
            teacherid = teacher_instance,
        )
        return redirect('index')

def sc_delete_courses(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        SC_Courses.objects.filter(id=id).delete()
        return redirect('index')
    
def sc_read_courses(request):
    courses = SC_Courses.objects.order_by('id')
    context = {'courses': courses}
    return render(request, 'read_templates/sc_read_courses.html', context)

def sc_edit_courses(request):
     if request.method == 'POST':
        id = request.POST['id']
        courses = SC_Courses.objects.get(id=id)

        name = request.POST.get('name')
        code = request.POST.get('code')
        teacherid = request.POST.get('teacherid')
        teacher_instance = SC_Teachers.objects.get(id=teacherid)

        if name:
            courses.name = name
        if code:
            courses.code = code
        if teacherid:
            teacher_instance = SC_Teachers.objects.get(id=teacherid)
            courses.teacherid = teacher_instance

        courses.save()
        return redirect('index')

        context = {}
        return render(request,'', context)     

# SCHOOL ENROLLMENT
def sc_add_enrollments(request):
    if request.method == 'POST':
        studentid = request.POST.get('studentid')
        courseid = request.POST.get('courseid')
        student_instance = SC_Students.objects.get(id=studentid)
        course_instance = SC_Courses.objects.get(id=courseid)

        SC_Enrollments.objects.create(
            studentid = student_instance,
            courseid = course_instance,
        )
        return redirect('index')

def sc_delete_enrollments(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        SC_Enrollments.objects.filter(id=id).delete()
        return redirect('index')
    
def sc_read_enrollments(request):
    enrollments = SC_Enrollments.objects.order_by('id')
    context = {'enrollments': enrollments}
    return render(request, 'read_templates/sc_read_enrollments.html', context)

def sc_edit_enrollments(request):
     if request.method == 'POST':
        id = request.POST['id']
        enrollments = SC_Enrollments.objects.get(id=id)

        studentid = request.POST.get('studentid')
        courseid = request.POST.get('courseid')
        student_instance = SC_Students.objects.get(id=studentid)
        course_instance = SC_Courses.objects.get(id=courseid)

        if studentid:
            student_instance = SC_Students.objects.get(id=studentid)
            enrollments.studentid = student_instance
        if courseid:
            course_instance = SC_Courses.objects.get(id=courseid)
            enrollments.courseid = course_instance

        enrollments.save()
        return redirect('index')

        context = {}
        return render(request,'', context)          

# SCHOOL LIBRARY BOOKS
def sc_add_librarybooks(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        isbn = request.POST.get('isbn')
        publication_date = request.POST.get('publication_date')

        SC_LibraryBooks.objects.create(
            title = title,
            author = author,
            genre = genre,
            isbn = isbn,
            publication_date = publication_date
        )
        return redirect('index')

def sc_delete_librarybooks(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        SC_LibraryBooks.objects.filter(id=id).delete()
        return redirect('index')
    
def sc_read_librarybooks(request):
    librarybooks = SC_LibraryBooks.objects.order_by('id')
    context = {'librarybooks': librarybooks}
    return render(request, 'read_templates/sc_read_librarybooks.html', context)

def sc_edit_librarybooks(request):
     if request.method == 'POST':
        id = request.POST['id']
        librarybooks = SC_LibraryBooks.objects.get(id=id)

        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        isbn = request.POST.get('isbn')
        publication_date = request.POST.get('publication_date')

        if title:
            librarybooks.title = title
        if author:
            librarybooks.author = author
        if genre:
            librarybooks.genre = genre
        if isbn:
            librarybooks.isbn = isbn
        if publication_date:
            librarybooks.publication_date = publication_date
  
        librarybooks.save()
        return redirect('index')

        context = {}
        return render(request,'', context) 

# SCHOOL LIBRARY MEMBERS
def sc_add_librarymembers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        SC_LibraryMembers.objects.create(
            name = name,
            age = age,
            address = address,
            phone = phone,
        )
        return redirect('index')

def sc_delete_librarymembers(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        SC_LibraryMembers.objects.filter(id=id).delete()
        return redirect('index')
    
def sc_read_librarymembers(request):
    librarymembers = SC_LibraryMembers.objects.order_by('id')
    context = {'librarymembers': librarymembers}
    return render(request, 'read_templates/sc_read_librarymembers.html', context)

def sc_edit_librarymembers(request):
     if request.method == 'POST':
        id = request.POST['id']
        librarymembers = LibraryMembers.objects.get(id=id)

        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        if name:
            librarymembers.name = name
        if age:
            librarymembers.age = age
        if address:
            librarymembers.address = address
        if phone:
            librarymembers.phone = phone
  

        librarymembers.save()
        return redirect('index')

        context = {}
        return render(request, 'update_school_librarymembers.html', context)   

# SCHOOL LIBRARY LOANS
def sc_add_libraryloans(request):
    if request.method == 'POST':
        memberid = request.POST.get('memberid')
        member_instace = SC_LibraryMembers.objects.get(id=memberid)
        bookid = request.POST.get('bookid')
        book_instace = SC_LibraryBooks.objects.get(id=bookid)
        borrowed_date = request.POST.get('borrowed_date')
        return_date = request.POST.get('return_date')

        SC_LibraryLoans.objects.create(
            memberid = member_instace,
            bookid = book_instace,
            borrowed_date = borrowed_date,
            return_date = return_date,
        )
        return redirect('index')

def sc_delete_libraryloans(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        SC_LibraryLoans.objects.filter(id=id).delete()
        return redirect('index')
    
def sc_read_libraryloans(request):
    libraryloans = SC_LibraryLoans.objects.order_by('id')
    context = {'libraryloans': libraryloans}
    return render(request, 'read_templates/sc_read_libraryloans.html', context)

def sc_edit_libraryloans(request):
     if request.method == 'POST':
        id = request.POST['id']
        libraryloans = SC_LibraryLoans.objects.get(id=id)

        memberid = request.POST.get('memberid')
        member_instace = SC_LibraryMembers.objects.get(id=memberid)
        bookid = request.POST.get('bookid')
        book_instace = SC_LibraryBooks.objects.get(id=bookid)
        borrowed_date = request.POST.get('borrowed_date')
        return_date = request.POST.get('return_date')

        if memberid:
            libraryloans.memberid = member_instace
        if bookid:
            libraryloans.bookid = book_instace
        if borrowed_date:
            libraryloans.borrowed_date = borrowed_date
        if return_date:
            libraryloans.return_date = return_date

        libraryloans.save()
        return redirect('index')

        context = {}
        return render(request,'', context)  
