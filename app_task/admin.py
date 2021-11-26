from django.contrib import admin

# Register your models here.
from app_task.models import App, Entity, Slot, Block, Task, Robot

admin.site.register(App)

admin.site.register(Robot)

admin.site.register(Task)

admin.site.register(Block)

admin.site.register(Slot)

admin.site.register(Entity)
