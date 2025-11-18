# tasks/utils/email.py

from django.core.mail import send_mail

def send_task_created_email(user_email, task):
    subject = f"New Task Created: {task.title}"
    message = f"""
Hello,

A new task has been created for you:

Title: {task.title}
Description: {task.description}
Due Date: {task.due_date}

Best regards,
Smart Task Manager
"""
    send_mail(
        subject,
        message,
        'suliaman3@gmail.com',  # المرسل
        [user_email],            # المستقبل
        fail_silently=False,
    )


def send_task_summary_email(user_email, tasks):
    subject = "Today's Tasks Summary"
    message = "Here are your tasks for today:\n\n"
    for task in tasks:
        message += f"- {task.title}: {task.description}\n"
    
    send_mail(
        subject,
        message,
        'suliaman3@gmail.com',  # المرسل
        [user_email],            # المستقبل
        fail_silently=False,
    )