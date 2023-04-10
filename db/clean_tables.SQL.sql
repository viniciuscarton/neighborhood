TRUNCATE sm_employees, sm_functions, sm_shifts, sm_inventory RESTART IDENTITY;
TRUNCATE ba_accounts, ba_customers RESTART IDENTITY;
TRUNCATE ds_customers, ds_prescriptions, ds_storage, ds_suppliers RESTART IDENTITY;
TRUNCATE gy_customers, gy_shifts, gy_staff RESTART IDENTITY;
TRUNCATE pr_prayer RESTART IDENTITY;
TRUNCATE re_apartments, re_houses, re_residents RESTART IDENTITY;
TRUNCATE sc_courses, sc_enrollments, sc_library_books, sc_library_loans, sc_library_members,
sc_students, sc_teachers RESTART IDENTITY;

DROP TABLE auth_group CASCADE;
DROP TABLE auth_group_permissions CASCADE;
DROP TABLE auth_permission CASCADE;
DROP TABLE auth_user CASCADE;
DROP TABLE auth_user_groups CASCADE;
DROP TABLE auth_user_user_permissions CASCADE;
DROP TABLE django_admin_log CASCADE;
DROP TABLE django_content_type CASCADE;
DROP TABLE django_migrations CASCADE;



