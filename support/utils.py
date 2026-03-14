from .models import BusinessFAQ

def get_answer_from_faq(user_query):
    """ডাটাবেজ থেকে উত্তর খুঁজে বের করার লজিক"""
    faqs = BusinessFAQ.objects.all()
    user_query = user_query.lower()

    for faq in faqs:
        # যদি ইউজারের প্রশ্নের ভেতরে ডাটাবেজের কোনো শব্দ থাকে
        if faq.question.lower() in user_query or user_query in faq.question.lower():
            return faq.answer

    # উত্তর না পাওয়া গেলে ডিফল্ট মেসেজ
    return "Thank you for reaching out. Our team will review your message and get back to you shortly."