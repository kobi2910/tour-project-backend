from rest_framework import permissions



class IsOwnerOrAdminPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.owner == request.user:
            return True
        return PermissionError() 


class IsGuidePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_guide:
            return True
        
    
    