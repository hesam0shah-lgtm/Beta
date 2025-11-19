# config.py

BOT_TOKEN = "2201475672:AAFPwLMmGZnwX6PH_3Nj7PGFtDX-O81eQnA/test"  # توکن ربات خود را اینجا قرار دهید
ADMIN_IDS = [5001296540]  # آی‌دی عددی ادمین‌ها

# تنظیمات Telethon (بعداً برای افزودن اکانت استفاده می‌شود)
API_ID = 24234031    # در بخش تنظیمات ربات توسط ادمین وارد خواهد شد
API_HASH = "5d4c8577195c633aebf1d35f5d19acdf"  # در بخش تنظیمات ربات توسط ادمین وارد خواهد شد

# تنظیمات دیتابیس
DATABASE_NAME = "data/database.db"

# مسیر پوشه‌ها
SESSIONS_DIR = "data/sessions/"
LOGS_DIR = "logs/"

# پیام‌های پیش‌فرض برای اسپمر (بعداً قابل ویرایش از طریق تنظیمات ربات)
DEFAULT_SPAM_MESSAGES = [
    "بيشعور",
    "بي تربيت",
    # ... موارد بیشتر
]
from telethon.tl import types


# دلایل ریپورت برای کاربر
REPORT_REASONS_USER_DATA = {
    "spam": {"display": "هرزنامه (Spam)", "obj": types.InputReportReasonSpam()},
    "violence": {"display": "خشونت (Violence)", "obj": types.InputReportReasonViolence()},
    "pornography": {"display": "محتوای جنسی (Pornography)", "obj": types.InputReportReasonPornography()},
    "child_abuse": {"display": "کودک آزاری (Child Abuse)", "obj": types.InputReportReasonChildAbuse()},
    "fake_account": {"display": "جعل هویت / اکانت جعلی (Fake Account)", "obj": types.InputReportReasonFake()},
    "drugs": {"display": "مواد مخدر (Illegal Drugs)", "obj": types.InputReportReasonIllegalDrugs()}, # <<< اضافه شد
    "other": {"display": "سایر دلایل (Other)", "obj": types.InputReportReasonOther()},
}
REPORT_REASON_CALLBACK_PREFIX_USER = "rep_user_rsn_"

# دلایل ریپورت برای کانال/گروه
REPORT_REASONS_CHAT_DATA = {
    "spam": {"display": "هرزنامه (Spam)", "obj": types.InputReportReasonSpam()},
    "violence": {"display": "خشونت (Violence)", "obj": types.InputReportReasonViolence()},
    "pornography": {"display": "محتوای جنسی (Pornography)", "obj": types.InputReportReasonPornography()},
    "child_abuse": {"display": "کودک آزاری (Child Abuse)", "obj": types.InputReportReasonChildAbuse()},
    "copyright": {"display": "نقض کپی‌رایت (Copyright)", "obj": types.InputReportReasonCopyright()},
    "fake_chat": {"display": "کانال/گروه جعلی (Fake/Scam)", "obj": types.InputReportReasonFake()},
    "drugs": {"display": "مواد مخدر (Illegal Drugs)", "obj": types.InputReportReasonIllegalDrugs()}, # <<< اضافه شد
    "geo_irrelevant": {"display": "محتوای نامرتبط جغرافیایی (Geo-irrelevant)", "obj": types.InputReportReasonGeoIrrelevant()}, # این دلیل ممکن است فقط برای برخی انواع چت‌ها معتبر باشد
    "other": {"display": "سایر دلایل (Other)", "obj": types.InputReportReasonOther()},
}
REPORT_REASON_CALLBACK_PREFIX_CHAT = "rep_chat_rsn_"


