# Mail Outreach Helpers

# أدوات إرسال البريد

أدوات برمجية لأتمتة إرسال رسائل بريدية مرفقة بالسيرة الذاتية دفعة واحدة.

يحتوي المشروع حاليًا على:

- `mass_mailer_txt.py`: يرسل رسائل البريد إلى قائمة عناوين مخزنة في ملف نصي. هذا هو السكربت الرئيسي المقترح للاستخدام.
- `mass_mailer.py`: يقرأ البيانات من ملف إكسل تم تصميمه وفق احتياجات المؤلف، ويمكن تكييفه مع جدولك بعد بعض التعديلات.

يشرح الدليل التالي كيفية تهيئة وتشغيل `mass_mailer_txt.py`.

## المتطلبات الأساسية

- بايثون 3.10 أو أحدث.
- حساب Gmail مفعّل عليه التحقق بخطوتين مع إنشاء كلمة مرور للتطبيق لخدمة "Mail".
- ملف السيرة الذاتية بصيغة PDF (أو أي وثيقة ترغب في إرفاقها).
- ملف نصي يحتوي على عنوان بريد إلكتروني واحد في كل سطر. يتم تجاهل التكرارات والعناوين غير الصحيحة تلقائيًا.

## تهيئة `mass_mailer_txt.py`

افتح الملف وعدّل قسم الإعدادات أعلى الكود.

- `EMAIL_ADDRESS`: بريدك الإلكتروني على Gmail.
- `EMAIL_PASSWORD`: كلمة مرور التطبيق المكوّنة من 16 حرفًا.
- `SUBJECT`: موضوع الرسالة الذي سيظهر لجميع المستلمين.
- `RESUME_PATH`: مسار ملف السيرة الذاتية (نسبي أو مطلق).
- `EMAILS_PATH`: مسار ملف `.txt` الذي يحتوي على قائمة المستلمين.
- `DRY_RUN`: اتركه `True` أثناء الاختبار؛ ستُرسل الرسائل فقط إلى `Test_Email` و`Test_Email2`.
- `Test_Email` / `Test_Email2`: عناوين بريدية تختبر بها الرسالة قبل الإرسال الحقيقي.
- الحقول `CONTACT_*` و`GITHUB_URL` و`LINKEDIN_URL` و`PORTFOLIO_URL`: روابط اختيارية تظهر في توقيع الرسالة.
- استبدل الجملة `WRITE YOUR MESSAGE HERE` (في النص العادي ونسخة HTML) بنص رسالتك. احتفظ بالتنسيق إذا رغبت في توقيع منسّق.

## تجهيز قائمة المستلمين

أنشئ ملفًا نصيًا بترميز UTF-8 (مثل `mails.txt`) يحتوي على عنوان بريد إلكتروني واحد في كل سطر. يتم تجاهل الأسطر الفارغة والتكرارات تلقائيًا. يمكنك حفظ أكثر من قائمة (مثل `mails2.txt`) وتغيير قيمة `EMAILS_PATH` وفق القائمة المطلوبة.

## وضع الاختبار (موصى به)

1. اضبط `DRY_RUN = True`.
2. تأكد من أن `Test_Email` (و `Test_Email2` إن استخدمتها) تعود إليك.
3. نفّذ الأمر:

   ```powershell
   python mass_mailer_txt.py
   ```

4. افحص الرسالة في صندوق الوارد لديك، وعدّل الصياغة أو التوقيع حتى تصل إلى النتيجة المناسبة.

## إرسال الحملة الفعلية

1. غيّر `DRY_RUN` إلى `False`.
2. تأكد من صحة المسارات (`RESUME_PATH` و`EMAILS_PATH`) ومحتوى الرسالة.
3. نفّذ الأمر:

   ```powershell
   python mass_mailer_txt.py
   ```

4. سيعرض السكربت كل مستلم ويطبع حالة النجاح (`✅`) أو الفشل (`❌`). يتضمن السكربت مهلة مقدارها خمس ثوانٍ بين الرسائل لتجنّب تجاوز حدود Gmail.

إذا فشل الإرسال لأحد العناوين، يكمل السكربت مع البقية. راجع المخرجات في الطرفية لتحديد العناوين غير الصحيحة أو مشكلات المصادقة.

## نصائح لاستكشاف الأخطاء وإصلاحها

- أخطاء المصادقة عادة تعني أن كلمة مرور التطبيق غير صحيحة أو أن التحقق بخطوتين غير مفعّل.
- ظهور خطأ `FileNotFoundError` يعني أن `RESUME_PATH` أو `EMAILS_PATH` يشير إلى ملف غير موجود. تحقق من الأسماء أو استخدم المسارات المطلقة.
- إذا أوقف Gmail النشاط، انتظر قليلًا ثم حاول مرة أخرى؛ الكميات الكبيرة خلال فترة قصيرة قد تُفعل حدود الخدمة.

## اختيارية: سير العمل باستخدام إكسل

يعرض `mass_mailer.py` كيفية استخراج العناوين من ملف إكسل (`comp.xlsx`). يحتاج إلى مكتبة `pandas` وتم تصميمه لأسماء أعمدة محددة. ثبّت التبعيات عبر `pip install pandas` وعدّل منطق القراءة قبل الاستخدام.

## قائمة تحقق سريعة

- راجع نص الرسالة والتوقيع لغويًا.
- أرسل لنفسك رسالة اختبار نهائية مع `DRY_RUN = False` وعنوان واحد مضمون.
- احترم الأنظمة المحلية المتعلقة بالاتصالات الجماعية.

# Mail Outreach Helpers

Automation scripts for sending batches of personalized outreach emails with your resume attached.

The project currently contains:

- `mass_mailer_txt.py`: sends emails to a list of addresses stored in a plain-text file. This is the primary script most users will run.
- `mass_mailer.py`: parses addresses from an Excel sheet that matches the author's internal layout (optional; requires tweaking for your own spreadsheet).

The sections below focus on getting `mass_mailer_txt.py` ready to use.

## Prerequisites

- Python 3.10 or newer.
- A Gmail account with [2-Step Verification](https://myaccount.google.com/security) enabled and an App Password generated for "Mail".
- A PDF resume (or any document you plan to attach).
- A text file containing one recipient email address per line (duplicates and malformed addresses are filtered automatically).

## Configure `mass_mailer_txt.py`

Open `mass_mailer_txt.py` and adjust the configuration block at the top of the file.

- `EMAIL_ADDRESS`: your Gmail address.
- `EMAIL_PASSWORD`: the 16-character app password you generated.
- `SUBJECT`: subject line to appear in every outgoing message.
- `RESUME_PATH`: absolute or relative path to the attachment you want to send.
- `EMAILS_PATH`: path to the `.txt` file that contains your recipient list.
- `DRY_RUN`: keep `True` while testing—emails go only to `Test_Email` / `Test_Email2`.
- `Test_Email` / `Test_Email2`: dummy addresses you control for dry runs.
- `CONTACT_*` / `GITHUB_URL` / `LINKEDIN_URL` / `PORTFOLIO_URL`: optional links used in the email signature.
- Replace the placeholder text `WRITE YOUR MESSAGE HERE` (both plain-text and HTML sections) with the body of your email. Keep the formatting if you want the signature to render nicely.

## Prepare Your Recipient List

Create a UTF-8 encoded text file—`mails.txt` for example—with one email address per line. Blank lines and duplicates are ignored automatically. You can maintain multiple lists (e.g., `mails2.txt`) and point `EMAILS_PATH` to whichever list you want.

## Test Mode (Highly Recommended)

1. Set `DRY_RUN = True`.
2. Ensure `Test_Email` (and optionally `Test_Email2`) are addresses you control.
3. Run the script:

   ```powershell
   python mass_mailer_txt.py
   ```

4. Confirm the message looks correct in your inbox. Adjust the wording and signature until satisfied.

## Send the Campaign

1. Flip `DRY_RUN` to `False`.
2. Double-check `RESUME_PATH`, `EMAILS_PATH`, and the message body.
3. Run the script:

   ```powershell
   python mass_mailer_txt.py
   ```

4. The script prints each recipient and reports success (`✅`) or failure (`❌`). A five-second pause between messages helps avoid Gmail rate limits.

If a send fails, the script continues with the next address. Review the console output to identify any invalid addresses or authentication issues.

## Troubleshooting Tips

- Authentication errors usually mean the Gmail app password is incorrect or 2-Step Verification is disabled.
- `FileNotFoundError` indicates `RESUME_PATH` or `EMAILS_PATH` is pointing to a non-existent file. Check spelling and use absolute paths if necessary.
- If Gmail flags the activity, wait and try again—heavy sending in a short window may trigger rate limits.

## Optional: Excel-Based Workflow

`mass_mailer.py` demonstrates how to extract emails from a structured Excel file (`comp.xlsx`). It requires `pandas` and is tailored to the author's column names. Install dependencies with `pip install pandas` and adapt the parsing logic before use.

## Good Practice Checklist

- Proofread your email copy and signature.
- Send yourself a final test message with `DRY_RUN = False` but a single known-good address.
- Respect privacy laws and company policies when sending mass outreach emails.
