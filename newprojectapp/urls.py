from django.urls import path

from newprojectapp import views,adminviews,studentviews,parentviews




urlpatterns=[
    path('',views.new,name='new'),
    path('log',views.log,name='log'),
    path('signstudent',views.signstudent,name='signstudent'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('studentpage',views.studentpage,name='studentpage'),
    path('parentpage',views.parentpage,name='parentpage'),
    path('psign',views.psign,name='psign'),
    path('sview',adminviews.sview,name='sview'),
    path('pview',adminviews.pview,name='pview'),

    path('approve_student/<int:id>/',adminviews.approve_student,name='approve_student'),
    path('reject_student/<int:id>/',adminviews.reject_student,name='reject_student'),
    path('approve_parent/<int:id>/', adminviews.approve_parent, name='approve_parent'),
    path('reject_parent/<int:id>/', adminviews.reject_parent, name='reject_parent'),

    path('add_hostel',adminviews.add_hostel,name='add_hostel'),
    path('view_hostel',adminviews.view_hostel,name='view_hostel'),

    path('add_food',adminviews.add_food,name='add_food'),
    path('view_food',adminviews.view_food,name='view_food'),

    path('add_fee',adminviews.add_fee,name='add_fee'),
    path('view_fee',adminviews.view_fee,name='view_fee'),



    path('view_stud_pay',studentviews.view_stud_pay,name='view_stud_pay'),
    path('view_pay',adminviews.view_pay,name='view_pay'),
    path('add_admin_pay', adminviews.add_admin_pay, name='add_admin_pay'),
    path('approve_payment/<int:id>/', studentviews.approve_payment, name='approve_payment'),
    path('reject_payment/<int:id>/', studentviews.reject_payment, name='reject_payment'),


    path('add_notification',adminviews.add_notification,name='add_notification'),
    path('view_notification',adminviews.view_notification,name='view_notification'),

    path('add_attendance',adminviews.add_attendance,name='add_attendance'),
    path('view_attendance',adminviews.view_attendance,name='view_attendance'),

    path('add_staff',adminviews.add_staff,name='add_staff'),
    path('view_staff',adminviews.view_staff,name='view_staff'),

    path('hostel_update/<int:id>/', adminviews.hostel_update, name='hostel_update'),
    path('hostel_delete/<int:id>/', adminviews.hostel_delete, name='hostel_delete'),

    path('food_update/<int:id>/', adminviews.food_update, name='food_update'),
    path('food_delete/<int:id>/', adminviews.food_delete, name='food_delete'),

    path('fee_update/<int:id>/', adminviews.fee_update, name='fee_update'),
    path('fee_delete/<int:id>/', adminviews.fee_delete, name='fee_delete'),

    path('pay_update/<int:id>/', adminviews.pay_update, name='pay_update'),
    path('pay_delete/<int:id>/', adminviews.pay_delete, name='pay_delete'),

    path('notification_update/<int:id>/', adminviews.notification_update, name='notification_update'),
    path('notification_delete/<int:id>/', adminviews.notification_delete, name='notification_delete'),

    path('attendance_update/<int:id>/', adminviews.attendance_update, name='attendance_update'),
    path('attendance_delete/<int:id>/', adminviews.attendance_delete, name='attendance_delete'),

    path('staff_update/<int:id>/', adminviews.staff_update, name='staff_update'),
    path('staff_delete/<int:id>/', adminviews.staff_delete, name='staff_delete'),

    path('view_stud_hostel',studentviews.view_stud_hostel,name='view_stud_hostel'),
    path('view_stud_food',studentviews.view_stud_food,name='view_stud_food'),
    path('view_stud_fee',studentviews.view_stud_fee,name='view_stud_fee'),
    path('view_stud_attendance',studentviews.view_stud_attendance,name='view_stud_attendance'),
    path('view_stud_notification',studentviews.view_stud_notification,name='view_stud_notification'),
    # path('view_stud_pay',studentviews.view_stud_pay,name='view_stud_pay'),
    path('add_complaint',studentviews.add_complaint,name='add_complaint'),
    path('view_stud_complaint',studentviews.view_stud_complaint,name='view_stud_complaint'),

    path('view_complaint',adminviews.view_complaint,name='view_complaint'),

    path('view_par_hostel',parentviews.view_par_hostel,name='view_par_hostel'),
    path('view_par_attendance',parentviews.view_par_attendance,name='view_par_attendance'),
    path('view_par_fee',parentviews.view_par_fee,name='view_par_fee'),
    path('view_par_staff',parentviews.view_par_staff,name='view_par_staff'),
    path('view_par_notification',parentviews.view_par_notification,name='view_par_notification'),
    path('view_par_pay',parentviews.view_par_pay,name='view_par_pay'),

    path('add_booking',studentviews.add_booking,name='add_booking'),
    path('view_stud_booking',studentviews.view_stud_booking,name='view_stud_booking'),

    path('view_booking',adminviews.view_booking,name='view_booking'),
    path('booking_update/<int:id>/', studentviews.booking_update, name='booking_update'),
    path('booking_delete/<int:id>/', studentviews.booking_delete, name='booking_delete'),

    path('approve_booking/<int:id>/', adminviews.approve_booking, name='approve_booking'),
    path('reject_booking/<int:id>/', adminviews.reject_booking, name='reject_booking'),



    path('view_par_booking',parentviews.view_par_booking,name='view_par_booking'),
    path('profile_view',studentviews.profile_view,name='profile_view'),
    path('profile_update',studentviews.profile_update,name='profile_update'),
    path('add_review',studentviews.add_review,name='add_review'),
    path('view_stud_review',studentviews.view_stud_review,name='view_stud_review'),
    path('view_review',adminviews.view_review,name='view_review'),
    path('com_replay/<int:id>/', adminviews.com_replay, name='com_replay'),

    path('logout_view', adminviews.logout_view, name='logout_view'),
    path('logout_view', studentviews.logout_view, name='logout_view'),
    path('logout_view', parentviews.logout_view, name='logout_view'),

    path('delete_profile_student', studentviews.delete_profile_student, name='delete_profile_student'),
    path('cancel_profile_student', studentviews.cancel_profile_student, name='cancel_profile_student'),
    path('delete_profile_parent', parentviews.delete_profile_parent, name='delete_profile_parent'),









]