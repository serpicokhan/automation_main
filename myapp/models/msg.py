from django.db import models
from myapp.models.users import *
class Msg(models.Model):
    fromUser=models.ForeignKey(SysUser,on_delete=models.CASCADE,related_name="fromuser1",verbose_name="از:",default=1)
    toUser=models.ForeignKey(SysUser,on_delete=models.CASCADE,related_name="touser1",verbose_name="به:",default=1)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="msg"
        ordering = ('date_added',)