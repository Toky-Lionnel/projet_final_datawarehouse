import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from ingestion.logging.report_builder import build_pipeline_report


def send_pipeline_email():

    sender_email = "tokyrajaonarivony@gmail.com"
    sender_password = "cjampvrnzernywjf"

    receiver_email = "tokyrajaonarivony@gmail.com"

    html_report = build_pipeline_report()

    message = MIMEMultipart("alternative")

    message["Subject"] = "WorldTrade Pipeline Report"
    message["From"] = sender_email
    message["To"] = receiver_email

    html_content = f"""
    <html>
        <body>
            <h2>WorldTrade Pipeline Execution Report</h2>

            {html_report}

        </body>
    </html>
    """

    message.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

        server.login(sender_email, sender_password)

        server.sendmail(
            sender_email,
            receiver_email,
            message.as_string()
        )

    print("Pipeline report email sent")