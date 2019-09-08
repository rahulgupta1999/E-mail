
from . import views
from django.urls import path

urlpatterns = [
	 path('index',views.index),
     path('register',views.register),
	 path('registerSave',views.registerSave),
	  path('login',views.login),
	   path('loginCheck',views.loginCheck),
	   path('composeOpen',views.composeOpen),
	   	   path('inboxOpen',views.inboxOpen),
		   	   path('sendboxOpen',views.sendboxOpen),
			   	   path('changepasswordOpen',views.changepasswordOpen),
				   	   path('composeSave',views.composeSave),
					    			   	   path('changepassword',views.changepassword),
                                          path('checkEmail',views.checkEmail),
]

