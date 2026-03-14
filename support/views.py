import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from .models import AIEmailLog
from .utils import get_answer_from_faq

@csrf_exempt
def email_reply_webhook(request):
    """ইউজার ইমেইল করলে এই ভিউটি উত্তর পাঠাবে"""
    if request.method == "POST":
        try:
            # ১. পোস্টম্যান বা ইমেইল সার্ভিস থেকে ডাটা নেওয়া
            data = json.loads(request.body)
            sender_email = data.get('from')
            subject = data.get('subject', 'Inquiry Reply')
            question_text = data.get('text', '')

            # ২. ডাটাবেজ থেকে উত্তর খুঁজে বের করা (utils থেকে)
            answer = get_answer_from_faq(question_text)

            # ৩. কাস্টমারকে ইমেইল রিপ্লাই পাঠানো
            send_mail(
                f"Re: {subject}",
                answer,
                settings.EMAIL_HOST_USER,
                [sender_email],
                fail_silently=False,
            )

            # ৪. রেকর্ড সেভ করা
            AIEmailLog.objects.create(
                user_email=sender_email,
                user_question=question_text,
                ai_response=answer
            )

            return JsonResponse({"status": "success", "reply": answer}, status=200)

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)