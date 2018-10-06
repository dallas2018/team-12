from django.contrib.auth import authenticate
from rest_framework import serializers
from drf_compound_fields.fields import ListField
from apps.user_info.models import primary_doctor
from apps.user_info.serialization import *
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):
    """Serilaizers registration requests and create a new user"""

    password = serializers.CharField(
        max_length = 128,
        min_length = 8,
        write_only = True
    )

    token = serializers.CharField(max_length = 255 , read_only = True)

    class Meta:
        model = User
        fields = ('id','username','email','firstname','mi','lastname','password','token')

        read_only = ('id',)
    def create(self , validated_data):
        return User.objects.create_user(**validated_data)





class LoginSerilaizer(serializers.Serializer):

    email = serializers.CharField(max_length = 255)

    username = serializers.CharField(max_length=255, read_only = True)

    password = serializers.CharField(max_length = 128  , write_only = True)

    token = serializers.CharField(max_length = 255 , read_only = True)

    id = serializers.CharField(max_length = 255, read_only = True)
    #firstname = serializers.CharField(max_length = 75, read_only = True)

    lastname = serializers.CharField(max_length = 100 , read_only = True)

    def validate(self , data):

        email = data.get('email',None)

        password = data.get('password',None)

        if email is None:
            raise serializers.ValidationError(
                "An email address is required to log in"
            )

        if password is None:
            raise serializers.ValidationError(
                "A password is required"
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                "A user with this email and password does not exist"
            )

        if not user.is_active:
            raise serializers.ValidationError(
                "The user has been deactivated"
            )
        return {
            "id" : user.id,
            "email" : user.email,
            "username" : user.username,
            "token": user.token

        }


class UserSerializer(serializers.ModelSerializer):


    """Handles Serilialization and deserialization of users"""

    password = serializers.CharField(
        max_length = 128,
        min_length = 8,
        write_only = True
    )

    class Meta:
        model = User
        fields = ('password','username','firstname','mi','lastname','email','token',)

        read_only_fields = ('token')


    def update(self,instance, validated_data):
        """perform a user update"""

        print(validated_data)

        password = validated_data.pop('password',None)

        for (key,value) in validated_data.items():
            setattr(instance ,key , value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance

class CompleteUserSerializer(serializers.ModelSerializer):

    
    doctor = Doctor_Serilaizer(read_only = True)

    insurance = Insurance_Serializer(read_only = True)

    generic_info = Generic_Info_Serializer(read_only = True)
   
    emergency_contacts = Emergency_Info_Serializer(many=True,read_only = True) 
    
    visits = Visitation_Serializer(read_only = True,many=True)
    class Meta:
        model = User
        fields = ('id','username','firstname','lastname','token','doctor','generic_info','insurance','emergency_contacts', 'visits')

        read_only_fields =('id','token',)

"""
class UserProfileProperties_Profile_Page_Serilaizer(serializers.ModelSerializer):

    doctor = Doctor_Serilaizer()
    insurance = Insurance_Serializer()
    generics = Generic_Info_Serializer()
    emergency_contacts = Emergency_Info_Serializer(many =True)
    class Meta:
        model = User
        fields = ('id','token','doctor','insurance','generics','emergency_contacts')
        read_only_fields = ('id','token',)
        
    def create(self ,validated_data):
        
        doctor_data = validated_data.pop('doctor')
        user_pk  = doctor_data['user']
        doctor_data.pop('user')
        curr_user = User.objects.get(pk = user_pk)
        
        insurance_data = validated_data.pop('insurance')
        insurance_data.pop('user')
        
        generic_data = validated_data.pop('generics')


        contact_data = validated_data.pop('emergency_contacts')
        for contact in contact_data:
            emergency_info.objects.create(**contact)

        primary_doctor.objects.create(user=curr_user,**doctor_data) 
        insurance_info.objects.create(user=curr_user,**insurance_data)
        generic_info.objects.create(user=curr_user,**generic_data)
        
        
        return curr_user
"""
class UserProfileProperties_Profile_Page_Serilaizer(serializers.ModelSerializer):

    doctor = Doctor_Serilaizer(required = False)
    insurance = Insurance_Serializer(required = False)
    generics = Generic_Info_Serializer(required = False)
    emergency_contacts = Emergency_Info_Serializer(required = False ,many =True)
    id  = serializers.IntegerField() 
    class Meta:
        model = User
        fields = ('id','token','firstname','lastname','mi','doctor','insurance','generics','emergency_contacts')
        read_only_fields = ('token','id')
        validators = [] 
    
    
    def create(self ,validated_data):
        user_id = validated_data.get('id')
        curr_user = User.objects.get(pk = user_id)

        doctor_data = validated_data.pop('doctor')
        
        insurance_data = validated_data.pop('insurance')
        
        generic_data = validated_data.pop('generics')

        contact_data = validated_data.pop('emergency_contacts')
        for contact in contact_data:
            emergency_info.objects.create(user = curr_user,**contact)

        primary_doctor.objects.create(user=curr_user,**doctor_data) 
        insurance_info.objects.create(user=curr_user,**insurance_data)
        generic_info.objects.create(user=curr_user,**generic_data)
        
        return curr_user

    
    def update(self, instance ,validated_data):
        #preliminaries
        doctor_data = validated_data.pop('doctor')
        insurance_data = validated_data.pop('insurance')
        generic_data = validated_data.pop('generics')
        emergency_data = validated_data.pop('emergency_contacts')

        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname',instance.lastname)
        instance.mi = validated_data.get('mi',instance.mi)
        instance.save()
        
        ########################### manage contact data ####################
        keep_emergency_contact_choice = []
        emergency_contacts_ids = []
        for ec in emergency_data:
            if 'id' in ec.keys():
                emergency_contacts_ids.append(ec['id'])
        
        for ec in instance.emergency_contacts.all():
            if ec.id not in keep_emergency_contact_choice:
                emergency_info.objects.get(id = str(ec)).delete()

        for contact in emergency_data:
            if 'id' in contact.keys():
                if emergency_info.objects.filter(id = contact['id']).exists():
                    c = emergency_info.objects.get(id= contact['id'])
                    c.firstname = contact.get('firstname',c.firstname)
                    c.lastname = contact.get('lastname',c.lastname)
                    c.relationship = contact.get('relationship',c.relationship)
                    c.phone = contact.get('phone',c.phone)
                    c.save()
                    keep_emergency_contact_choice.append(c.id)
                else:
                    continue
            else:
                c = emergency_info.objects.create(user = instance, **contact)
                keep_emergency_contact_choice.append(c.id)

        

        ####################################################################

        ########################### manage doctor data #####################
        tmp_doc = instance.doctor; 
        instance.doctor.doctor_firstname = doctor_data.get('doctor_firstname',tmp_doc.doctor_firstname)

        instance.doctor.doctor_lastname = doctor_data.get('doctor_lastname',tmp_doc.doctor_lastname)


        instance.doctor.phone_number= doctor_data.get('phone_number',tmp_doc.phone_number)

        instance.doctor.ext= doctor_data.get('ext',tmp_doc.ext)

        instance.doctor.address= doctor_data.get('address',tmp_doc.address)

        instance.doctor.save()
        #########################################################
        
        ################### manage insurance data ##############
        
        tmp_insur = instance.insurance
        
        instance.insurance.has_insurance=insurance_data.get('has_insurance',tmp_insur.has_insurance)

        instance.insurance.member_id=insurance_data.get('member_id',tmp_insur.member_id)

        instance.insurance.group_id=insurance_data.get('group_id',tmp_insur.group_id)

        instance.insurance.if_other=insurance_data.get('if_other',tmp_insur.if_other)


        instance.insurance.insurance = insurance_data.get('insurance',tmp_insur.insurance)
       
        instance.insurance.save()

       ###################################################

       ################### manage generic data ############

        tmp_generic = instance.generics

        instance.generics.blood_type = generic_data.get("blood_type",tmp_generic.blood_type)

        instance.generics.weigth_kg  = generic_data.get("weigth_kg",tmp_generic.weigth_kg)

        instance.generics.heigth_cm = generic_data.get('heigth_cm',tmp_generic.heigth_cm)

        instance.generics.save()
       ############################################################ 
        return instance




class UserProfile_Reg_Page1_Serializer(serializers.ModelSerializer):

    allergy = Allergies_Serializer(many = True) 
    visits =  Visitation_Serializer(many = True)
    supplements = Supplements_Serializer(many = True )
    pharmacy = Pharmacy_Serializer(many = True)
    id  = serializers.IntegerField() 

    class Meta:
        model = User
        fields = ('id','token','allergy','visits','supplements','pharmacy')
        read_only_fields = ('id','token')
    def create(self , validated_data):
        user_id = validated_data.get('id')
        curr_user = User.objects.get(pk = user_id)

        allergy_data = validated_data.pop('allergy')
        for a in allergy_data:
            allergies.objects.create(user = curr_user,**a)

        visit_data = validated_data.pop('visits')
        for v in visit_data:
            visit_reasons.objects.create(user = curr_user, **v)

        supplement_data = validated_data.pop('supplements')
        for s in supplement_data:
            supplements.objects.create(user = curr_user,**s)

        pharmacy_data = validated_data.pop('pharmacy')
        for p in pharmacy_data:
            pharmacy.objects.create(user = curr_user, **p)

        return curr_user
    def update(self, instance , validated_data):

        allergy_data = validated_data.pop('allergy')
        visits_data = validated_data.pop('visits')
        supp_data = validated_data.pop('supplements')
        phar_data = validated_data.pop('pharmacy')

        ###################### allergy update###############################
        keep_allergy_choices = []
        

        for a in allergy_data:
            if 'id' in a.keys():
                keep_allergy_choices.append(a['id'])
        for a in instance.allergy.all():
            if a.id not in keep_allergy_choices:
                allergies.objects.get(id = a.id).delete()

        for a in allergy_data:
            if 'id' in a.keys():
                if allergies.objects.filter(id = a['id']).exists():
                    tmp = allergies.objects.get(id = a['id'])
                    if tmp.allergy.id == 13:
                        tmp.if_other = a.get('if_other',tmp.if_other)
                        tmp.save()
                else:
                    continue
            else:
                tmp = allergies.objects.create(user = instance,**a)
                keep_allergy_choices.append(tmp.id)

        
################################################################################

        keep_visit_ids = []
    
        for v in visits_data:
           if 'id' in v.keys():
               keep_visit_ids.append(v['id'])

        for v in visits_data:
            if 'id' in v.keys():
                if visit_reasons.objects.filter(id=v['id']).exists():
                    tmp = visit_reasons.objects.get(id=v['id'])
                    tmp.medical_problem = v.get('medical_problem',tmp.medical_problem)
                    tmp.reason_for_visit= v.get('reason_for_visit',tmp.reason_for_visit)
                    tmp.save()

                else:
                    continue
            else:
                tmp  = visit_reasons.objects.create(user = instance , **v)
                keep_visit_ids.append(tmp.id)

        for v in instance.visits.all():
            if v.id not in keep_visit_ids:
                visit_reasons.objects.get(id = str(v.id)).delete()
##############################################################################
        keep_supp_choices = []
        
        for a in supp_data:
            if 'id' in a.keys():
                keep_supp_choices.append(a['id'])
        for a in instance.supplements.all():
            if a.id not in keep_supp_choices:
                supplements.objects.get(id = a.id).delete()

        for a in supp_data:
            if 'id' in a.keys():
                if supplements.objects.filter(id = a['id']).exists():
                    tmp = supplements.objects.get(id = a['id'])
                    if tmp.supplement_id == 29:
                        tmp.if_other = a.get('if_other',tmp.if_other)
                        tmp.save()
                else:
                    continue
            else:
                tmp = supplements.objects.create(user = instance,**a)
                keep_supp_choices.append(tmp.id)

       

##############################################################################
        keep_pharm_ids = []
    
        for v in phar_data:
           if 'id' in v.keys():
               keep_pharm_ids.append(v['id'])

        for v in phar_data:
            if 'id' not in v.keys():
                tmp  = pharmacy.objects.create(user = instance , **v)
                keep_visit_ids.append(tmp.id)

        for v in instance.pharmacy.all():
            if v.id not in keep_visit_ids:
                pharmacy.objects.get(id = str(v.id)).delete()


        return instance


class UserProfile_Reg_Page2_Serializer(serializers.ModelSerializer):

    family = Family_History_Serializer( many = True) 
    user_hosp_history = Hospitalization_Serializer(many=True)
    id  = serializers.IntegerField() 

    class Meta:
        model = User
        fields = ('id','token','family','user_hosp_history')
        read_only_fields = ('id','token')

    def create(self , validated_data):
       
        user_id = validated_data.get('id')
        curr_user = User.objects.get(pk = user_id)

        family_data = validated_data.pop('family')
        for member in family_data:
           family_hisotry.objects.create(user = curr_user,**member)

        user_hosp_history_date = validated_data.pop('user_hosp_history')
        for history in user_hosp_history_date:
            hospitalizations.objects.create(user = curr_user, **history)

        return curr_user

    def update(self, instance, validated_data):

        family_data = validated_data.pop('family')
        user_hosp_data = validated_data.pop('user_hosp_history')
        
##############################family data update #######################

        keep_fam_list = []

        for f in family_data:
            if 'id' in f.keys():
                keep_fam_list.append(f['id'])
        
        for f in instance.family.all():
            if f.id not in keep_fam_list:
                family_hisotry.objects.get(id = str(f.id)).delete()

        for f in family_data:
            if 'id' in f.keys():
                if family_hisotry.objects.filter(id=f['id']).exists():
                    tmp = family_hisotry.objects.get(id = f['id'])
                    tmp.realationship = f.get('relationship',tmp.realationship)
                    tmp.age_of_death = f.get('age_of_death',tmp.age_of_death)
                    tmp.reason = f.get('reason', tmp.reason)
                    tmp.save()
                else:
                    continue
            else:
                tmp = family_hisotry.objects.create(user = instance , **f)
                keep_fam_list.append(tmp.id)

       
################################################################################
        keep_hosp_list = []

        for f in user_hosp_data:
            if 'id' in f.keys():
                keep_hosp_list.append(f['id'])
        for f in instance.user_hosp_history.all():
            if f.id not in keep_hosp_list:
                hospitalizations.objects.get(id = str(f.id)).delete()

        for f in user_hosp_data:
            if 'id' in f.keys():
                if hospitalizations.objects.filter(id=f['id']).exists():
                    tmp = hospitalizations.objects.get(id = f['id'])
                    tmp.date = f.get('date',tmp.date)
                    tmp.type_reason = f.get('type_reason',tmp.type_reason)
                    tmp.reason = f.get('reason', tmp.reason)
                    tmp.save()
                else:
                    continue
            else:
                tmp = hospitalizations.objects.create(user = instance , **f)
                keep_hosp_list.append(tmp.id)

       

        return instance 
class Common_Heath_Issues_Serializer_Prime(serializers.ModelSerializer):

    common_health_issues = Medical_Issues_Serializer(many = True)
    id  = serializers.IntegerField() 

    class Meta:
        model = User
        fields = ('id','token','common_health_issues')
        read_only_fields = ('id','token')

    def create(self , validated_data):

        user_id = validated_data.get('id')
        curr_user = User.objects.get(pk  = user_id)

        common_health_issues_data = validated_data.pop("common_health_issues")
        
        for issue in common_health_issues_data:
            medical_issues.objects.create(user=curr_user,**issue)

        return curr_user

    def update(seld, instance, validated_data):

        keep_id = []

        heath_issues_data = validated_data.pop("common_health_issues")

        for a in heath_issues_data:
            if 'id' in a.keys():
                keep_id.append(a['id'])
        for a in instance.common_health_issues.all():
            if a.id not in keep_id:
                medical_issues.objects.get(id = a.id).delete()

        for a in heath_issues_data:
            if 'id' in a.keys():
                if medical_issues.objects.filter(id = a['id']).exists():
                    tmp = medical_issues.objects.get(id = a['id'])
                    if tmp.condition.id == 20:
                        tmp.if_other = a.get('if_other',tmp.if_other)
                        tmp.save()
                else:
                    continue
            else:
                tmp = medical_issues.objects.create(user = instance,**a)
                keep_id.append(tmp.id)

       
        return instance
#######################################################################

class Pill_Box_Group_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    users_pills = pill_box_pills_Serilaizer(many = True)
    
    class Meta:
        model = User
        fields = ('id','token','users_pills')
        read_only_fields = ('id','token')

    def create(self , validated_data):
        
        user_id = validated_data.get('id')
        pill_data  = validated_data.pop('users_pills')
        curr_user = User.objects.get(pk = user_id)
        
        for pill in pill_data:
            print(pill)
            schedule_data = pill.pop('pill_schedule')
            pill_obj = pill_box_pills.objects.create(user=curr_user,**pill)
            for date in schedule_data:
                print(date)
                schedule.objects.create(parent=pill_obj,**date)

        
        return curr_user

    def update(self , instance , validated_data):

#        print(validated_data)
        schedule_id = []
        pill_id = []
        pill_data = validated_data.pop("users_pills")

        for pill in pill_data:
            if 'id' in pill.keys():
                if pill_box_pills.objects.filter(id = pill['id']).exists():
                    tmp = pill_box_pills.objects.get(id = pill['id'])
                    tmp.start_date=pill.get('start_date',tmp.start_date)
                    tmp.end_date=pill.get('end_date',tmp.end_date)
                    tmp.pill = pill.get('pill',tmp.pill)
                    tmp_pill_schedule = pill.pop('pill_schedule') 
                    for date in tmp_pill_schedule:
                        if 'id' in date.keys():
                            print(date)
                            sch_inst = schedule.objects.get(id=date['id'])
                            sch_inst.location=date.get('location',sch_inst.location)
                            sch_inst.time=date.get('time',sch_inst.time)
                            sch_inst.day = date.get('day',sch_inst.day)

                            sch_inst.save()
                            schedule_id.append(sch_inst.id)
                        else:
                            new_date = schedule.objects.create( parent= tmp,**date)
                            schedule_id.append(new_date.id)

                    for a in tmp.pill_schedule.all():
                        if a.id not in schedule_id:
                            schedule.objects.get(id = a.id).delete()

                    tmp.save()
                    pill_id.append(tmp.id)
        
        for a in instance.users_pills.all():
           if a.id not in pill_id:
               pill_box_pills.objects.get(id = a.id).delete()


        return instance 

############################################################################

class User_end_pill_box_reg_Serializer(serializers.Serializer):
    
    pill_box_id = serializers.CharField(max_length = 50)


