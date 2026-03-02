from rest_framework import permissions

class IsSuperUser(permissions):
    def has_permission(self,request,view):
        return bool(request.user and request.user. is_superuser)
    
    