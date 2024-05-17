from rest_framework import serializers, status
from django.contrib.auth.models import User
from .models import ParkOwner, Zone, Booking, Vehicle, Subscription,Employee


class ParkownerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkOwner
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    mobile_no = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)
    payment_date = serializers.DateField(write_only=True,required=False)
    image = serializers.ImageField(required=False, write_only=True)

    class Meta:
        model = ParkOwner
        fields = ['username', 'first_name', 'last_name', 'mobile_no',
                  'nid_card_no', 'email', 'password', 'confirm_password', 'slot_size', 'capacity', 'address', 'area', 'payment_method', 'amount', 'payment_date','image']  

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        mobile_no = self.validated_data['mobile_no']
        nid_card_no = self.validated_data['nid_card_no']
        slot_size = self.validated_data['slot_size']
        capacity = self.validated_data['capacity']
        address = self.validated_data['address']
        area = self.validated_data['area']
        payment_method = self.validated_data['payment_method']
        amount = self.validated_data['amount']
        payment_date = self.validated_data['payment_date']
        image = self.validated_data.get('image', None)

        if password != password2:
            raise serializers.ValidationError(
                {'error': "Password Doesn't Matched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'error': "Email Already exists"})
        if ParkOwner.objects.filter(mobile_no=mobile_no).exists():
            raise serializers.ValidationError(
                {'error': "This mobile number is already in use"})

        user = User(username=username, email=email,
                    first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.is_active = False
        user.save()
        ParkOwner.objects.create(park_owner_id=user, mobile_no=mobile_no,
                                 id=user.id, nid_card_no=nid_card_no, address=address, slot_size=slot_size, capacity=capacity, area=area, payment_method=payment_method, payment_date=payment_date, image=image,amount=amount)

        return user

class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    mobile_no = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)
    email = serializers.CharField(write_only=True, required=True)
    joined_date = serializers.DateTimeField(write_only=True, required=True)
    class Meta:
        model = Employee
        fields = ['username', 'first_name', 'last_name','qualification', 'mobile_no',
                  'nid_card_no', 'email', 'password', 'confirm_password','address','joined_date']
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        qualification = self.validated_data['qualification']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        mobile_no = self.validated_data['mobile_no']
        nid_card_no = self.validated_data['nid_card_no']
        address = self.validated_data['address']
        joined_date = self.validated_data['joined_date']
        

        if password != password2:
            raise serializers.ValidationError(
                {'error': "Password Doesn't Matched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'error': "Email Already exists"})
        if Employee.objects.filter(mobile_no=mobile_no).exists():
            raise serializers.ValidationError(
                {'error': "This mobile number is already in use"})
        
        user = self.context['request'].user  # Getting the logged-in user
        try:
            park_owner = ParkOwner.objects.get(park_owner_id=user)
        except ParkOwner.DoesNotExist:
            raise serializers.ValidationError(
                {'error': "Logged in user is not a ParkOwner"})

        employee = User(username=username, email=email,
                    first_name=first_name, last_name=last_name)
        employee.set_password(password)
        employee.is_active = False
        employee.save()
        Employee.objects.create(employee=employee, mobile_no=mobile_no,
                                 id=employee.id, nid_card_no=nid_card_no, address=address, qualification=qualification, joined_date=joined_date, park_owner_id= park_owner)

        return employee
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):
                return data
            else:
                raise serializers.ValidationError(
                    "Incorrect username or password.",
                    code='invalid_credentials',
                    status_code=status.HTTP_401_UNAUTHORIZED
                )
        else:
            raise serializers.ValidationError(
                "Both username and password are required.",
                code='missing_credentials',
                status_code=status.HTTP_400_BAD_REQUEST
            )

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['park_owner_id','name', 'capacity', 'created_at']

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['plate_number', 'mobile_no']


class BookingSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()
    ticket_no = serializers.SerializerMethodField()
    class Meta:
        model = Booking
        fields = ['zone', 'slot', 'time_slot', 'vehicle', 'ticket_no']
        read_only_fields = ['ticket_no']

    def get_ticket_no(self, instance):
        return instance.ticket_no()

    def create(self, validated_data):
        vehicle_data = validated_data.pop('vehicle')
        vehicle = Vehicle.objects.create(**vehicle_data)
        booking = Booking.objects.create(
            vehicle=vehicle, status=True, **validated_data)
        return booking


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'package', 'start_date', 'end_date', 'amount']
        read_only_fields = ['end_date', 'amount']

    # Read-only field for amount
    amount = serializers.ReadOnlyField()

    def create(self, validated_data):
        instance = Subscription(**validated_data)
        instance.save()
        return instance
