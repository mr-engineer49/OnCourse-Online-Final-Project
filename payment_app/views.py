from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse
from payments import get_payment_model, RedirectNeeded
from .models import Course



def payment(request):
    return render(request, 'payments/pay.html') 



def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    Payment = get_payment_model()

    # Create a payment object
    payment = Payment(
        variant='dummy',  # Use the Dummy backend
        description=f'Enrollment in {course.title}',
        total=course.price,  # Set the course price as the payment amount
        tax=0,  # No tax for testing
        currency='USD',  # Set the currency
        delivery=0,  # No delivery cost
    )
    payment.save()

    try:
        # Redirect to the payment process
        form = payment.get_form()
        raise RedirectNeeded(payment.get_process_url())
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))