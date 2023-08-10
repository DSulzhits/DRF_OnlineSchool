from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.relations import SlugRelatedField
from courses.models import Course, Lesson, Payment
from users.models import User


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonListSerializer(ModelSerializer):
    course = SlugRelatedField(slug_field="title", queryset=Course.objects.all())
    owner = SlugRelatedField(slug_field="email", queryset=User.objects.all())

    class Meta:
        model = Lesson
        fields = ("title", "course", "owner",)


class CourseSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')
    lessons_number = SerializerMethodField()

    def get_lessons_number(self, course):
        lessons = Lesson.objects.filter(course=course)
        if lessons:
            return lessons.count()
        return 0

    class Meta:
        model = Course
        fields = '__all__'


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

# class PaymentCreateSerializer(ModelSerializer):
#     class Meta:
#         model = Payment
#         fields = ("course",)
