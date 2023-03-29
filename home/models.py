

from django.db import models
from wagtail.models import Page, Orderable
from wagtail.admin.panels import (
    FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
)
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey


class HomePage(Page):
    body = RichTextField(blank=True, features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic','ol', 'ul', 'hr','link','document-link','image','embed','code','superscript', 'subscript', 'strikethrough','blockquote' ])

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]


# Define the Category model
class Category(models.Model):
    # Define the fields for the category

    name = models.CharField(max_length=255)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='category_images'
    )

    # Define the string representation of the model
    def __str__(self):
        return self.name

    # Define the metadata for the model
    class Meta:
        verbose_name_plural = "categories"

    # Define the panels for the category in the admin interface
    panels = [
        FieldPanel('name'),
        FieldPanel('image'),
    ]


# Define the Service model
class Service(Page):
    # Define the fields for the service

    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
    content = RichTextField(blank=True, features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic','ol', 'ul', 'hr','link','document-link','image','embed','code','superscript', 'subscript', 'strikethrough','blockquote' ])

    # Define the panels for the service in the admin interface
    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('category'),
        FieldPanel('content'),
    ]

    # Define the string representation of the model
    def __str__(self):
        return self.name


# Define the TeamMember model
class TeamMember(Page):
    # Define the fields for the team member

    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Define the panels for the team member in the admin interface
    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('position'),
        FieldPanel('bio'),
        FieldPanel('photo'),
    ]

    # Define the string representation of the model
    def __str__(self):
        return self.name


# Define the Project model
class Project(Page):
    # Define the fields for the project

    name = models.CharField(max_length=255)
    description = models.TextField()
    technologies = models.CharField(max_length=255)
    images = models.ManyToManyField(
        'wagtailimages.Image',
        blank=True,
        related_name='+'
    )
    content = RichTextField(blank=True, features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic','ol', 'ul', 'hr','link','document-link','image','embed','code','superscript', 'subscript', 'strikethrough','blockquote' ])

    # Define the panels for the project in the admin interface
    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('technologies'),
        FieldPanel('content'),
        InlinePanel('project_images', label="Images"),
    ]

    # Define the string representation of the model
    def __str__(self):
        return self.name


# Define the ProjectImage model for the images associated with each project
class ProjectImage(Orderable):
    # Define the fields for the project image

    project = ParentalKey(Project, on_delete=models.CASCADE, related_name='project_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )

    # Define the panels for in the Project Image admin interface
    panels = [
        FieldPanel('project'),
        FieldPanel('image'),
    ]
    # Define the string representation of the model
    def __str__(self):
        return self.image
