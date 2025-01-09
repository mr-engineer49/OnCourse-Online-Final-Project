from django.shortcuts import get_object_or_404, render, redirect
# from .models import Payment
# import stripe

# stripe.api_key = 'YOUR_STRIPE_SECRET_KEY'

# def pay_for_course(request, course_pk):
#     course = get_object_or_404(Course, pk=course_pk)
#     if request.method == 'POST':
#         # Process payment using Stripe
#         session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[{
#                 'price_data': {
#                     'currency': 'usd',
#                     'product_data': {
#                         'name': course.title,
#                     },
#                     'unit_amount': int(course.price * 100),
#                 },
#                 'quantity': 1,
#             }],
#             mode='payment',
#             success_url='http://localhost:8000/payments/success/',
#             cancel_url='http://localhost:8000/payments/cancel/',
#         )
#         return redirect(session.url, code=303)
#     return render(request, 'payments/pay.html', {'course': course})

# def payment_success(request):
#     # Handle successful payment
#     return render(request, 'payments/success.html')

# def payment_cancel(request):
#     # Handle cancelled payment
#     return render(request, 'payments/cancel.html')

def payment(request):
    return render(request, 'payments/pay.html') 