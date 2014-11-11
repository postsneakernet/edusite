from django.db import models


def course_dir(instance, filename):
    return '/'.join(['courses', instance.slug,'course_details', filename])


def module_dir(instance, filename):
    return '/'.join(['courses', instance.course.slug, 'modules', instance.slug, filename])


def file_dir(instance, filename):
    return '/'.join(['courses', instance.module.course.slug, 'modules', 
        instance.module.slug, filename])


def assignment_dir(instance, filename):
    return '/'.join(['courses', instance.course.slug, 'assignments', 
        instance.title, filename])


class ModuleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class AssignmentQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="course name")
    prefix = models.CharField(max_length=20, verbose_name="course abbreviation")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="unique name")
    photo = models.ImageField(upload_to=course_dir, null=True, blank=True,
            verbose_name="course photo")
    office_hours = models.CharField(max_length=200)
    grades = models.CharField(max_length=200, null=True, blank=True)
    final = models.DateTimeField(null=True, blank=True)
    syllabus_pdf = models.FileField(upload_to=course_dir, null=True, blank=True)
    syllabus = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=200)
    prefix = models.CharField(max_length=20, verbose_name="course abbreviation")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="unique name")
    course = models.ForeignKey(Course)
    topic = models.CharField(max_length=200)
    module_pdf = models.FileField(upload_to=module_dir, null=True, blank=True)
    body = models.TextField()
    activity = models.TextField()
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = ModuleQuerySet.as_manager() 

    def __str__(self):
        return self.title


class File(models.Model):
    file = models.FileField(upload_to=file_dir)
    module = models.ForeignKey(Module)
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Assignment(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course)
    due_date = models.DateTimeField()
    assignment_pdf = models.FileField(upload_to=assignment_dir, null=True, blank=True)
    misc_file = models.FileField(upload_to=assignment_dir, null=True, blank=True,
            verbose_name="additional file")
    body = models.TextField()
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects =AssignmentQuerySet.as_manager()

    def __str__(self):
        return self.title

