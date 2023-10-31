import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from course.models import CourseApply


stripe.api_key = settings.STRIPE_SECRET_KEY
webhook_secret = settings.STRIPE_WEBHOOK_SECRET

FRONTEND_CHECKOUT_SUCCESS_URL = settings.CHECKOUT_SUCCESS_URL
FRONTEND_CHECKOUT_FAILED_URL = settings.CHECKOUT_FAILED_URL


class CreateCheckoutSession(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data_dict = dict(request.data)
        price = data_dict["price"][0]
        course = data_dict["name"][0]
        apply, _ = CourseApply.objects.get_or_create(course__slug=course, user=request.user)
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "product_data": {
                                "name": course,
                            },
                            "unit_amount": price,
                        },
                        "quantity": 1,
                    }
                ],
                mode="payment",
                success_url=f"{settings.SITE_URL}/courses/{course}/",
                cancel_url=FRONTEND_CHECKOUT_FAILED_URL,
            )
            apply.status = CourseApply.ApplyStatus.PAID
            apply.save()
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            print(e)
            return e


class WebHook(APIView):
    def post(self, request):
        event = None
        payload = request.body
        sig_header = request.META["HTTP_STRIPE_SIGNATURE"]

        try:
            event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
        except ValueError as err:
            # Invalid payload
            raise err
        except stripe.error.SignatureVerificationError as err:  # noqa
            # Invalid signature
            raise err

        # Handle the event
        if event.type == "payment_intent.succeeded":
            payment_intent = event.data.object
            print("--------payment_intent ---------->", payment_intent)
        elif event.type == "payment_method.attached":
            payment_method = event.data.object
            print("--------payment_method ---------->", payment_method)
        # ... handle other event types
        else:
            print("Unhandled event type {}".format(event.type))

        return JsonResponse(success=True, safe=False)
