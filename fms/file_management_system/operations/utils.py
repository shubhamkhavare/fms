from .models import UserCount

def update_user_count(mode):

    try:
        user_count_object = UserCount.objects.filter(id=1).last()
        if mode == 'image_to_pdf':
            user_count_object.image_to_pdf += 1
        elif mode == 'word_to_pdf':
            user_count_object.word_to_pdf += 1
        user_count_object.save()
        return True

    except Exception as e:
        return False