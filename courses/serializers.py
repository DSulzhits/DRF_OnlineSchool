from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from rest_framework.relations import SlugRelatedField
from courses.models import Course, Lesson, Payment, CourseSubscription
from users.models import User
from courses.validators import ScamValidator


class LessonSerializer(ModelSerializer):
    # video_url = CharField(validators=[validator_scam_links])

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [ScamValidator(field='video_url')]


class LessonListSerializer(ModelSerializer):
    course = SlugRelatedField(slug_field="title", queryset=Course.objects.all())
    owner = SlugRelatedField(slug_field="email", queryset=User.objects.all())

    class Meta:
        model = Lesson
        fields = ("title", "course", "owner",)


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')
    lessons_number = SerializerMethodField()
    subscribe_status = SerializerMethodField

    def get_lessons_number(self, course):
        lessons = Lesson.objects.filter(course=course)
        if lessons:
            return lessons.count()
        return 0

    def get_subscribe_status(self, instance):
        user = self.context['request'].user.id
        object = CourseSubscription.objects.filter(course=instance).filter(user=user)
        if object:
            return object.first().status
        return False

    class Meta:
        model = Course
        fields = '__all__'


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class CourseSubscriptionSerializer(ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = "__all__"

# class PaymentCreateSerializer(ModelSerializer):
#     class Meta:
#         model = Payment
#         fields = ("course",)
