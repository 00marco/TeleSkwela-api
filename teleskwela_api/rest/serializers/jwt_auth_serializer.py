from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import exceptions, serializers
from rest.models import Student


class CustomTokenObtainSerializer(serializers.Serializer):

    default_error_messages = {
        'no_active_account': ('No active account found with the given credentials')
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields[self.username_field] = serializers.CharField()
        # self.fields['password'] = PasswordField()
        self.fields['api_key'] = serializers.CharField()

    def custom_authenticate(self, authenticate_kwargs):
        api_key = authenticate_kwargs['api_key']
        student = Student.objects.filter(api_key = api_key).first()
        return student

    def validate(self, attrs):
        authenticate_kwargs = {
            # self.username_field: attrs[self.username_field],
            # 'password': attrs['password'],
            'api_key': attrs['api_key']
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        self.user = self.custom_authenticate(authenticate_kwargs)

        # Prior to Django 1.10, inactive users could be authenticated with the
        # default `ModelBackend`.  As of Django 1.10, the `ModelBackend`
        # prevents inactive users from authenticating.  App designers can still
        # allow inactive users to authenticate by opting for the new
        # `AllowAllUsersModelBackend`.  However, we explicitly prevent inactive
        # users from authenticating to enforce a reasonable policy and provide
        # sensible backwards compatibility with older Django versions.
        if self.user is None or not self.user.is_active:
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )

        return {}

    @classmethod
    def get_token(cls, user):
        raise NotImplementedError('Must implement `get_token` method for `TokenObtainSerializer` subclasses')


class CustomTokenObtainPairSerializer(CustomTokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data