
from rest_framework.routers import SimpleRouter
from .views import ApiView, UserList

router = SimpleRouter()
router.register('users', UserList, basename='users')
router.register('', ApiView, basename='posts')
urlpatterns = router.urls