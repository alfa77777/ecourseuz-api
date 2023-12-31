from django.urls import path

from common.views import (
    AboutUsListApiViews,
    ApplicationFormView,
    BannerApiView,
    BlogDetail,
    BlogList,
    BoardTextView,
    ContactFormView,
    ContactUsListApiView,
    SocialMediaList,
    TestimonialsListView,
)


app_name = "common"
urlpatterns = [
    path("blogs/", BlogList.as_view(), name="blog-list"),
    path("blogs/<slug:slug>/", BlogDetail.as_view(), name="blog-detail"),
    path("banner/", BannerApiView.as_view(), name="banner"),
    path("application-form/", ApplicationFormView.as_view(), name="application-form"),
    path("about-us/", AboutUsListApiViews.as_view(), name="about-us"),
    path("contact/", ContactUsListApiView.as_view(), name="contact-us"),
    path("contact-form/", ContactFormView.as_view(), name="contact-form"),
    path("social-medias/", SocialMediaList.as_view(), name="social-media-list"),
    path("testimonials/", TestimonialsListView.as_view(), name="testimonial-list"),
    path("board/", BoardTextView.as_view(), name="board"),
]
