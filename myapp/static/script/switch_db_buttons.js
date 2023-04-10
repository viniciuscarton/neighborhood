// SUPERMARKET
const inventoryDiv = document.getElementById("SM-INVENTORY");
const functionsDiv = document.getElementById("SM-FUNCTIONS");
const shiftsDiv = document.getElementById("SM-SHIFTS");
const employeesDiv = document.getElementById("SM-EMPLOYEES");

const btnInventory = document.getElementById("btn-inventory");
const btnFunctions = document.getElementById("btn-functions");
const btnShifts = document.getElementById("btn-shifts");
const btnEmployees = document.getElementById("btn-employees");

btnInventory.addEventListener("click", function () {
    inventoryDiv.style.display = "block";
    functionsDiv.style.display = "none";
    shiftsDiv.style.display = "none";
    employeesDiv.style.display = "none"
});
btnFunctions.addEventListener("click", function () {
    inventoryDiv.style.display = "none";
    functionsDiv.style.display = "block";
    shiftsDiv.style.display = "none";
    employeesDiv.style.display = "none"
});
btnShifts.addEventListener("click", function () {
    inventoryDiv.style.display = "none";
    functionsDiv.style.display = "none";
    shiftsDiv.style.display = "block";
    employeesDiv.style.display = "none"
})
btnEmployees.addEventListener("click", function () {
    inventoryDiv.style.display = "none";
    functionsDiv.style.display = "none";
    shiftsDiv.style.display = "none";
    employeesDiv.style.display = "block"
})
// hide divs
functionsDiv.style.display = "none";
shiftsDiv.style.display = "none";
employeesDiv.style.display = "none";

// RESIDENCIES
const houseDiv = document.getElementById("RE-HOUSES");
const apartmentDiv = document.getElementById("RE-APARTMENTS");
const residentDiv = document.getElementById("RE-RESIDENTS");

const btnHouse = document.getElementById("btn-house");
const btnApartment = document.getElementById("btn-apartment");
const btnResident = document.getElementById("btn-resident");

btnHouse.addEventListener("click", function () {
    houseDiv.style.display = "block";
    apartmentDiv.style.display = "none";
    residentDiv.style.display = "none";
})

btnApartment.addEventListener("click", function () {
    houseDiv.style.display = "none";
    apartmentDiv.style.display = "block";
    residentDiv.style.display = "none";
})

btnResident.addEventListener("click", function () {
    houseDiv.style.display = "none";
    apartmentDiv.style.display = "none";
    residentDiv.style.display = "block";
})

// hide divs
apartmentDiv.style.display = "none";
residentDiv.style.display = "none";

// BANK
const customerDiv = document.getElementById("BA-CUSTOMERS");
const accountDiv = document.getElementById("BA-ACCOUNTS");

const btnCustomer = document.getElementById("btn-customer");
const btnAccount = document.getElementById("btn-account");

btnCustomer.addEventListener("click", function () {
    customerDiv.style.display = "block";
    accountDiv.style.display = "none";
})
btnAccount.addEventListener("click", function () {
    customerDiv.style.display = "none";
    accountDiv.style.display = "block";
})

// // hide divs
accountDiv.style.display = "none";

// DRUGSTORE 
const DS_customerDiv = document.getElementById("DS-CUSTOMERS");
const DS_prescriptionsDiv = document.getElementById("DS-PRESCRIPTIONS");
const DS_storageDiv = document.getElementById("DS-STORAGE");
const DS_suppliersDiv = document.getElementById("DS-SUPPLIERS");

const btnDS_Customer = document.getElementById("btn-customers");
const btnDS_Prescriptions = document.getElementById("btn-prescription");
const btnDS_Storage = document.getElementById("btn-storage");
const btnDS_Suppliers = document.getElementById("btn-supplier");

btnDS_Customer.addEventListener("click", function () {
    DS_customerDiv.style.display = "block";
    DS_prescriptionsDiv.style.display = "none";
    DS_storageDiv.style.display = "none";
    DS_suppliersDiv.style.display = "none";
})

btnDS_Storage.addEventListener("click", function () {
    DS_customerDiv.style.display = "none";
    DS_prescriptionsDiv.style.display = "none";
    DS_storageDiv.style.display = "block";
    DS_suppliersDiv.style.display = "none";
})

btnDS_Suppliers.addEventListener("click", function () {
    DS_customerDiv.style.display = "none";
    DS_prescriptionsDiv.style.display = "none";
    DS_storageDiv.style.display = "none";
    DS_suppliersDiv.style.display = "block";
})

btnDS_Prescriptions.addEventListener("click", function () {
    DS_customerDiv.style.display = "none";
    DS_prescriptionsDiv.style.display = "block";
    DS_storageDiv.style.display = "none";
    DS_suppliersDiv.style.display = "none";
})

// hide the divs
DS_prescriptionsDiv.style.display = "none";
DS_storageDiv.style.display = "none";
DS_suppliersDiv.style.display = "none";

// GYM
const GY_customersDiv = document.getElementById("GY-CUSTOMERS");
const GY_shiftsDiv = document.getElementById("GY-SHIFTS");
const GY_staffDiv = document.getElementById("GY-STAFF");

const btnGY_Customers = document.getElementById("btn-gy-customers");
const btnGY_Shifts = document.getElementById("btn-gy-shifts");
const btnGY_Staff = document.getElementById("btn-gy-staff");

btnGY_Customers.addEventListener("click", function () {
    GY_customersDiv.style.display = "block";
    GY_shiftsDiv.style.display = "none";
    GY_staffDiv.style.display = "none";
})

btnGY_Shifts .addEventListener("click", function () {
    GY_customersDiv.style.display = "none";
    GY_shiftsDiv.style.display = "block";
    GY_staffDiv.style.display = "none";
})
btnGY_Staff.addEventListener("click", function () {
    GY_customersDiv.style.display = "none";
    GY_shiftsDiv.style.display = "none";
    GY_staffDiv.style.display = "block";
})

// hide the divs
GY_shiftsDiv.style.display = "none";
GY_staffDiv.style.display = "none";

// SCHOOL
const StudentsDiv = document.getElementById("SC-STUDENTS");
const TeachersDiv = document.getElementById("SC-TEACHERS");
const CoursesDiv = document.getElementById("SC-COURSES");
const EnrollmentsDiv = document.getElementById("SC-ENROLLMENTS");
const LibraryBooksDiv = document.getElementById("SC-L-BOOKS");
const LibraryMembersDiv = document.getElementById("SC-L-MEMBERS");
const LibraryLoansDiv = document.getElementById("SC-L-LOANS");

const btnStudents = document.getElementById("btn-students");
const btnTeachers = document.getElementById("btn-teachers");
const btnCourses = document.getElementById("btn-courses");
const btnEnrollments = document.getElementById("btn-enrollments");
const btnLibraryBooks = document.getElementById("btn-librarybooks");
const btnLibraryMembers = document.getElementById("btn-librarymembers");
const btnLibraryLoans = document.getElementById("btn-libraryloans");

btnStudents.addEventListener("click", function () {
    StudentsDiv.style.display = "block";
    TeachersDiv.style.display = "none";
    CoursesDiv.style.display = "none";
    EnrollmentsDiv.style.display = "none";
    LibraryBooksDiv.style.display = "none";
    LibraryMembersDiv.style.display = "none";
    LibraryLoansDiv.style.display = "none";
})
btnTeachers.addEventListener("click", function () {
    StudentsDiv.style.display = "none";
    TeachersDiv.style.display = "block";
    CoursesDiv.style.display = "none";
    EnrollmentsDiv.style.display = "none";
    LibraryBooksDiv.style.display = "none";
    LibraryMembersDiv.style.display = "none";
    LibraryLoansDiv.style.display = "none";
})
btnCourses.addEventListener("click", function () {
    StudentsDiv.style.display = "none";
    TeachersDiv.style.display = "none";
    CoursesDiv.style.display = "block";
    EnrollmentsDiv.style.display = "none";
    LibraryBooksDiv.style.display = "none";
    LibraryMembersDiv.style.display = "none";
    LibraryLoansDiv.style.display = "none";
})
btnEnrollments.addEventListener("click", function () {
    StudentsDiv.style.display = "none";
    TeachersDiv.style.display = "none";
    CoursesDiv.style.display = "none";
    EnrollmentsDiv.style.display = "block";
    LibraryBooksDiv.style.display = "none";
    LibraryMembersDiv.style.display = "none";
    LibraryLoansDiv.style.display = "none";
})
btnLibraryBooks.addEventListener("click", function () {
    StudentsDiv.style.display = "none";
    TeachersDiv.style.display = "none";
    CoursesDiv.style.display = "none";
    EnrollmentsDiv.style.display = "none";
    LibraryBooksDiv.style.display = "block";
    LibraryMembersDiv.style.display = "none";
    LibraryLoansDiv.style.display = "none";
})
btnLibraryMembers.addEventListener("click", function () {
    StudentsDiv.style.display = "none";
    TeachersDiv.style.display = "none";
    CoursesDiv.style.display = "none";
    EnrollmentsDiv.style.display = "none";
    LibraryBooksDiv.style.display = "none";
    LibraryMembersDiv.style.display = "block";
    LibraryLoansDiv.style.display = "none";
})
btnLibraryLoans.addEventListener("click", function () {
    StudentsDiv.style.display = "none";
    TeachersDiv.style.display = "none";
    CoursesDiv.style.display = "none";
    EnrollmentsDiv.style.display = "none";
    LibraryBooksDiv.style.display = "none";
    LibraryMembersDiv.style.display = "none";
    LibraryLoansDiv.style.display = "block";
})

// hide the divs
TeachersDiv.style.display = "none";
CoursesDiv.style.display = "none";
EnrollmentsDiv.style.display = "none";
LibraryBooksDiv.style.display = "none";
LibraryMembersDiv.style.display = "none";
LibraryLoansDiv.style.display = "none";

