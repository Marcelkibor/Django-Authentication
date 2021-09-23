from rest_framework import serializers
from .models import User
class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {
        'password':{'write_only':True}# blocks write access to password field
    }
    def create(self, validated_data):
        unharshedpass = validated_data.pop('password', None)
        newuser = self.Meta.model(**validated_data)# userwithout any password
        if unharshedpass is not None:
            newuser.set_password(unharshedpass)
        newuser.save()


        return newuser 